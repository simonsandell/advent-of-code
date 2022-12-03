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
for l in lines:
    first, last = l[: len(l) // 2], l[len(l) // 2 :]
    for c in first:
        if c in last:
            priority_sum += priority(c)
            break
print(priority_sum)
