#!/usr/bin/env python
import sys
import numpy as np

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

with open(infile) as f:
    lines = f.read().strip().split("\n")
width = len(lines[0])
height = len(lines)
arr = np.zeros((width, height))
for y, l in enumerate(lines):
    arr[:, y] = [int(x) for x in l]


def get_adjacent(k):
    neighbours = {
        (k[0] + 1, k[1]),
        (k[0] - 1, k[1]),
        (k[0], k[1] + 1),
        (k[0], k[1] - 1),
    }
    if k[0] == 0:
        neighbours.remove((k[0] - 1, k[1]))
    if k[0] + 1 == width:
        neighbours.remove((k[0] + 1, k[1]))
    if k[1] == 0:
        neighbours.remove((k[0], k[1] - 1))
    if k[1] + 1 == height:
        neighbours.remove((k[0], k[1] + 1))
    return neighbours


neighbours = dict()
for x in range(width):
    for y in range(height):
        neighbours[(x, y)] = get_adjacent((x, y))


graph = {(0, 0): 0}
visited = set()
unvisited = {(0, 0)}
while True:
    mv = 10e10
    mk = None
    for k in unvisited:
        if graph[k] < mv:
            mv = graph[k]
            mk = k
    visited.add(mk)
    unvisited.remove(mk)
    if mk == (width - 1, height - 1):
        break
    for n in neighbours[mk]:
        if n not in visited:
            unvisited.add(n)
        if n not in graph:
            graph[n] = arr[n] + mv
        else:
            if arr[n] + mv < graph[n]:
                graph[n] = arr[n] + mv
print(int(graph[(width - 1, height - 1)]))
