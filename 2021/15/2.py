#!/usr/bin/env python
import sys
import numpy as np
import heapq

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

with open(infile) as f:
    lines = f.read().strip().split("\n")
orig_width = len(lines[0])
orig_height = len(lines)
width = 5 * orig_width
height = 5 * orig_height
arr = np.zeros((width, height))
for y, l in enumerate(lines):
    arr[: len(lines[0]), y] = [int(x) for x in l]


def mod(v):
    if v > 9:
        return v % 9
    return v


for y in range(height):
    for x in range(width):
        arr[x, y] = mod(
            arr[x % orig_width, y % orig_height]
            + (x // orig_width)
            + (y // orig_height)
        )


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
unvisited = [(0, (0, 0))]
while unvisited:
    _, mk = heapq.heappop(unvisited)
    if mk == (width - 1, height - 1):
        break
    for n in neighbours[mk]:
        cost = graph[mk] + arr[n]
        if n not in graph or cost < graph[n]:
            heapq.heappush(unvisited, (cost, n))
            graph[n] = cost
print(int(graph[(width - 1, height - 1)]))
