import numpy as np

with open("input") as f:
    lines = f.read().strip().split("\n")

hlines = []
vlines = []
xmax = 0
ymax = 0
for l in lines:
    coords = list(map(lambda x: tuple(int(x) for x in x.split(",")), l.split(" -> ")))
    xmax = max(xmax, coords[0][0], coords[1][0])
    ymax = max(ymax, coords[0][1], coords[1][1])
    if coords[0][0] == coords[1][0]:
        vlines.append(coords)
    if coords[0][1] == coords[1][1]:
        hlines.append(coords)

grid = np.zeros((xmax + 1, ymax + 1))

for hl in hlines:
    x1 = min(hl[0][0], hl[1][0])
    x2 = max(hl[0][0], hl[1][0])
    y = hl[0][1]
    grid[x1 : x2 + 1, y] += 1

for vl in vlines:
    y1 = min(vl[0][1], vl[1][1])
    y2 = max(vl[0][1], vl[1][1])
    x = vl[0][0]
    grid[x, y1 : y2 + 1] += 1

intersections = np.where(grid > 1)
print(intersections[0].shape[0])
