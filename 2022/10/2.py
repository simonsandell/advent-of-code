#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")


screen = [["." for _ in range(40)] for _ in range(6)]
signal = [1]


def draw():
    xpos = (len(signal) - 1) % 40
    ypos = (len(signal) - 1) // 40
    if abs(signal[-1] - xpos) < 2:
        screen[ypos][xpos] = "#"


def addx(x):
    noop()
    signal.append(signal[-1] + x)
    draw()


def noop():
    signal.append(signal[-1])
    draw()


for l in lines:
    if l == "noop":
        noop()
    else:
        addx(int(l.split(" ")[1]))

s = ""
for r in screen:
    for c in r:
        s += c
    s += "\n"
print(s)
