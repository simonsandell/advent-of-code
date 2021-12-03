from functools import reduce

with open("input") as f:
    input = f.read()


def parse_input(input):
    res = []
    for l in input.strip().split("\n"):
        res.append(int(l))
    return res


def get_summable(ints):
    unique = list(set(ints))
    sums = set()
    for i in unique[:-1]:
        for j in unique[1:]:
            sums.add(i + j)
    return sums


def find_contigous(ints, target):
    for i, int1 in enumerate(ints[:-1]):
        pos = [i]
        sum = int1
        for j, int2 in enumerate(ints[i + 1 :]):
            pos.append(i + 1 + j)
            sum += int2
            if sum >= target:
                break
        else:
            raise Exception
        if sum == target:
            break
        else:
            pass
    return pos


ints = parse_input(input)
unsummables = []
pos = 24
while True:
    pos += 1
    summable = get_summable(ints[pos - 25 : pos])
    if ints[pos] not in summable:
        unsummable = ints[pos]
        break

cont = find_contigous(ints, unsummable)
vals = list(map(lambda x: ints[x], cont))
print(min(vals) + max(vals))
