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


def print_grid(rope, visited):
    grid = [["." for _ in range(100)] for _ in range(100)]
    grid[50][50] = "s"
    for v in visited:
        grid[50 + v[0]][50 + v[1]] = "#"
    for i, r in enumerate(rope):
        grid[50 + r[0]][50 + r[1]] = str(i)
    for l in grid:
        print("".join(l))


def adjust_t(t_pos, h_pos):
    x_dist = abs(t_pos[0] - h_pos[0])
    y_dist = abs(t_pos[1] - h_pos[1])
    if x_dist + y_dist < 2:
        return t_pos
    if x_dist + y_dist == 2 and x_dist != 0 and y_dist != 0:
        return t_pos
    n_pos = [None, None]
    if h_pos[0] - t_pos[0] >= 2:
        n_pos[0] = h_pos[0] - 1
        n_pos[1] = h_pos[1]
    elif h_pos[0] - t_pos[0] <= -2:
        n_pos[0] = h_pos[0] + 1
        n_pos[1] = h_pos[1]
    elif h_pos[1] - t_pos[1] >= 2:
        n_pos[1] = h_pos[1] - 1
        n_pos[0] = h_pos[0]
    elif h_pos[1] - t_pos[1] <= -2:
        n_pos[1] = h_pos[1] + 1
        n_pos[0] = h_pos[0]
    assert n_pos != [None, None], (t_pos, h_pos)
    return n_pos


rope = []
for _ in range(10):
    rope.append([0, 0])


def adjust_rope(rope):
    for j in range(1, 10):
        rope[j] = adjust_t(rope[j], rope[j - 1])


for l in lines:
    to, dist = l.split(" ")
    print(to, dist)
    print_grid(rope, visited)
    if to == "L":
        for i in range(int(dist)):
            rope[0][0] -= 1
            adjust_rope(rope)
            visited.add(tuple(rope[-1]))
    elif to == "R":
        for i in range(int(dist)):
            rope[0][0] += 1
            adjust_rope(rope)
            visited.add(tuple(rope[-1]))
    if to == "U":
        for i in range(int(dist)):
            rope[0][1] -= 1
            adjust_rope(rope)
            visited.add(tuple(rope[-1]))
    elif to == "D":
        for i in range(int(dist)):
            rope[0][1] += 1
            adjust_rope(rope)
            visited.add(tuple(rope[-1]))
    input()

print(len(visited))
