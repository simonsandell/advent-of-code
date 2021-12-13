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


def combine_dots(grid):
    dots = set()
    for p in grid:
        dots.add((p[0], p[1]))
    return dots


for f in folds:
    if "x" in f:
        fold_x(int(f.split("=")[1]), grid)
    else:
        fold_y(int(f.split("=")[1]), grid)


def plot_dots(dots):
    xmax, ymax = 0, 0
    for p in dots:
        if p[0] > xmax:
            xmax = p[0]
        if p[1] > ymax:
            ymax = p[1]
    picture = ""
    for y in range(ymax + 1):
        for x in range(xmax + 1):
            if (x, y) in dots:
                picture += "#"
            else:
                picture += "."
        picture += "\n"
    print(picture)


plot_dots(combine_dots(grid))
