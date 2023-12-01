#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")

translate = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def preprocess(l):
    for k, v in translate.items():
        if k in l:
            l = l[: l.index(k)] + k + v + l[l.index(k) :]
            l = l[: l.rindex(k)] + k + v + l[l.rindex(k) :]
    return l


s = 0
for rl in lines:
    l = preprocess(rl)
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
