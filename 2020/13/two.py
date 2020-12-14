import math
from functools import reduce
with open('input') as f:
    input = f.read()

def parse_input(input):
    deps = []
    for i,x in enumerate(input.strip().split('\n')[1].split(',')):
        if x != 'x':
            deps.append((int(x),i))
    return deps

"""
n_0*d_0 = x
n_1*d_1 - 1 = x
n_2*d_2 - 2 = x
...

n_1*d_1 = n_0*d_0 + 1
"""


deps = parse_input(input)
deps.sort(key=0)
print(deps)
print(reduce(lambda x,y: x*y, map(lambda x: x[0],deps)))
smallest = 100000000000000

def check_condition(x, dep, diff):
    # dep*n = x + diff
    # n = (x + diff)/dep
    nl = math.floor((x+diff)/dep)
    nu = math.ceil((x+diff)/dep)
    if nl*dep -diff == x:
        return True
    if nu*dep -diff == x:
        return True
    return False

def get_x(n, dep, diff):
    return dep*n -diff



