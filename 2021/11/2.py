import numpy as np

arr = np.zeros((10, 10))
with open("input") as f:
    lines = f.read().strip().split("\n")
for i, l in enumerate(lines):
    for j, x in enumerate((int(x) for x in l)):
        arr[i, j] = x


def apply_flash(grid, pos):
    i, j = pos
    if i - 1 >= 0:
        grid[i - 1, j] += 1
    if i + 1 < 10:
        grid[i + 1, j] += 1
    if j + 1 < 10:
        grid[i, j + 1] += 1
    if j - 1 >= 0:
        grid[i, j - 1] += 1

    if i - 1 >= 0 and j - 1 >= 0:
        grid[i - 1, j - 1] += 1
    if i - 1 >= 0 and j + 1 < 10:
        grid[i - 1, j + 1] += 1
    if i + 1 < 10 and j - 1 >= 0:
        grid[i + 1, j - 1] += 1
    if i + 1 < 10 and j + 1 < 10:
        grid[i + 1, j + 1] += 1


def step(grid):
    grid += np.ones(grid.shape)
    flashed = np.zeros(grid.shape) == 1
    while True:
        to_flash = np.logical_and(grid > 9, ~flashed)
        if not np.any(to_flash):
            break
        for pos in np.argwhere(to_flash):
            apply_flash(grid, pos)
        flashed = np.logical_or(flashed, to_flash)
    flash_count = sum(sum(grid > 9))
    grid[grid > 9] = 0
    return flash_count


i = 0
while True:
    i += 1
    flashcount = step(arr)
    if flashcount == 100:
        break
print(i)
