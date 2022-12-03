#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")

# A = X = Rock
# B = Y = Paper
# C = Z = Scissors
shape_score = {"X": 1, "Y": 2, "Z": 3}
win_score = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}


def determine_score(i, j):
    return shape_score[j] + win_score[i][j]


total = 0
for l in lines:
    opponent, me = l.split(" ")
    total += determine_score(opponent, me)
print(total)
