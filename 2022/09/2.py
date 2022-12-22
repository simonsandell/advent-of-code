#!/usr/bin/env python
import sys
from copy import deepcopy

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")

start_pos = [0, 0]
visited = set()
visited.add(tuple(start_pos))


def print_grid(rope, visited):
    max_n = 20 + int(1.5 * max(map(lambda x: abs(x[0]) + abs(x[1]), visited)))
    grid = [["." for _ in range(max_n)] for _ in range(max_n)]
    grid[max_n // 2][max_n // 2] = "s"
    for v in visited:
        grid[max_n // 2 + v[1]][max_n // 2 + v[0]] = "#"
    for i, r in enumerate(rope):
        grid[max_n // 2 + r[1]][max_n // 2 + r[0]] = str(i)
    for l in grid:
        print("".join(l))


def check_adjacent(x, y):
    x_dist = abs(x[0] - y[0])
    y_dist = abs(x[1] - y[1])
    if x_dist + y_dist < 2:
        return True
    elif x_dist + y_dist == 2 and x_dist != 0 and y_dist != 0:
        return True
    return False


def adjust_t(t_pos, h_pos):
    x_dist = abs(t_pos[0] - h_pos[0])
    y_dist = abs(t_pos[1] - h_pos[1])
    n_pos = deepcopy(t_pos)
    visited = {tuple(n_pos)}
    if check_adjacent(n_pos, h_pos):
        return n_pos, visited
    if x_dist == 0:
        while not check_adjacent(n_pos, h_pos):
            if n_pos[1] < h_pos[1]:
                n_pos[1] = n_pos[1] + 1
            else:
                n_pos[1] = n_pos[1] - 1
            visited.add(tuple(n_pos))
        return n_pos, visited
    if y_dist == 0:
        while not check_adjacent(n_pos, h_pos):
            if n_pos[0] < h_pos[0]:
                n_pos[0] = n_pos[0] + 1
            else:
                n_pos[0] = n_pos[0] - 1
            visited.add(tuple(n_pos))
        return n_pos, visited
    while not check_adjacent(n_pos, h_pos):
        if n_pos[0] < h_pos[0]:
            n_pos[0] = n_pos[0] + 1
        else:
            n_pos[0] = n_pos[0] - 1
        if n_pos[1] < h_pos[1]:
            n_pos[1] = n_pos[1] + 1
        else:
            n_pos[1] = n_pos[1] - 1
        visited.add(tuple(n_pos))
    return n_pos, visited


rope = []
for _ in range(10):
    rope.append([0, 0])


def adjust_rope(rope):
    for j in range(1, 10):
        rope[j], visited = adjust_t(rope[j], rope[j - 1])
    return visited


for l in lines:
    to, dist = l.split(" ")
    print(f"== {to} {dist} ==")
    for i in range(int(dist)):
        if to == "L":
            rope[0][0] -= 1
        elif to == "R":
            rope[0][0] += 1
        if to == "U":
            rope[0][1] -= 1
        elif to == "D":
            rope[0][1] += 1
        new_visited = adjust_rope(rope)
        visited = visited.union(new_visited)
        # print_grid(rope, visited)
        # print()
    # input()

print(len(visited))
