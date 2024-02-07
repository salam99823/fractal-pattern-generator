from enum import Enum
from math import cos, radians, sin
from typing import Iterable, Iterator, NamedTuple

from numpy import array


class MTurtleCommands(NamedTuple):
    DrawForward: str
    DrawBackward: str
    MoveForward: str
    MoveBackward: str
    TurnLeft: str
    TurnRight: str


class MTurtleActions(Enum):
    DrawForward: int = 0
    DrawBackward: int = 1
    MoveForward: int = 2
    MoveBackward: int = 3
    TurnLeft: int = 4
    TurnRight: int = 5


class MTurtlePoint(NamedTuple):
    x_coordinate: float
    y_coordinate: float


class Line(NamedTuple):
    point1: MTurtlePoint
    point2: MTurtlePoint
    
    @staticmethod
    def calculate_endpoint(
            _point1: MTurtlePoint,
            length: float,
            angle_of_rotation: float
    ) -> MTurtlePoint:
        return MTurtlePoint(
                _point1.x_coordinate + length * cos(radians(angle_of_rotation)),
                _point1.y_coordinate - length * sin(radians(angle_of_rotation)),
        )


class MTurtle:
    _turtle_commands: dict[str, MTurtleActions]
    position: MTurtlePoint
    rotation: float
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, _turtle_commands: MTurtleCommands = None):
        super().__init__()
        self.position: MTurtlePoint = MTurtlePoint(0, 0)
        self.rotation: float = 0
        if _turtle_commands is not None:
            self.turtle_commands = _turtle_commands
    
    def __call__(self, _turtle_actions: Iterable[tuple[str, int]]) -> Iterator[tuple[Line, str]]:
        for action, quantyti in _turtle_actions:
            action = self.turtle_commands.get(action)
            match action:
                case MTurtleActions.DrawForward:
                    yield self.draw_forward(quantyti)
                case MTurtleActions.DrawBackward:
                    yield self.draw_backward(quantyti)
                case MTurtleActions.MoveForward:
                    self.move_forward(quantyti)
                case MTurtleActions.MoveBackward:
                    self.move_backward(quantyti)
                case MTurtleActions.TurnLeft:
                    self.turn_left(quantyti)
                case MTurtleActions.TurnRight:
                    self.turn_right(quantyti)
    
    def __getattribute__(self, item):
        return self.__dict__.get(item)
    
    @property
    def turtle_commands(self) -> dict[str, int]:
        return self._turtle_commands
    
    @turtle_commands.setter
    def turtle_commands(self, _turtle_commands: dict[str, int]) -> None:
        self._turtle_commands = {}
        for key, action in zip(_turtle_commands, MTurtleActions):
            self._turtle_commands[key] = action
    
    def draw_forward(self, _length: float) -> tuple[Line, str]:
        _point1 = MTurtlePoint(self.position.x_coordinate, self.position.y_coordinate)
        _point2 = Line.calculate_endpoint(_point1, _length, self.rotation)
        self.position = _point2
        return Line(_point1, _point2), ""
    
    def draw_backward(self, _length: float) -> tuple[Line, str]:
        _point1 = MTurtlePoint(self.position.x_coordinate, self.position.y_coordinate)
        _point2 = Line.calculate_endpoint(_point1, -_length, self.rotation)
        self.position = _point2
        return Line(_point1, _point2), ""
    
    def move_forward(self, _length: float) -> None:
        self.position = Line.calculate_endpoint(self.position, _length, self.rotation)
    
    def move_backward(self, _length: float) -> None:
        self.position = Line.calculate_endpoint(self.position, -_length, self.rotation)
    
    def turn_left(self, _angle: float) -> None:
        self.rotation += _angle
    
    def turn_right(self, _angle: float) -> None:
        self.rotation -= _angle


if __name__ == '__main__':
    turtle = MTurtle(MTurtleCommands("F", "B", "f", "b", "L", "R"))
    some = turtle((("F", 1), ("B", 1)))
    for line, color in some:
        print(array(line), color, sep = "\n")
