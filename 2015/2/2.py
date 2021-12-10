from functools import reduce
from operator import mul, add

with open("input") as f:
    lines = f.read().strip().split("\n")


def get_length(line):
    l, w, h = (int(x) for x in line.split("x"))
    ribbon = reduce(add, map(lambda x: x * 2, sorted((l, w, h))[:2]))
    bow = l * w * h
    return ribbon + bow


print(reduce(add, map(get_length, lines)))
