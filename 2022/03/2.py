#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")


def priority(item):
    if item.isupper():
        return ord(item) - 64 + 26
    return ord(item) - 96


priority_sum = 0
for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
    for c in l1:
        if c in l2 and c in l3:
            priority_sum += priority(c)
            break

print(priority_sum)
