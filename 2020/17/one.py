import numpy as np

with open("input") as f:
    inp = f.read()


def parse_input(arr, inp):
    for y, i in enumerate(inp.strip().split("\n")):
        for x, c in enumerate(i):
            if c == "#":
                arr[nrounds + x, nrounds + y, nrounds] = 1
            else:
                arr[nrounds + x, nrounds + y, nrounds] = 0
    return arr


nrounds = 6
x = 10 + 2 * nrounds
y = 10 + 2 * nrounds
z = 1 + 2 * nrounds
space = np.zeros((x, y, z))

space = parse_input(space, inp)


def get_neighbours(pos):
    return {
        (pos[0] + 1, pos[1], pos[2]),
        (pos[0] + 1, pos[1] + 1, pos[2]),
        (pos[0] + 1, pos[1], pos[2] + 1),
        (pos[0] + 1, pos[1] + 1, pos[2] + 1),
        (pos[0] + 1, pos[1] - 1, pos[2]),
        (pos[0] + 1, pos[1] - 1, pos[2] - 1),
        (pos[0] + 1, pos[1] - 1, pos[2] + 1),
        (pos[0] + 1, pos[1], pos[2] - 1),
        (pos[0] + 1, pos[1] + 1, pos[2] - 1),
        (pos[0] - 1, pos[1], pos[2]),
        (pos[0] - 1, pos[1] + 1, pos[2]),
        (pos[0] - 1, pos[1], pos[2] + 1),
        (pos[0] - 1, pos[1] + 1, pos[2] + 1),
        (pos[0] - 1, pos[1] - 1, pos[2]),
        (pos[0] - 1, pos[1] - 1, pos[2] - 1),
        (pos[0] - 1, pos[1] - 1, pos[2] + 1),
        (pos[0] - 1, pos[1], pos[2] - 1),
        (pos[0] - 1, pos[1] + 1, pos[2] - 1),
        (pos[0], pos[1] + 1, pos[2]),
        (pos[0], pos[1], pos[2] + 1),
        (pos[0], pos[1] + 1, pos[2] + 1),
        (pos[0], pos[1] - 1, pos[2]),
        (pos[0], pos[1] - 1, pos[2] - 1),
        (pos[0], pos[1] - 1, pos[2] + 1),
        (pos[0], pos[1], pos[2] - 1),
        (pos[0], pos[1] + 1, pos[2] - 1),
    }


def count_active_neighbours(arr, pos):
    neighbours = get_neighbours(pos)
    s = 0
    for n in neighbours:
        try:
            s += arr[n[0], n[1], n[2]]
        except IndexError:
            pass
    return s


def step(arr):
    new = arr.copy()
    shape = arr.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                c = count_active_neighbours(arr, (i, j, k))
                if arr[i, j, k] == 1 and c not in {2, 3}:
                    new[i, j, k] = 0
                elif arr[i, j, k] == 0 and c == 3:
                    new[i, j, k] = 1
    return new


print(space.sum().sum().sum())
for i in range(6):
    space = step(space)
    print(space.sum().sum().sum())
