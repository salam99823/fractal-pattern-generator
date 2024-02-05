"""
in this file I am testing some functions
"""
from numpy import array

from cpuboundfunctions import *
from Lsystems.Lsystem import LSystem

if __name__ == '__main__':
    lsys = LSystem((("F", "CFLFRRFLF"),), ["F", "B", ("f",), ("b",), 'L', 'R', "C"])
    
    string = lsys.generate_action_string("F", 2)
    
    lines, colors = generate_lines(
            string,
            {
                "F": "DrawForward",
                "B": "DrawBack",
                "f": "MoveForward",
                "b": "MoveBack",
                "R": "TurnRight",
                "L": "TurnLeft",
                "C": "ChangePenColor",
            },
            60
    )
    print(array(lines), array(colors))
