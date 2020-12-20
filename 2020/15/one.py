
with open('input') as f:
    inp = f.read()


def parse_input(input):
    return eval('[' + input + ']')

m = parse_input(inp)

turn = len(m) -1
while turn < 2019:
    if m.count(m[turn]) == 1:
        m.append(0)
    else:
        idx = len(m) - 1 - list(reversed(m)).index(m[turn],1)
        m.append(turn - idx)
    turn += 1
print(m[turn])
