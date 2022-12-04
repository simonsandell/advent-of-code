#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")


def parse(l):
    r1, r2 = l.split(",")
    r1 = r1.split("-")
    r2 = r2.split("-")
    r1 = [int(x) for x in r1]
    r2 = [int(x) for x in r2]
    return [r1, r2]


def check_contains(r1, r2):
    if r2[0] <= r1[1] and r2[0] >= r1[0] and r2[1] <= r1[1] and r2[1] >= r1[0]:
        return True
    return False


completely_overlapping = 0
for l in lines:
    ranges = parse(l)
    if check_contains(ranges[0], ranges[1]) or check_contains(ranges[1], ranges[0]):
        completely_overlapping += 1
print(completely_overlapping)
