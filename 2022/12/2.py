#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")

start_pos = None
end_pos = set()
grid = []
for y, l in enumerate(lines):
    row = []
    for x, c in enumerate(l):
        if c == "S":
            row.append("a")
            end_pos.add((x, y))
        elif c == "E":
            start_pos = (x, y)
            row.append("z")
        elif c == "a":
            row.append(c)
            end_pos.add((x, y))
        else:
            row.append(c)
    grid.append(row)


def get_neighbours(x, y):
    elev = ord(grid[y][x])
    candidates = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    neighbours = []
    for p in candidates:
        if p[0] < 0 or p[1] < 0:
            continue
        try:
            target_elev = ord(grid[p[1]][p[0]])
            if target_elev - elev < -1:
                continue
            neighbours.append(p)
        except IndexError:
            continue
    return neighbours


class Node:
    def __init__(self, x, y, neighbours):
        self.pos = (x, y)
        self.neighbours = neighbours
        self.distance = 99999999

    def __repr__(self):
        return str(self.distance)


nodes = []
unvisited = set()
for y, l in enumerate(lines):
    row = []
    for x, c in enumerate(l):
        unvisited.add((x, y))
        row.append(Node(x, y, get_neighbours(x, y)))
    nodes.append(row)

start_node = nodes[start_pos[1]][start_pos[0]]
start_node.distance = 0
unvisited.remove(start_node.pos)
queue = [start_node]
while queue:
    n = queue.pop()
    if n.pos in end_pos:
        print(n.distance)
        break
    for npos in n.neighbours:
        neighbour = nodes[npos[1]][npos[0]]
        if neighbour.pos in unvisited:
            unvisited.remove(neighbour.pos)
            neighbour.distance = n.distance + 1
            queue.insert(0, neighbour)
