with open("input") as f:
    lines = f.read().strip().split("\n")


def parse_line(l):
    digits, reading = l.split(" | ")
    return [frozenset(x) for x in digits.split(" ")], [
        frozenset(x) for x in reading.split(" ")
    ]


def decode(digits):
    mapping = {
        0: "",  # 6
        1: "",  # 2
        2: "",  # 5
        3: "",  # 5
        4: "",  # 4
        5: "",  # 5
        6: "",  # 6
        7: "",  # 3
        8: "",  # 7
        9: "",  # 6
    }
    for d in digits:
        if len(d) == 2:
            mapping[1] = d
        if len(d) == 3:
            mapping[7] = d
        if len(d) == 4:
            mapping[4] = d
        if len(d) == 7:
            mapping[8] = d
    tl_m = mapping[4].difference(mapping[1])
    for d in digits:
        # 2, 3 or 5
        if len(d) == 5:
            if len(d.difference(mapping[1])) == 3:
                mapping[3] = d
            elif len(d.difference(tl_m)) == 3:
                mapping[5] = d
            else:
                mapping[2] = d
    bl = mapping[2].difference(mapping[5]).difference(mapping[1])
    for d in digits:
        # 0, 6 or 9
        if len(d) == 6:
            if len(d.intersection(mapping[1])) == 1:
                mapping[6] = d
            elif d.intersection(bl) == frozenset():
                mapping[9] = d
            else:
                mapping[0] = d
    return {v: k for k, v in mapping.items()}


def get_value(mapping, reading):
    s = 0
    for i, v in enumerate(reversed(reading)):
        s += mapping[v] * (10 ** i)
    return s


total = 0
for l in lines:
    digits, reading = parse_line(l)
    mapping = decode(digits)
    total += get_value(mapping, reading)
print(total)
