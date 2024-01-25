import time

from numpy import array

import lsystem2
from Lsystems.Lsystem import LSystem
from enum import StrEnum


class Actions(StrEnum):
    DrawForward = "DrawForward"
    DrawBack = "DrawBack"
    MoveForward = "MoveForward"
    MoveBack = "MoveBack"
    TurnLeft = "TurnLeft"
    TurnRight = "TurnRight"


if __name__ == '__main__':
    lsys = LSystem(("F->FLFRRFLF",), ["F", "B", "Mf", "Mb", 'R', 'L'])
    act = lsys.generate_action_string('FLLFLLF', 9)
    start = time.monotonic()
    res = lsystem2.generate_lines(
            act,
            {
                "F": Actions.DrawForward,
                "B": Actions.DrawBack,
                "L": Actions.TurnLeft,
                "R": Actions.TurnRight
            },
            60
    )
    print(time.monotonic() - start)
    print(array(res))
