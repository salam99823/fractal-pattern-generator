import time
from enum import StrEnum

from numpy import array

import my_lib_rs
from Lsystems.Lsystem import LSystem


class Actions(StrEnum):
    DrawForward = "DrawForward"
    DrawBack = "DrawBack"
    MoveForward = "MoveForward"
    MoveBack = "MoveBack"
    TurnLeft = "TurnLeft"
    TurnRight = "TurnRight"


if __name__ == '__main__':
    lsys = LSystem(("F->FLFRRFLF",), ["F", "B", "Mf", "Mb", 'R', 'L'])
    act = lsys.generate_action_string('FLLFLLF', 4)
    print()
    start = time.monotonic()
    res = my_lib_rs.generate_lines(
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
    start = time.monotonic()
    res = array(res)
    print(res)
    res /= 10
    res -= (500, 300, 500, 300)
    print(time.monotonic() - start)
    
    import turtle
    
    t = turtle.Turtle()
    t.up()
    t.goto(*res[0][0:2])
    t.down()
    t.getscreen().tracer(1)
    """for *_, x, y in res:
        t.goto(x, y)"""
    turtle.exitonclick()
