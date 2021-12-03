from itertools import combinations
from copy import deepcopy
import numpy as np

with open("input") as f:
    inp = f.read()


def parse_input(arr, inp):
    for y, i in enumerate(inp.strip().split("\n")):
        for x, c in enumerate(i):
            if c == "#":
                arr[nrounds + x, nrounds + y, nrounds, nrounds] = 1
            else:
                arr[nrounds + x, nrounds + y, nrounds, nrounds] = 0
    return arr


nrounds = 6
x = 10 + 2 * nrounds
y = 10 + 2 * nrounds
z = 1 + 2 * nrounds
w = 1 + 2 * nrounds
space = np.zeros((x, y, z, w))

space = parse_input(space, inp)

neighbour_lookup = {}


def get_neighbours(pos):
    global neighbour_lookup
    if pos not in neighbour_lookup:
        operations = {
            lambda a: (a[0] + 1, a[1], a[2], a[3]),
            lambda a: (a[0] - 1, a[1], a[2], a[3]),
            lambda a: (a[0], a[1] + 1, a[2], a[3]),
            lambda a: (a[0], a[1] - 1, a[2], a[3]),
            lambda a: (a[0], a[1], a[2] + 1, a[3]),
            lambda a: (a[0], a[1], a[2] - 1, a[3]),
            lambda a: (a[0], a[1], a[2], a[3] + 1),
            lambda a: (a[0], a[1], a[2], a[3] - 1),
        }
        res = set()
        for i in range(1, 5):
            for c in combinations(operations, i):
                neigh = deepcopy(pos)
                for op in c:
                    neigh = op(neigh)
                res.add(neigh)
        res.discard(pos)
        neighbour_lookup[pos] = res
    return neighbour_lookup[pos]


def count_active_neighbours(arr, pos):
    neighbours = get_neighbours(pos)
    s = 0
    for n in neighbours:
        try:
            s += arr[n[0], n[1], n[2], n[3]]
        except IndexError:
            pass
    return s


def step(arr):
    new = arr.copy()
    shape = arr.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                for l in range(shape[3]):
                    c = count_active_neighbours(arr, (i, j, k, l))
                    if arr[i, j, k, l] == 1 and c not in {2, 3}:
                        new[i, j, k, l] = 0
                    elif arr[i, j, k, l] == 0 and c == 3:
                        new[i, j, k, l] = 1
    return new


print(space.sum().sum().sum().sum())
for i in range(6):
    space = step(space)
    print(space.sum().sum().sum().sum())
