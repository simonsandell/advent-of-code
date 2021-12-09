from functools import reduce

with open("input") as f:
    lines = f.read().strip().split("\n")

width = len(lines[0])
height = len(lines)

lowpoints = []

for i, l in enumerate(lines):
    for j, v in enumerate(list(l)):
        up = "a"
        down = "a"
        left = "a"
        right = "a"

        if i - 1 >= 0:
            up = lines[i - 1][j]
        if i + 1 < height:
            down = lines[i + 1][j]
        if j + 1 < width:
            right = lines[i][j + 1]
        if j - 1 >= 0:
            left = lines[i][j - 1]
        if up > v and down > v and left > v and right > v:
            lowpoints.append((i, j))


def get_neighbours(i, j):
    n = set()
    if i - 1 >= 0:
        if lines[i - 1][j] < "9":
            n.add((i - 1, j))
    if i + 1 < height:
        if lines[i + 1][j] < "9":
            n.add((i + 1, j))
    if j + 1 < width:
        if lines[i][j + 1] < "9":
            n.add((i, j + 1))
    if j - 1 >= 0:
        if lines[i][j - 1] < "9":
            n.add((i, j - 1))
    return n


def count_basin(x, y):
    basin = {(x, y)}
    unchecked = {(x, y)}
    while unchecked != set():
        new_to_check = set()
        for coord in unchecked:
            n = get_neighbours(*coord)
            new_to_check = new_to_check.union(n.difference(basin))
            basin = basin.union(n)
        unchecked = new_to_check
    return len(basin)


sizes = []
for lp in lowpoints:
    sizes.append(count_basin(*lp))
print(reduce(lambda x, y: x * y, sorted(sizes)[-3:]))
