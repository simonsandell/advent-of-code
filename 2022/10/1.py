#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")


signal = [1]


def addx(x):
    noop()
    signal.append(signal[-1] + x)


def noop():
    signal.append(signal[-1])


for l in lines:
    if l == "noop":
        noop()
    else:
        addx(int(l.split(" ")[1]))


def signal_strength(n):
    return n * signal[n - 1]


print(
    signal_strength(20)
    + signal_strength(60)
    + signal_strength(100)
    + signal_strength(140)
    + signal_strength(180)
    + signal_strength(220)
)
print(
    signal_strength(20),
    signal_strength(60),
    signal_strength(100),
    signal_strength(140),
    signal_strength(180),
    signal_strength(220),
)
