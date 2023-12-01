#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")

s = 0
for l in lines:
    calibration_value = ""
    for c in l:
        if c.isnumeric():
            calibration_value += c
            break
    for c in reversed(l):
        if c.isnumeric():
            calibration_value += c
            break
    s += int(calibration_value)
print(s)
