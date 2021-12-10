with open("input") as f:
    p = f.read().strip()

floor = 0
i = 0
while floor >= 0:
    floor += 1 if p[i] == "(" else -1
    i += 1
print(i)
