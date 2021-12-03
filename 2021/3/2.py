from copy import deepcopy

digits = []
with open('input') as f:
    for l in f.readlines():
        d = [int(x) for x in list(l.strip())]
        digits.append(d)

def get_most_common(digs, pos):
    n = len(digs)
    s = 0
    for d in digs:
        s += d[pos]
    if 2*s >= n:
        return 1
    if 2*s < n:
        return 0

def filter_digits(digs, pos, val):
    r = []
    for d in digs:
        if d[pos] == val:
            r.append(d)
    return r

oxy_digs = deepcopy(digits)
pos = 0
while len(oxy_digs) > 1:
    oxy_digs = filter_digits(oxy_digs, pos, get_most_common(oxy_digs, pos))
    pos += 1

co2_digs = deepcopy(digits)
pos = 0
while len(co2_digs) > 1:
    co2_digs = filter_digits(co2_digs, pos, int(not get_most_common(co2_digs, pos)))
    pos += 1

oxy = eval("0b" + "".join([str(x) for x in oxy_digs[0]]))
co2 = eval("0b" + "".join([str(x) for x in co2_digs[0]]))

print(oxy * co2)
