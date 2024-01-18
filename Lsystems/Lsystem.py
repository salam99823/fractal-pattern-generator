"""

"""
from json import dumps, loads
from re import escape, finditer, sub
from sqlite3 import connect as sql_connect
from typing import Generator, Iterable


class LSystem(object):
    """
    """
    __rules: tuple[tuple[str, str], ...] = ()
    __keywords: tuple[tuple[str, ...], ...] = ()
    
    def __init__(
            self,
            rules: Iterable[str] | None = None,
            keywords: Iterable[Iterable[str]] | None = None,
    ):
        """
        :param rules:
        :param keywords:
        """
        if keywords is not None:
            self.keywords = keywords
        if rules is not None:
            self.rules = rules
    
    @property
    def rules(self) -> tuple[tuple[str, str], ...]:
        """
        
        """
        return self.__rules
    
    @rules.setter
    def rules(self, rules: Iterable[str]) -> None:
        """
        
        """
        if isinstance(rules, Iterable):
            for rule in rules:
                rule = self.multiplication(rule).split('->', maxsplit = 1)
                if len(rule) == 2:
                    self.__rules += (tuple(rule),)
        else:
            raise TypeError("Invalid type for rules.")
    
    @property
    def keywords(self) -> tuple[tuple[str, ...], ...]:
        """
        Get the keywords of the LSystem.

        :return: Tuple of keywords.
        """
        return self.__keywords
    
    @keywords.setter
    def keywords(self, keywords: Iterable[Iterable[str]]) -> None:
        """
        Set the keywords of the LSystem.
        """
        if not isinstance(keywords, Iterable):
            raise TypeError("Invalid type for keywords. Must be an iterable.")
        temp_keywords = []
        for keyword in keywords:
            if isinstance(keyword, str):
                if keyword:
                    temp_keywords.append((keyword,))
            elif isinstance(keyword, Iterable):
                temp_keywords.append(tuple(sorted(keyword, key = len)))
            else:
                raise TypeError("Invalid type for keywords. Must be an iterable of strings or iterables of strings.")
        self.__keywords = tuple(temp_keywords)
    
    def generate_action_string(
            self,
            string: str,
            number_of_iterations: int,
    ) -> tuple[tuple[str, int]]:
        """
        Generate the action string based on the LSystem.

        :param string: Starting string.
        :param number_of_iterations: Number of iterations to perform.
        :return: List of tuples representing the action string.
        """
        
        def generate(string_: str) -> tuple:
            """
            :param string_: some string
            :return:
            """
            for _ in range(number_of_iterations):
                for _key, _value in self.rules:
                    string_ = string_.replace(_key, _value)
            action_string_ = tuple(self.formatting(string_))
            cursor.execute(
                    """
                    INSERT INTO conclusions (rule_id, Keywords_array_id, axiom_id, n_iter, conclusion)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (*temp, number_of_iterations, dumps(action_string_))
            )
            return action_string_
        
        def insert_into_tables(table: str, column: str, value: str) -> int:
            """
            :param table:
            :param column:
            :param value:
            :return:
            """
            cursor.execute(f"SELECT {column}_id FROM {table} WHERE {column} = ?", (value,))
            if not cursor.fetchone():
                cursor.execute(f"INSERT INTO {table} ({column}) VALUES (?)", (value,))
            cursor.execute(f"SELECT {column}_id FROM {table} WHERE {column} = ?", (value,))
            return cursor.fetchone()[0]
        
        with sql_connect("../Lsystem_outs.db") as connection:
            cursor = connection.cursor()
            cursor.executescript(
                    """
                    CREATE TABLE IF NOT EXISTS rules (
                        rule_id INTEGER NOT NULL UNIQUE,
                        rule TEXT UNIQUE,
                        PRIMARY KEY("rule_id" AUTOINCREMENT)
                    );
                    CREATE TABLE IF NOT EXISTS axioms (
                        axiom_id INTEGER NOT NULL UNIQUE,
                        axiom TEXT NOT NULL UNIQUE,
                        PRIMARY KEY("axiom_id" AUTOINCREMENT)
                    );
                    CREATE TABLE IF NOT EXISTS conclusions (
                        conclusion_id INTEGER NOT NULL UNIQUE,
                        rule_id INTEGER NOT NULL,
                        Keywords_array_id INTEGER NOT NULL,
                        axiom_id INTEGER NOT NULL,
                        n_iter INTEGER NOT NULL DEFAULT 1,
                        conclusion BLOB NOT NULL,
                        PRIMARY KEY("conclusion_id" AUTOINCREMENT)
                    );
                    CREATE TABLE IF NOT EXISTS keywords (
                        Keywords_array_id INTEGER NOT NULL UNIQUE,
                        Keywords_array TEXT UNIQUE,
                        PRIMARY KEY("Keywords_array_id" AUTOINCREMENT)
                    )
                    """
            )
            
            rules = dumps(self.rules)
            keywords = dumps(self.keywords)
            
            string = self.multiplication(string)
            temp = (
                insert_into_tables("rules", "rule", rules),
                insert_into_tables("keywords", "Keywords_array", keywords),
                insert_into_tables("axioms", "axiom", string)
            )
            
            cursor.execute(
                    """
                    SELECT conclusion_id,
                    conclusions.rule_id,
                    conclusions.Keywords_array_id,
                    conclusions.axiom_id,
                    n_iter
                    FROM conclusions
                    JOIN rules, keywords, axioms
                    ON conclusions.rule_id = rules.rule_id AND
                    conclusions.Keywords_array_id = keywords.Keywords_array_id AND
                    conclusions.axiom_id = axioms.axiom_id
                    WHERE rule = ? AND
                    Keywords_array = ? AND
                    axiom = ? AND
                    n_iter = ?
                    """,
                    (rules, keywords, string, number_of_iterations)
            )
            
            result = cursor.fetchone()
            
            if not result:
                action_string = generate(string)
            else:
                cursor.execute('SELECT conclusion FROM conclusions WHERE conclusion_id = ?', [result[0]])
                action_string = tuple(map(tuple, loads(cursor.fetchone()[0])))
            
            return action_string
    
    @staticmethod
    def clear_database():
        """
        Clear the LSystem database.
        """
        with sql_connect("../Lsystem_outs.db") as connection:
            cursor = connection.cursor()
            cursor.executescript(
                    """
                    DROP TABLE IF EXISTS rules;
                    DROP TABLE IF EXISTS axioms;
                    DROP TABLE IF EXISTS conclusions;
                    DROP TABLE IF EXISTS keywords;
                    """
            )
    
    def formatting(self, string: str) -> Generator[tuple[str, int], None, None]:
        """
        Format the string by replacing keywords and adding quantity information.

        :param string: Input string.
        :return: Generator of tuples representing the formatted string.
        """
        if not isinstance(string, str):
            raise TypeError('argument "string" must be a string')
        for keywords in self.keywords:
            for keyword in keywords:
                string = string.replace(keyword, keywords[0])
            string = sub(
                    f"(?<! )(?P<keyword>{escape(keywords[0])})+",
                    lambda match: f" {match.group(1)}({len(match.group(0)) // len(keywords[0])})",
                    string
            )
        result = (
            (match.group('keyword'), int(match.group('quantity'))) for match in finditer(
                r"(?P<keyword>\S+)\((?P<quantity>\d+)\)",
                string, )
        )
        return result
    
    def multiplication(self, argument: str) -> str:
        """
        Perform multiplication of characters based on the keywords.

        :param argument: Input string.
        :return: Resulting string after multiplication.
        """
        for keywords in self.keywords:
            for keyword in keywords:
                argument = sub(
                        f"(?P<keyword>{escape(keyword)})" + r"\((?P<quantity>\d+)\)",
                        lambda match: match.group(1) * int(match.group(2)),
                        argument
                )
        argument = sub(
                r"(?P<keyword>.)\((?P<quantity>\d+)\)",
                lambda match: match.group(1) * int(match.group(2)),
                argument
        )
        return argument
    
    def __repr__(self):
        return f"{self.__class__.__module__}.{self.__class__.__name__}{self.rules, self.keywords}"
