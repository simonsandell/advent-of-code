from functools import reduce

with open("input") as f:
    input = f.read()


def get_empty_plane(rows=128, cols=8):
    plane = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        plane.append(row)
    return plane


def get_midpoints(min, max):
    return (min + int((max - min) / 2), min + round(0.5 + (max - min) / 2))


def find_seat(string):
    rowrange = [0, 127]
    for c in string[:-3]:
        if c == "F":
            rowrange[1] = get_midpoints(rowrange[0], rowrange[1])[0]
        elif c == "B":
            rowrange[0] = get_midpoints(rowrange[0], rowrange[1])[1]
        else:
            raise Exception
    colrange = [0, 7]
    for c in string[-3:]:
        if c == "L":
            colrange[1] = get_midpoints(colrange[0], colrange[1])[0]
        elif c == "R":
            colrange[0] = get_midpoints(colrange[0], colrange[1])[1]
        else:
            raise Exception
    return rowrange[0], colrange[0]


def get_seatid(row, col):
    return (row * 8) + col


def get_rowcol(seatid):
    col = seatid % 8
    row = (seatid - col) // 8
    return row, col


def mark_seat(plane, row, col):
    plane[row][col] = 1


plane = get_empty_plane()
seats = [x.strip() for x in input.strip().split("\n")]
for s in seats:
    mark_seat(plane, *find_seat(s))
unmarked = []
for row in range(1, 127):
    for col in range(0, 8):
        if plane[row][col] == 0:
            unmarked.append(get_seatid(row, col))
for u in unmarked:
    if u - 1 in unmarked or u + 1 in unmarked:
        continue
    print(u)
