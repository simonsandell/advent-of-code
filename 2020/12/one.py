pos = [0, 0]
direction = 0


def move_west(n):
    pos[1] += n


def move_south(n):
    pos[0] += n


def move_east(n):
    pos[1] -= n


def move_north(n):
    pos[0] -= n


dir_to_card = {0: move_east, 90: move_south, 180: move_west, 270: move_north}


def turn_right(d):
    global direction
    direction += d
    direction = direction % 360


def turn_left(d):
    turn_right(-d)


def move_forward(n):
    dir_to_card[direction](n)


char_to_action = {
    "E": move_east,
    "S": move_south,
    "W": move_west,
    "N": move_north,
    "L": turn_left,
    "R": turn_right,
    "F": move_forward,
}

with open("input") as f:
    input = f.read()

for l in [x.strip() for x in input.strip().split("\n")]:
    c = l[0]
    n = int(l[1:])
    char_to_action[c](n)
print(abs(pos[0]) + abs(pos[1]))
