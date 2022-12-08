#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")

max_x = len(lines) - 1
max_y = len(lines[0]) - 1


def count_visible_left(x, y):
    at_x = x
    at_y = y
    base_h = int(lines[x][y])
    count = 0
    while at_x > 0:
        count += 1
        at_x -= 1
        h = int(lines[at_x][at_y])
        if h >= base_h:
            break
    return count


def count_visible_right(x, y):
    at_x = x
    at_y = y
    base_h = int(lines[x][y])
    count = 0
    while at_x < max_x:
        count += 1
        at_x += 1
        h = int(lines[at_x][at_y])
        if h >= base_h:
            break
    return count


def count_visible_top(x, y):
    at_x = x
    at_y = y
    base_h = int(lines[x][y])
    count = 0
    while at_y > 0:
        count += 1
        at_y -= 1
        h = int(lines[at_x][at_y])
        if h >= base_h:
            break
    return count


def count_visible_bottom(x, y):
    at_x = x
    at_y = y
    base_h = int(lines[x][y])
    count = 0
    while at_y < max_y:
        count += 1
        at_y += 1
        h = int(lines[at_x][at_y])
        if h >= base_h:
            break
    return count


max_score = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        score = (
            count_visible_left(i, j)
            * count_visible_right(i, j)
            * count_visible_top(i, j)
            * count_visible_bottom(i, j)
        )
        if score > max_score:
            max_score = score
print(max_score)
