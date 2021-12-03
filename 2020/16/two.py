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


def parse_myticket(t):
    t = t.replace("your ticket:\n", "")
    return eval("[" + t.strip() + "]")


def parse_input(inp):
    rules, myticket, neartickets = inp.strip().split("\n\n")
    return parse_rules(rules), parse_myticket(myticket), parse_nearby(neartickets)


rules, my, nearby = parse_input(inp)
all_valid = set()
for r in rules:
    all_valid.update(r[1])

valid_tickets = [my]
for t in nearby:
    for v in t:
        if v not in all_valid:
            break
    else:
        valid_tickets.append(t)

possible_field = {}
for i in range(len(valid_tickets[0])):
    possible_field[i] = set()
    nums_in_field = set(map(lambda a: a[i], valid_tickets))
    for ft, valid in rules:
        for n in nums_in_field:
            if n not in valid:
                break
        else:
            possible_field[i].add(ft)

class_to_idx = {ft: -1 for ft, _ in rules}
while True:
    for i, pot_classes in possible_field.items():
        if len(pot_classes) == 1:
            break
    cl = pot_classes.pop()
    class_to_idx[cl] = i
    for _, pc in possible_field.items():
        pc.discard(cl)

    for c, i in class_to_idx.items():
        if i == -1:
            break
    else:
        break
prod = 1
for ft, idx in class_to_idx.items():
    if "departure" in ft:
        prod *= my[idx]
print(prod)
