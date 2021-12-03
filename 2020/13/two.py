import math
from functools import reduce

with open("tinput") as f:
    input = f.read()


def parse_input(input):
    deps = []
    for i, x in enumerate(input.strip().split("\n")[1].split(",")):
        if x != "x":
            deps.append((int(x), i))
    return deps


deps = parse_input(input)
deps.sort(key=lambda x: x[0], reverse=True)


def check_condition(t, dep, diff):
    if (t + diff) % dep == 0:
        return True
    return False


def get_t(n, dep, diff):
    return dep * n - diff


def solve(deps):
    n0 = 1
    t = n0 * deps[0][0]
    while True:
        for i in range(1, len(deps)):
            if not check_condition(t, deps[i][0], deps[i][1]):
                n0 += 1
                t = get_t(n0, deps[0][0], deps[0][1])
                break
        else:
            break
    return t


def solve_next(deps, t, tstep):
    while True:
        for i in range(len(deps)):
            if not check_condition(t, deps[i][0], deps[i][1]):
                t += tstep
                break
        else:
            break
    return t


def get_prod(deps):
    return reduce(lambda a, b: a * b, map(lambda a: a[0], deps))


t0 = 1
tstep = 1

for i in range(2, 1 + len(deps)):
    t0 = solve_next(deps[:i], t0, tstep)
    tstep = get_prod(deps[:i])
    print(t0)
