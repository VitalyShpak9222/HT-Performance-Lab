import sys
from decimal import Decimal

ellipse_file = sys.argv[1]
points_file = sys.argv[2]

with open(ellipse_file) as file:
    x0, y0 = map(Decimal, file.readline().split())
    a, b = map(Decimal, file.readline().split())

a2 = a * a
b2 = b * b
border = a2 * b2

with open(points_file) as file:
    for line in file:
        x, y = map(Decimal, line.split())

        dx = x - x0
        dy = y - y0
        value = dx * dx * b2 + dy * dy * a2

        if value < border:
            print(1)
        elif value > border:
            print(2)
        else:
            print(0)