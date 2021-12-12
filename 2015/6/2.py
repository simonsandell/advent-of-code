import numpy as np

with open("input") as f:
    lines = f.read().strip().split("\n")

grid = np.zeros((1000, 1000))


def parse_line(l):
    parts = list(reversed(l.split(" ")))
    instruction = parts[3]
    pos1 = [int(x) for x in parts[0].split(",")]
    pos2 = [int(x) for x in parts[2].split(",")]
    fr = (min(pos1[0], pos2[0]), min(pos1[1], pos2[1]))
    to = max(pos1[0], pos2[0]), max(pos1[1], pos2[1])
    return instruction, fr, to


def turn_on(grid, fr, to):
    grid[fr[0] : to[0] + 1, fr[1] : to[1] + 1] += 1


def turn_off(grid, fr, to):
    grid[fr[0] : to[0] + 1, fr[1] : to[1] + 1] -= 1
    grid[grid < 0] = 0


def toggle(grid, fr, to):
    grid[fr[0] : to[0] + 1, fr[1] : to[1] + 1] += 2


for l in lines:
    instr, fr, to = parse_line(l)
    if instr == "on":
        turn_on(grid, fr, to)
    if instr == "off":
        turn_off(grid, fr, to)
    if instr == "toggle":
        toggle(grid, fr, to)
print(int(sum(sum(grid))))
