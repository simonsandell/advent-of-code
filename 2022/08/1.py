#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")

from_left = [l for l in lines]
from_right = [l[::-1] for l in lines]


def transpose(lines):
    transposed_lines = ["" for _ in lines]
    for l in lines:
        for i, c in enumerate(l):
            transposed_lines[i] += c
    return transposed_lines


transposed_lines = transpose(lines)
from_top = [l for l in transposed_lines]
from_bottom = [l[::-1] for l in transposed_lines]


def get_visible(tree_line):
    current_max = -1
    visible = ""
    for i, c in enumerate(tree_line):
        h = int(c)
        if h > current_max:
            visible += "1"
            current_max = h
        else:
            visible += "0"
    return visible


visible_left = []
visible_right = []
for l in from_left:
    visible_left.append(get_visible(l))
for l in from_right:
    visible_right.append(get_visible(l)[::-1])

visible_top = []
visible_bottom = []
for l in from_top:
    visible_top.append(get_visible(l))
for l in from_bottom:
    visible_bottom.append(get_visible(l)[::-1])
visible_top = transpose(visible_top)
visible_bottom = transpose(visible_bottom)


def or_str(str1, str2):
    r = ""
    for i in range(len(str1)):
        if str1[i] == "1" or str2[i] == "1":
            r += "1"
        else:
            r += "0"
    return r


count = 0
for i in range(len(lines)):
    count += or_str(
        visible_left[i],
        or_str(visible_right[i], or_str(visible_top[i], visible_bottom[i])),
    ).count("1")
print(count)
