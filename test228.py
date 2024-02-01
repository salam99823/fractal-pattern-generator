import time

from cpuboundfunctions import *

from Lsystems.Lsystem import LSystem

if __name__ == '__main__':
    lsys = LSystem((("F", "FLFRRFLF"),), ["F", "B", "Mf", "Mb", 'L', 'R'])
    num = 1
    
    start = time.monotonic()
    
    string2 = tuple(lsys.formatting(multiply_recursively("F", lsys.rules, num)))
    
    print(time.monotonic() - start)
    print(
            generate_lines(
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
            [:4]
    )
    
    start = time.monotonic()
    string = lsys.generate_action_string("F", num)
    
    print(time.monotonic() - start)
    print(
            generate_lines(
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
            [:4]
    )
    
    print(string == string2)
