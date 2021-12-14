from functools import reduce

with open("input") as f:
    lines = f.read().strip().split("\n")

template = lines[0]

rules = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in lines[2:]}

for i in range(10):
    newline = template[0]
    for a, b in zip(template[:-1], template[1:]):
        if a + b in rules.keys():
            newline += rules[a + b] + b
    template = newline

print(
    reduce(lambda x, y: max(x, y), map(lambda x: template.count(x), set(template)))
    - reduce(lambda x, y: min(x, y), map(lambda x: template.count(x), set(template)))
)
