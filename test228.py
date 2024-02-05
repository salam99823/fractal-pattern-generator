"""
in this file I am testing some functions
"""

from cpuboundfunctions import *
from cpuboundfunctions.TurtleActions import TurtleActions
from numpy import array

from Lsystems.Lsystem import LSystem

if __name__ == '__main__':
    lsys = LSystem((("F", "CFLFRRFLF"),), ("F", "B", ("f",), ("b",), 'L', 'R', "C"))
    
    string = lsys.generate_action_string("F", 1)
    
    lines, colors = generate_lines(
            (i for i in string),
            {
                "F": TurtleActions.DrawBack,
                "B": TurtleActions.DrawBack,
                "f": TurtleActions.MoveForward,
                "b": TurtleActions.MoveBack,
                "R": TurtleActions.TurnRight,
                "L": TurtleActions.TurnLeft,
                "C": TurtleActions.ChangePenColor,
            },
            60,
            4
    )
    print(array(lines), "\n", array(colors))
