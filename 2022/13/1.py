#!/usr/bin/env python
import sys
from itertools import zip_longest

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")


def compare(l, r):
    if l is None and r is not None:
        return True
    if r is None and l is not None:
        return False
    if type(l) == type(r) is int:
        if l < r:
            return True
        elif r == l:
            return None
        return False
    if type(l) == type(r) is list:
        for li, ri in zip_longest(l, r):
            c = compare(li, ri)
            if c:
                return True
            elif c is None:
                continue
            else:
                return False
        return None
    if type(l) is int:
        return compare([l], r)
    if type(r) is int:
        return compare(l, [r])


indices = []
for i in range(0, len(lines), 3):
    left = eval(lines[i])
    right = eval(lines[i + 1])
    if compare(left, right):
        indices.append(1 + (i // 3))
print(sum(indices))
