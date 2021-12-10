from functools import reduce
from operator import add

with open("input") as f:
    lines = f.read().strip().split("\n")


def is_nice(string):
    for i, (c, cc) in enumerate(zip(string[:-1], string[1:])):
        s = c + cc
        p1, p2 = string[:i], string[i + 2 :]
        if s in p1:
            break
        if s in p2:
            break
    else:
        return False

    for c, cc in zip(string[:-2], string[2:]):
        if c == cc:
            break
    else:
        return False
    return True


print(reduce(add, map(is_nice, lines)))
