with open('input') as f:
    lines = [int(x) for x in f.read().strip().split('\n')]

count_increase = 0
prev = -1
for x,y,z in zip(lines[0:-2], lines[1:-1], lines[2:]):
    if prev == -1:
        prev = x + y + z
        continue
    if (x + y + z) > prev:
        count_increase += 1
    prev = x + y + z
print(count_increase)
