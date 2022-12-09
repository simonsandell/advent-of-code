#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")

start_pos = [0, 0]
visited = set()
visited.add(tuple(start_pos))

t_pos = [0, 0]
h_pos = [0, 0]


def adjust_t(t_pos, h_pos):
    x_dist = abs(t_pos[0] - h_pos[0])
    y_dist = abs(t_pos[1] - h_pos[1])
    if x_dist + y_dist < 2:
        return t_pos
    if x_dist + y_dist == 2 and x_dist != 0 and y_dist != 0:
        return t_pos
    n_pos = [None, None]
    if h_pos[0] - t_pos[0] == 2:
        n_pos[0] = h_pos[0] - 1
        n_pos[1] = h_pos[1]
    elif h_pos[0] - t_pos[0] == -2:
        n_pos[0] = h_pos[0] + 1
        n_pos[1] = h_pos[1]
    elif h_pos[1] - t_pos[1] == 2:
        n_pos[1] = h_pos[1] - 1
        n_pos[0] = h_pos[0]
    elif h_pos[1] - t_pos[1] == -2:
        n_pos[1] = h_pos[1] + 1
        n_pos[0] = h_pos[0]
    assert n_pos != [None, None], (t_pos, h_pos)
    return n_pos


for l in lines:
    to, dist = l.split(" ")
    if to == "L":
        for i in range(int(dist)):
            h_pos[0] -= 1
            t_pos = adjust_t(t_pos, h_pos)
            visited.add(tuple(t_pos))
    elif to == "R":
        for i in range(int(dist)):
            h_pos[0] += 1
            t_pos = adjust_t(t_pos, h_pos)
            visited.add(tuple(t_pos))
    if to == "U":
        for i in range(int(dist)):
            h_pos[1] -= 1
            t_pos = adjust_t(t_pos, h_pos)
            visited.add(tuple(t_pos))
    elif to == "D":
        for i in range(int(dist)):
            h_pos[1] += 1
            t_pos = adjust_t(t_pos, h_pos)
            visited.add(tuple(t_pos))
print(len(visited))
