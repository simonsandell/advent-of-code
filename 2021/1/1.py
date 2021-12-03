with open("input") as f:
    lines = f.read().strip().split("\n")
count_increase = 0
prev = -1
for l in lines:
    if prev == -1:
        prev = int(l)
        continue
    if int(l) > prev:
        count_increase += 1
    prev = int(l)
print(count_increase)
