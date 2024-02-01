import time
from numpy import array
from enum import StrEnum

import cpuboundfunctions

from Lsystems.Lsystem import LSystem


class Actions(StrEnum):
    DrawForward = "DrawForward"
    DrawBack = "DrawBack"
    MoveForward = "MoveForward"
    MoveBack = "MoveBack"
    TurnLeft = "TurnLeft"
    TurnRight = "TurnRight"


if __name__ == '__main__':
    lsys = LSystem((("F", "FLFRRFLF"),), ["F", "B", "Mf", "Mb", 'L', 'R'])
    num = 8
    
    string2: str = "F"
    string: str = "F"
    start = time.monotonic()
    
    string2 = tuple(lsys.formatting(cpuboundfunctions.multiply_recursively(string2, lsys.rules, num)))  # type: ignore
    
    print(
            array(
                    cpuboundfunctions.generate_lines(
                            string2,
                            {
                                "F": Actions.DrawForward,
                                "B": Actions.DrawBack,
                                "Mf": Actions.MoveForward,
                                "Mb": Actions.MoveBack,
                                "L": Actions.TurnLeft,
                                "R": Actions.TurnRight,
                            },
                            60
                    )
            )[0]
    )
    
    print(time.monotonic() - start)
    
    start = time.monotonic()
    string = lsys.generate_action_string(string, num)
    
    print(
            array(
                    cpuboundfunctions.generate_lines(  # type: ignore
                            string,
                            {
                                "F": Actions.DrawForward,
                                "B": Actions.DrawBack,
                                "Mf": Actions.MoveForward,
                                "Mb": Actions.MoveBack,
                                "L": Actions.TurnLeft,
                                "R": Actions.TurnRight,
                            },
                            60
                    )
            )[0]
    )
    
    print(time.monotonic() - start)
    
    print(string == string2)
