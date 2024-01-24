import time

from numpy import array

import my_lib_rs
from Lsystems.Lsystem import LSystem

if __name__ == '__main__':
    lsys = LSystem(("F->FLFRRFLF",), ["F", "B", "Mf", "Mb", 'R', 'L'])
    act = lsys.generate_action_string('F', 9)
    start = time.monotonic()
    res = my_lib_rs.generate_lines(
            act,
            tuple('FBMfRL'),
            60
    )
    print(time.monotonic() - start)
    start = time.monotonic()
    print(array(res))
    print(time.monotonic() - start)
    #res /= 100
    #res -= 400
    #t = turtle.Turtle()
    #t.speed(0)
    #t.screen.tracer(1000)
    #for *_, x, y in res:
    #    t.goto(x, y)
    ##turtle.done()
