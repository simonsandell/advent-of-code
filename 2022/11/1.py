#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")

monkeys = []


def print_monkeys():
    for i, m in enumerate(monkeys):
        print(i, m.items)


class Monkey:
    def __init__(self, lines):
        self.num_inspected = 0
        self.items = [int(x) for x in lines[0].split(": ")[1].split(", ")]
        self.op = lines[1].split(" = ")[1]
        self.test_div = int(lines[2].split(" by ")[1])
        self.to_if_true = int(lines[3].split("monkey ")[1])
        self.to_if_false = int(lines[4].split("monkey ")[1])

    def turn(self):
        self.num_inspected += len(self.items)
        for item in self.items:
            old = item
            new = eval(self.op)
            relief = new // 3
            if relief % self.test_div == 0:
                monkeys[self.to_if_true].items.append(relief)
            else:
                monkeys[self.to_if_false].items.append(relief)
        self.items = []


for i, l in enumerate(lines):
    if "Monkey" in l:
        monkeys.append(Monkey(lines[i + 1 : i + 6]))
for _ in range(20):
    for m in monkeys:
        m.turn()
active = []
for m in monkeys:
    active.append(m.num_inspected)
print(sorted(active)[-1] * sorted(active)[-2])
