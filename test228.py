import math

import numpy

arr = numpy.arange(10, 260, 10)
side = int(math.sqrt(arr.size))
arr.shape = (side, side)
matr = []
pos = numpy.array((0, 0))
for g in range(math.ceil(arr.shape[0] / 2)):
    for i in arr:
        matr.append(i)
    for i in arr[-1][1:]:
        matr.append(i)
    for i in arr[::-1][1:]:
        matr.append(i[-1])
    for j in arr[0][::-1][1:][:-1]:
        print(j)
        matr.append(j)
print([10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70])
print(matr)
print(arr)
