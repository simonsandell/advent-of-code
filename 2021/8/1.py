with open("input") as f:
    lines = f.read().strip().split("\n")


def parse_line(l):
    digits, reading = l.split(" | ")
    return digits.split(" "), reading.split(" ")


ones, fours, sevens, eights = 0, 0, 0, 0
for l in lines:
    _, reading = parse_line(l)
    for r in reading:
        if len(r) == 2:
            ones += 1
        if len(r) == 3:
            sevens += 1
        if len(r) == 4:
            fours += 1
        if len(r) == 7:
            eights += 1

print(sum((ones, fours, sevens, eights)))
