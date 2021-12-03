import math

with open("input") as f:
    input = f.read()


def parse_input(input):
    target = int(input.split("\n")[0])
    depts = [int(x) for x in input.strip().split("\n")[1].split(",") if x != "x"]
    return target, depts


t, deps = parse_input(input)

pot = {}
for d in deps:
    lb = math.floor(t / d)
    ub = math.ceil(t / d)
    if lb * d >= t:
        pot[lb * d] = (d, lb)
    elif ub * d >= t:
        pot[ub * d] = (d, lb)

earliest = sorted(list(pot.keys()))[0]
d = pot[earliest][0]
diff = earliest - t
print(diff * d)
