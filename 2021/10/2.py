with open("input") as f:
    lines = f.read().strip().split("\n")


def score_line(l):
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
            return -1
    score = 0
    for c in reversed(s):
        if c == "(":
            score *= 5
            score += 1
        if c == "[":
            score *= 5
            score += 2
        if c == "{":
            score *= 5
            score += 3
        if c == "<":
            score *= 5
            score += 4
    return score


scores = []
for l in lines:
    s = score_line(l)
    if s >= 0:
        scores.append(s)
winner = int(len(scores) / 2)
print(sorted(scores)[winner])
