with open("input") as f:
    lines = f.read().strip().split("\n")

grid = []
folds = []
for l in lines:
    if not "," in l:
        if "fold" in l:
            folds.append(l.split(" ")[2])
        continue
    grid.append([int(x) for x in l.split(",")])


def fold_y(v, grid):
    for p in grid:
        if p[1] > v:
            p[1] -= 2 * (p[1] - v)


def fold_x(v, grid):
    for p in grid:
        if p[0] > v:
            p[0] -= 2 * (p[0] - v)


def count_dots(grid):
    dots = set()
    for p in grid:
        dots.add((p[0], p[1]))
    return len(dots)


for f in folds:
    if "x" in f:
        fold_x(int(f.split("=")[1]), grid)
    else:
        fold_y(int(f.split("=")), grid)
    break
print(count_dots(grid))
