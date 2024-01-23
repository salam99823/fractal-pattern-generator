import math
import sys

import numpy

arr = numpy.arange(10, 260, 10)
side = int(math.sqrt(arr.size))
arr.shape = (side, side)
actual = []
pos = numpy.array((0, 0))
for j in range(math.ceil(arr.shape[0] / 2) + 1):
    print(j)
    for i in arr[j:-j - 1]:
        actual.append(i[j])
    for i in arr[-j - 1][j:-j - 1]:
        actual.append(i)
    for i in arr[::-1][j:-j - 1]:
        actual.append(i[-j - 1])
    for i in arr[j][::-1][j:-j - 1]:
        actual.append(i)
expected = numpy.array(
        (10, 60, 110, 160,
         210, 220, 230, 240,
         250, 200, 150, 100, 50,
         40, 30, 20, 70,
         120, 170, 180, 190,
         140, 90, 80,)
)
actual = numpy.array(actual)
if not all(expected == actual):
    file = sys.stderr
else:
    file = sys.stdout
print(f"{actual}\n{expected}\n{arr}", )
