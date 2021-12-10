with open("input") as f:
    directions = f.read().strip()

positions = {(0, 0)}
x, y = 0, 0
for d in directions:
    if d == ">":
        x += 1
    if d == "<":
        x -= 1
    if d == "^":
        y += 1
    if d == "v":
        y -= 1
    positions.add((x, y))
print(len(positions))
