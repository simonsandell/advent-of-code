from functools import reduce

with open("input") as f:
    input = f.read()


def get_empty_plane(rows=128, cols=8):
    row = [0] * cols
    return [row] * rows


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


seats = [x.strip() for x in input.split("\n")]
print(
    reduce(
        lambda x, y: x if x > y else y, map(lambda x: get_seatid(*find_seat(x)), seats)
    )
)
