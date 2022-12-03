#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")

elves_calories = []
calorie_sum = 0
for c in lines:
    if c == "":
        elves_calories.append(calorie_sum)
        calorie_sum = 0
        continue
    calorie_sum += int(c)


print(sum(sorted(elves_calories)[-3:]))
