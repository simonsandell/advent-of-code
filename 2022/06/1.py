#!/usr/bin/env python
import sys
from collections import deque

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip()


def is_start_of_packet(marker):
    if len(set(marker)) == 4:
        return True
    return False


marker = deque()
for i, c in enumerate(lines):
    marker.append(c)
    if i < 3:
        continue
    if is_start_of_packet(marker):
        print(i + 1)
        break
    marker.popleft()
