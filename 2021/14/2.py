with open("input") as f:
    lines = f.read().strip().split("\n")

template = lines[0]

rules = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in lines[2:]}
num_pairs = {k: 0 for k in rules.keys()}
components = set(rules.values())
comp_num = {c: template.count(c) for c in components}
for a, b in zip(template[:-1], template[1:]):
    num_pairs[a + b] += 1
for i in range(40):
    next_pairs = num_pairs.copy()
    for k, v in rules.items():
        a, b = list(k)
        n = num_pairs[k]
        next_pairs[k] -= n
        next_pairs[a + v] += n
        next_pairs[v + b] += n
        comp_num[v] += n
    num_pairs = next_pairs
print(
    comp_num[max(comp_num, key=comp_num.get)]
    - comp_num[min(comp_num, key=comp_num.get)]
)
