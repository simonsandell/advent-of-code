#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")

sand_origin = (500, 0)
rock = set()
sand = set()


def get_rocks(p, q):
    if p[0] == q[0]:
        ymin = min(p[1], q[1])
        ymax = max(p[1], q[1])
        for y in range(ymin, ymax + 1):
            yield (p[0], y)
    elif p[1] == q[1]:
        xmin = min(p[0], q[0])
        xmax = max(p[0], q[0])
        for x in range(xmin, xmax + 1):
            yield (x, p[1])
    else:
        assert False, (p, q)


MAX_Y = 0
for l in lines:
    positions = [tuple(int(n) for n in pos.split(",")) for pos in l.split(" -> ")]
    for p, q in zip(positions[:-1], positions[1:]):
        for r in get_rocks(p, q):
            rock.add(r)
            if r[1] > MAX_Y:
                MAX_Y = r[1]


def draw(xrange, yrange):
    s = ""
    for y in range(yrange[0], yrange[1]):
        for x in range(xrange[0], xrange[1]):
            if (x, y) in rock:
                s += "#"
            elif (x, y) in sand:
                s += "o"
            elif (x, y) == sand_origin:
                s += "+"
            else:
                s += "."
        s += "\n"
    print(s)


def add_sand():
    x, y = sand_origin
    blockers = rock.union(sand)
    while True:
        below = (x, y + 1)
        below_left = (x - 1, y + 1)
        below_right = (x + 1, y + 1)
        if y == MAX_Y:
            return False
        elif below not in blockers:
            x, y = below
            continue
        elif below_left not in blockers:
            x, y = below_left
            continue
        elif below_right not in blockers:
            x, y = below_right
            continue
        else:
            sand.add((x, y))
            return True


while add_sand():
    # draw((485, 515), (0, 25))
    pass

print(len(sand))
