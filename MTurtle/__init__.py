from enum import Enum
from typing import Iterable, Iterator, NamedTuple

from MTurtle._BaseMTurtle import BaseMTurtle, Line, MTurtlePoint


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


class MTurtle(BaseMTurtle):
    _turtle_commands: dict[str, MTurtleActions] = {}
    
    def __init__(self, _turtle_commands: MTurtleCommands = None):
        super().__init__()
        if _turtle_commands is not None:
            self.turtle_commands = _turtle_commands
    
    def __call__(
            self,
            _turtle_actions: Iterable[tuple[str, int]],
            _length: float,
            _angle_of_turn: float
    ) -> Iterator[tuple[Line, str]]:
        for action, quantyti in _turtle_actions:
            match self.turtle_commands.get(action):
                case MTurtleActions.DrawForward:
                    yield self.draw_forward(quantyti * _length)
                case MTurtleActions.DrawBackward:
                    yield self.draw_backward(quantyti * _length)
                case MTurtleActions.MoveForward:
                    self.move_forward(quantyti * _length)
                case MTurtleActions.MoveBackward:
                    self.move_backward(quantyti * _length)
                case MTurtleActions.TurnLeft:
                    self.turn_left(quantyti * _angle_of_turn)
                case MTurtleActions.TurnRight:
                    self.turn_right(quantyti * _angle_of_turn)
    
    @property
    def turtle_commands(self) -> dict[str, MTurtleActions]:
        return self._turtle_commands
    
    @turtle_commands.setter
    def turtle_commands(
            self,
            _turtle_commands: MTurtleCommands
    ) -> None:
        if not isinstance(_turtle_commands, MTurtleCommands):
            raise TypeError("turtle_commands must be an instance of MTurtleCommands")
        self._turtle_commands = {}
        for key, action in zip(_turtle_commands, MTurtleActions):
            self._turtle_commands[key] = action


def main():
    pass


if __name__ == '__main__':
    main()
