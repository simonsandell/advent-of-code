from functools import reduce
from operator import mul, add

with open("input") as f:
    lines = f.read().strip().split("\n")


def get_area(line):
    l, w, h = (int(x) for x in line.split("x"))
    area = 2 * l * w + 2 * w * h + 2 * h * l
    slack = reduce(mul, sorted((l, w, h))[:2])
    return area + slack


print(reduce(add, map(get_area, lines)))
