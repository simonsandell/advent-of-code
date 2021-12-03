from itertools import combinations

with open("input") as f:
    input = f.read().strip()


def parse_mask(m):
    mask = m.replace("mask = ", "")
    o_mask = 0
    f_mask = set()
    for i, c in enumerate(mask):
        if c == "1":
            o_mask += 2 ** (35 - i)
        if c == "X":
            f_mask.add(36 - i)
    return o_mask, f_mask


def parse_mem(m):
    return [int(x) for x in m.replace("mem[", "").split("] = ")]


def get_m(val):
    m = bin(val)
    while len(m) != 38:
        m = "0b0" + m[2:]
    return m


def set_zero(val, pos):
    m = get_m(val)
    l = len(m)
    m = m[: l - pos] + "0" + m[l - pos + 1 :]
    return eval(m)


def set_one(val, pos):
    m = get_m(val)
    l = len(m)
    m = m[: l - pos] + "1" + m[l - pos + 1 :]
    return eval(m)


def mask_addr(val, o, f):
    masked = val | o
    res = {masked}
    for v in f:
        additional = set()
        for r in res:
            additional.add(set_one(r, v))
            additional.add(set_zero(r, v))
        res.update(additional)
    return res


def load_program(input):
    memory = {}
    om = 0
    fm = []
    for l in [x.strip() for x in input.split("\n")]:
        if "mask" in l:
            om, fm = parse_mask(l)
        if "mem" in l:
            key, val = parse_mem(l)
            addr = mask_addr(key, om, fm)
            for a in addr:
                memory[a] = val
    return memory


print(sum(list(load_program(input).values())))
