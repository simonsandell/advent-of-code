#!/usr/bin/env python
import sys
from functools import reduce

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

with open(infile) as f:
    hexstr = f.read().strip()
    hlen = len(hexstr * 4)
    bstr = (bin(int(hexstr, 16))[2:]).zfill(hlen)
from operator import add, mul, lt, gt, eq

operators = {0: add, 1: mul, 2: min, 3: max, 5: gt, 6: lt, 7: eq}
i = 0


def solve(bstr):
    version = int(bstr[:3], 2)
    typeid = int(bstr[3:6], 2)
    if typeid == 4:
        # literal
        j = 0
        valpart = bstr[j + 7 : j + 11]
        while bstr[j + 6] != "0":
            j += 5
            valpart += bstr[j + 7 : j + 11]
        step = 6 + j + 5
        value = int(valpart, 2)
        return value, step
    else:
        lengthtypeid = int(bstr[6], 2)
        if lengthtypeid == 0:
            subpacketlength = int(bstr[7:22], 2)
            i = 0
            values = []
            while i < subpacketlength:
                val, l = solve(bstr[22 + i :])
                values.append(val)
                i += l
            assert i == subpacketlength
            return int(reduce(operators[typeid], values)), 22 + subpacketlength
        else:
            numsubpackets = int(bstr[7:18], 2)
            i = 0
            values = []
            for _ in range(numsubpackets):
                val, l = solve(bstr[18 + i :])
                values.append(val)
                i += l
            return int(reduce(operators[typeid], values)), 18 + i


print(solve(bstr)[0])
