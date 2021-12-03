from operator import add
from functools import reduce

digits = []
with open('input') as f:
    for l in f.readlines():
        d = [int(x) for x in list(l.strip())]
        digits.append(d)

n = float(len(digits))
f = lambda x,y : map(add, x, y)
summed = list(reduce(f, digits))

gamma = list(map(lambda x: round(x/n), summed))
epsilon = [int(not x) for x in gamma]

gamma = eval("0b" + "".join([str(x) for x in gamma]))
epsilon = eval("0b" + "".join([str(x) for x in epsilon]))

print(gamma*epsilon)

