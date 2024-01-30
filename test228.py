import time
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
    lsys = LSystem((("F", "FLFRRFLF"),), ["F", "B", "Mf", "Mb", 'R', 'L'])
    string = "F"
    string2 = "F"
    start = time.monotonic()
    for i in range(6):
        string2 = cpuboundfunctions.recurse_multiplier(string2, lsys.rules, i)  # type: ignore
    print(time.monotonic() - start)
    print(string2[:10])
    
    start = time.monotonic()
    for i in range(6):
        for _ in range(i):
            for key, value in lsys.rules:
                string = string.replace(key, value)
    print(time.monotonic() - start)
    print(string[:10])
    #act = tuple(lsys.formatting(act))  # type: ignore
    
    #start = time.monotonic()
    #res = cpuboundfunctions.generate_lines(  # type: ignore
    #        act,
    #        {
    #            "F": Actions.DrawForward,
    #            "B": Actions.DrawBack,
    #            "L": Actions.TurnLeft,
    #            "R": Actions.TurnRight
    #        },
    #        60
    #)
    #print(time.monotonic() - start)
    #print(array(res), len(res))
    #import turtle
    #
    #res = array(res)
    #res -= (500, 100, 500, 100)
    #res /= 10
    #tut = turtle.Turtle()
    #tut.speed(0)
    #tut.penup()
    #tut.goto(*res[0][0:2])
    #tut.pendown()
    #for *_, x, y in res[:10]:
    #    tut.goto(x, y)
    #turtle.mainloop()
