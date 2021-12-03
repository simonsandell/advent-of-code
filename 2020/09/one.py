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


ints = parse_input(input)
pos = 24
while True:
    pos += 1
    summable = get_summable(ints[pos - 25 : pos])
    if ints[pos] not in summable:
        break
print(ints[pos])
