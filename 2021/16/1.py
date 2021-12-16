#!/usr/bin/env python
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

with open(infile) as f:
    hexstr = f.read().strip()
    hlen = len(hexstr * 4)
    bstr = (bin(int(hexstr, 16))[2:]).zfill(hlen)


i = 0
versionsum = 0
while i + 7 < len(bstr):
    version = int(bstr[i : i + 3], 2)
    versionsum += version
    typeid = int(bstr[i + 3 : i + 6], 2)
    if typeid == 4:
        j = 0
        while bstr[i + 6 + j] != "0":
            j += 5
        step = 6 + j + 5
        #        while step % 4 != 0:
        #            step += 1
        i += step
    else:
        lengthtypeid = int(bstr[i + 6], 2)
        if lengthtypeid == 0:
            subpacketlength = int(bstr[i + 7 : i + 22], 2)
            i += 22
        else:
            numsubpackets = int(bstr[i + 7 : i + 18], 2)
            i += 18
print(versionsum)
