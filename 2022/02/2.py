#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")

# A = Rock
# B = Paper
# C = Scissors

# X = Lose
# Y = Draw
# Z = Win

shape_score = {"A": 1, "B": 2, "C": 3}
win_score = {"X": 0, "Y": 3, "Z": 6}

determine_shape = {
    "X": {"A": "C", "B": "A", "C": "B"},
    "Y": {"A": "A", "B": "B", "C": "C"},
    "Z": {"A": "B", "B": "C", "C": "A"},
}


def determine_score(i, j):
    return shape_score[determine_shape[j][i]] + win_score[j]


total = 0
for l in lines:
    opponent, me = l.split(" ")
    total += determine_score(opponent, me)
print(total)
