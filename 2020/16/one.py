with open("input") as f:
    inp = f.read()


def parse_rules(r):
    res = []
    for l in (x.strip() for x in r.split("\n")):
        field_name, ranges = l.split(":")
        ranges = ranges.strip().split(" or ")
        valid_nums = set()
        for r in ranges:
            r0, r1 = [int(x) for x in r.split("-")]
            for i in range(r0, r1 + 1):
                valid_nums.add(i)
        res.append((field_name, valid_nums))
    return res


def parse_nearby(t):
    tickets = []
    t = t.replace("nearby tickets:\n", "")
    for l in (x.strip() for x in t.split("\n")):
        tickets.append(eval("[" + l + "]"))
    return tickets


def parse_input(inp):
    rules, myticket, neartickets = inp.strip().split("\n\n")
    return parse_rules(rules), myticket, parse_nearby(neartickets)


def check_valid(num, rules):
    pass


rules, my, nearby = parse_input(inp)
all_valid = set()
for r in rules:
    all_valid.update(r[1])
tser = 0
for t in nearby:
    for v in t:
        if v not in all_valid:
            tser += v
print(tser)
