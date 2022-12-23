#!/usr/bin/env python
import sys
from itertools import zip_longest

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")
lines.append("")
lines.append("[[2]]")
lines.append("[[6]]")


def compare(l, r):
    if l is None and r is not None:
        return True
    if r is None and l is not None:
        return False
    if type(l) == type(r) is int:
        if l < r:
            return True
        elif r == l:
            return None
        return False
    if type(l) == type(r) is list:
        for li, ri in zip_longest(l, r):
            c = compare(li, ri)
            if c:
                return True
            elif c is None:
                continue
            else:
                return False
        return None
    if type(l) is int:
        return compare([l], r)
    if type(r) is int:
        return compare(l, [r])


class Packet:
    def __init__(self, v):
        self.value = v

    def __lt__(self, other):
        return compare(self.value, other.value)

    def __eq__(self, other):
        return self == other

    def __repr__(self):
        return str(self.value)


packets = []
for i in range(0, len(lines), 3):
    left = eval(lines[i])
    right = eval(lines[i + 1])
    packets.append(Packet(left))
    packets.append(Packet(right))
sorted_packets = [x for x in sorted(packets)]
decoder_key = 1
for i, p in enumerate(sorted_packets):
    if p.value == [[2]] or p.value == [[6]]:
        decoder_key *= i + 1
print(decoder_key)
