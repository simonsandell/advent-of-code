with open("input") as f:
    lines = f.read().strip().split("\n")


def parseable_line(l):
    s = []
    for c in list(l):
        if c in {"(", "[", "{", "<"}:
            s.append(c)
        else:
            m = s.pop()
            if c == ")" and m == "(":
                continue
            if c == "]" and m == "[":
                continue
            if c == "}" and m == "{":
                continue
            if c == ">" and m == "<":
                continue
            return c


scoremap = {")": 3, "]": 57, "}": 1197, ">": 25137}
illegal_count = {")": 0, "]": 0, "}": 0, ">": 0}

for l in lines:
    illegal = parseable_line(l)
    if illegal:
        illegal_count[illegal] = illegal_count[illegal] + 1
score = 0
for k, v in scoremap.items():
    score += v * illegal_count[k]
print(score)
