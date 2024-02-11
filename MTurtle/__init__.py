from enum import Enum
from math import cos, radians, sin
from typing import Iterable, Iterator, NamedTuple


class MTurtleCommands(NamedTuple):
    DrawForward: str
    DrawBackward: str
    MoveForward: str
    MoveBackward: str
    TurnLeft: str
    TurnRight: str
    ChengeColor: str


class MTurtleActions(Enum):
    DrawForward: int = 0
    DrawBackward: int = 1
    MoveForward: int = 2
    MoveBackward: int = 3
    TurnLeft: int = 4
    TurnRight: int = 5
    ChengeColor: int = 6


class MTurtlePoint(NamedTuple):
    x: float
    y: float


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
                _point1.x + length * cos(radians(angle_of_rotation)),
                _point1.y - length * sin(radians(angle_of_rotation)),
        )


class MTurtle:
    _turtle_commands: dict[str, MTurtleActions]
    position: MTurtlePoint = MTurtlePoint(0, 0)
    rotation: float = 0
    
    def __init__(self, _turtle_commands: MTurtleCommands = None):
        super().__init__()
        if _turtle_commands is not None:
            self.turtle_commands = _turtle_commands
        else:
            self._turtle_commands = {}
    
    def execute(
            self,
            _turtle_actions: Iterable[tuple[str, int]],
            angle_of_rotation: float,
            line_lenght: float,
            move_distance: float
    ) -> Iterator[tuple[Line, int]]:
        color_index = 0
        for action, quantyti in _turtle_actions:
            action = self.turtle_commands.get(action)
            match action:
                case MTurtleActions.DrawForward:
                    yield self.draw_forward(quantyti * line_lenght), color_index
                case MTurtleActions.DrawBackward:
                    yield self.draw_backward(quantyti * line_lenght), color_index
                case MTurtleActions.MoveForward:
                    self.move_forward(quantyti * move_distance)
                case MTurtleActions.MoveBackward:
                    self.move_backward(quantyti * move_distance)
                case MTurtleActions.TurnLeft:
                    self.turn_left(quantyti * angle_of_rotation)
                case MTurtleActions.TurnRight:
                    self.turn_right(quantyti * angle_of_rotation)
                case MTurtleActions.ChengeColor:
                    color_index += 1
    
    @property
    def turtle_commands(self) -> dict[str, MTurtleActions]:
        return self._turtle_commands
    
    @turtle_commands.setter
    def turtle_commands(self, _turtle_commands: MTurtleCommands) -> None:
        self._turtle_commands = {}
        for key, action in zip(_turtle_commands, MTurtleActions):
            self._turtle_commands[key] = action
    
    def draw_forward(self, _length: float) -> Line:
        _point1 = MTurtlePoint(self.position.x, self.position.y)
        _point2 = Line.calculate_endpoint(_point1, _length, self.rotation)
        self.position = _point2
        return Line(_point1, _point2)
    
    def draw_backward(self, _length: float) -> Line:
        _point1 = MTurtlePoint(self.position.x, self.position.y)
        _point2 = Line.calculate_endpoint(_point1, -_length, self.rotation)
        self.position = _point2
        return Line(_point1, _point2)
    
    def move_forward(self, _length: float) -> None:
        self.position = Line.calculate_endpoint(self.position, _length, self.rotation)
    
    def move_backward(self, _length: float) -> None:
        self.position = Line.calculate_endpoint(self.position, -_length, self.rotation)
    
    def turn_left(self, _angle: float) -> None:
        self.rotation += _angle
    
    def turn_right(self, _angle: float) -> None:
        self.rotation -= _angle
    
    def reset(self):
        self.position = MTurtlePoint(0, 0)
        self.rotation = 0


if __name__ == '__main__':
    pass
