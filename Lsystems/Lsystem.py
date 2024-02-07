"""
An L-System is a set of rules that can be used to generate a fractal pattern from a string.
The L-System is defined by a set of rules, which are a set of pairs of strings that represent
substitution rules. The L-System also has a set of "keywords", which are strings that are used
to represent variables in the L-System.

The L-System can be used to generate a fractal pattern by starting with a string, applying the
rules repeatedly, and then using the keywords to represent the variables in the pattern.

This class provides methods for defining the rules and keywords of an L-System, as well as
methods for generating the action string based on the L-System.
"""
from re import escape, finditer, sub
from typing import Iterable, Iterator, Sequence


class LSystem(object):
    """
    Initialize a new L-System.

    :param rules: The rules of the L-System.
    :param keywords: The keywords of the L-System.
    """
    __rules: tuple[tuple[str, str], ...] = ()
    __keywords: tuple[tuple[str, ...], ...] = ()
    
    def __init__(
            self,
            rules: Iterable[tuple[str, str]] | None = None,
            keywords: Iterable[Iterable[str]] | None = None,
    ):
        """
        Initialize a new L-System.

        :param rules: The rules of the L-System.
        :param keywords: The keywords of the L-System.
        """
        if keywords is not None:
            self.keywords = keywords
        if rules is not None:
            self.rules = rules
    
    @property
    def rules(self) -> tuple[tuple[str, str], ...]:
        """
        Get the rules of the L-System.

        :return: The rules of the L-System.
        """
        return self.__rules
    
    @rules.setter
    def rules(self, rules: Iterable[tuple[str, str]]) -> None:
        """
        Set the rules of the L-System.

        :param rules: The rules of the L-System.
        """
        if not isinstance(rules, Iterable) or not all(
                isinstance(_key, str) and isinstance(_value, str) for _key, _value in rules
        ):
            raise TypeError("Invalid type for rules. Must be an iterable of tuples of strings.")
        for _key, _value in rules:
            self.__rules += ((self.multiplication(_key), self.multiplication(_value)),)
    
    @property
    def keywords(self) -> tuple[tuple[str, ...], ...]:
        """
        Get the keywords of the L-System.

        :return: The keywords of the L-System.
        """
        return self.__keywords
    
    @keywords.setter
    def keywords(self, keywords: Iterable[Sequence[str]]) -> None:
        """
        Set the keywords of the L-System.

        :param keywords: The keywords of the L-System.
        """
        if not isinstance(keywords, Iterable) or not all(
                isinstance(keyword, Iterable) and (isinstance(_, str) for _ in keyword) for keyword in keywords
        ):
            raise TypeError("Invalid type for keywords. Must be an iterable of iterables of strings.")
        self.__keywords = tuple(tuple(sorted(keyword, key = len)) for keyword in keywords)
    
    def use_rules(
            self,
            string: str,
            number_of_iterations: int,
    ) -> str:
        """
        Generate the action string based on the L-System.

        :param string: The starting string.
        :param number_of_iterations: The number of iterations to perform.
        :return: The action string.
        """
        for _ in range(number_of_iterations):
            for _key, _value in self.rules:
                string = string.replace(_key, _value)
        return string
    
    def formatting(self, string: str) -> Iterator[tuple[str, int]]:
        """
        Format the string by replacing keywords and adding quantity information.

        :param string: The input string.
        :return: An iterator of tuples containing the formatted string and its quantity.
        """
        if not isinstance(string, str):
            raise TypeError("argument 'string' must be a string")
        for keywords in self.keywords:
            for keyword in keywords[1:]:
                string = string.replace(keyword, keywords[0])
            string = sub(
                    f"(?<! )(?P<keyword>{escape(keywords[0])})+",
                    lambda match: f" {match.group(1)}({len(match.group(0)) // len(keywords[0])})",
                    string,
            )
        result = (
            (match.group("keyword"), int(match.group("quantity")))
            for match in finditer(
                r"(?P<keyword>\S+)\((?P<quantity>\d+)\)",
                string, )
        )
        return result
    
    def multiplication(self, argument: str) -> str:
        """
        Perform multiplication of characters based on the keywords.

        :param argument: The input string.
        :return: The resulting string after multiplication.
        """
        for keywords in self.keywords:
            for keyword in keywords:
                argument = sub(
                        f"(?P<keyword>{escape(keyword)})" + r"\((?P<quantity>\d+)\)",
                        lambda match: match.group(1) * int(match.group(2)),
                        argument,
                )
        argument = sub(
                r"(?P<keyword>.)\((?P<quantity>\d+)\)",
                lambda match: match.group(1) * int(match.group(2)),
                argument,
        )
        return argument
    
    def __repr__(self):
        return f"{self.__class__.__module__}.{self.__class__.__name__}{self.rules, self.keywords}"
