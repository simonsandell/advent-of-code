with open("input") as f:
    lines = f.read().strip().split("\n")

width = len(lines[0])
height = len(lines)
tot_risk_level = 0
for i, l in enumerate(lines):
    for j, v in enumerate(list(l)):
        up = "a"
        down = "a"
        left = "a"
        right = "a"

        if i - 1 >= 0:
            up = lines[i - 1][j]
        if i + 1 < height:
            down = lines[i + 1][j]
        if j + 1 < width:
            right = lines[i][j + 1]
        if j - 1 >= 0:
            left = lines[i][j - 1]
        if up > v and down > v and left > v and right > v:
            tot_risk_level += int(v) + 1
print(tot_risk_level)
