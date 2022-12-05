#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):

# [N]     [Q]         [N]
# [R]     [F] [Q]     [G] [M]
# [J]     [Z] [T]     [R] [H] [J]
# [T] [H] [G] [R]     [B] [N] [T]
# [Z] [J] [J] [G] [F] [Z] [S] [M]
# [B] [N] [N] [N] [Q] [W] [L] [Q] [S]
# [D] [S] [R] [V] [T] [C] [C] [N] [G]
# [F] [R] [C] [F] [L] [Q] [F] [D] [P]
#  1   2   3   4   5   6   7   8   9

with open(infile) as f:
    lines = f.read().strip().split("\n")

piles = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
for l in lines[7::-1]:
    for i, c in enumerate(l[1::4]):
        if c != " ":
            piles[i + 1].append(c)

for l in lines[10:]:
    instruction = l.split(" ")
    num_move = int(instruction[1])
    from_pile = int(instruction[3])
    to_pile = int(instruction[5])

    to_move = reversed(piles[from_pile][-num_move:])
    piles[from_pile] = piles[from_pile][:-num_move]
    piles[to_pile].extend(to_move)

tops = ""
for i in range(1, 10):
    tops += piles[i][-1]
print(tops)
