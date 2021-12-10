with open("input") as f:
    p = f.read().strip()

print(p.count("(") - p.count(")"))
