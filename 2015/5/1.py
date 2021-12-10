from functools import reduce
from operator import add

with open("input") as f:
    lines = f.read().strip().split("\n")


def count_vowels(string):
    return (
        string.count("a")
        + string.count("e")
        + string.count("i")
        + string.count("o")
        + string.count("u")
    )


banned = ("ab", "cd", "pq", "xy")


def is_nice(string):
    for b in banned:
        if b in string:
            return False
    for c, cc in zip(string[:-1], string[1:]):
        if c == cc:
            break
    else:
        return False
    if count_vowels(string) < 3:
        return False
    return True


print(reduce(add, map(is_nice, lines)))
