import re
from copy import deepcopy

with open("input") as f:
    inp = f.read()


def expand_rules(r):
    newr = deepcopy(r)
    for k, v in r.items():
        newv = ""
        for n in v.split(" "):
            if n.isnumeric():
                newv += r[n] + " "
            else:
                newv += n + " "
        newr[k] = newv.strip()
    return newr


def trim_rules(r):
    newr = deepcopy(r)
    for k, v in r.items():
        newv = v.replace('"', "").replace(" ", "")
        newr[k] = newv
    return newr


def check_numeric_vals(r):
    for v in r.values():
        if re.search("\d", v):
            return True
    return False


def parse_rules(rules):
    r = {}
    for l in rules.strip().split("\n"):
        k, v = l.split(": ")
        if "|" in v:
            v = "( " + v + " )"
        r[k] = v
    while check_numeric_vals(r):
        r = expand_rules(r)
    r = trim_rules(r)
    return r


def parse_input(inp):
    rules, messages = inp.strip().split("\n\n")
    r = parse_rules(rules)
    return r, messages


rules, messages = parse_input(inp)

c = 0
for m in messages.strip().split("\n"):
    if re.fullmatch(rules["0"], m):
        c += 1
print(c)
