with open("input") as f:
    directions = f.read().strip()

positions = {(0, 0)}
x, y = 0, 0
rx, ry = 0, 0
for i, d in enumerate(directions):
    if d == ">":
        if i % 2:
            rx += 1
        else:
            x += 1
    if d == "<":
        if i % 2:
            rx -= 1
        else:
            x -= 1
    if d == "^":
        if i % 2:
            ry += 1
        else:
            y += 1
    if d == "v":
        if i % 2:
            ry -= 1
        else:
            y -= 1
    if i % 2:
        positions.add((rx, ry))
    else:
        positions.add((x, y))
print(len(positions))
