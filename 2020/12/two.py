shippos = [0, 0]
waypoint = [10, 1]


def move_east(n):
    waypoint[0] += n


def move_west(n):
    waypoint[0] -= n


def move_north(n):
    waypoint[1] += n


def move_south(n):
    waypoint[1] -= n


def rotate_clockwise():
    global waypoint
    waypoint = [-waypoint[1], waypoint[0]]


def rotate_anticlock():
    global waypoint
    waypoint = [waypoint[1], -waypoint[0]]


def turn_left(d):
    n = round(d / 90)
    for i in range(n):
        rotate_clockwise()


def turn_right(d):
    n = round(d / 90)
    for i in range(n):
        rotate_anticlock()


def move_forward(n):
    shippos[0] += waypoint[0] * n
    shippos[1] += waypoint[1] * n


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

print(abs(shippos[0]) + abs(shippos[1]))
