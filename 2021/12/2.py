from collections import deque

with open("input") as f:
    lines = f.read().strip().split("\n")

graph = dict()
for l in lines:
    f, t = l.split("-")
    if t not in graph.keys():
        graph[t] = set()
    if f not in graph.keys():
        graph[f] = set()
    if t != "start":
        graph[f].add(t)
    if f != "start":
        graph[t].add(f)
graph["end"] = set()


def get_possible_next(path):
    if path[0] == "used_double":
        return graph[path[-1]].difference([x for x in path if x.lower() == x])
    return graph[path[-1]]


open_paths = deque()
for n in graph["start"]:
    open_paths.append(["start", n])

closed_paths = []
while len(open_paths) > 0:
    p = open_paths.pop()
    nn = get_possible_next(p)
    if not nn:
        if p[-1] == "end":
            closed_paths.append(p)
    for n in nn:
        np = p.copy()
        np.append(n)
        if n in p and n.lower() == n:
            np.insert(0, "used_double")
        open_paths.append(np)
print(len(closed_paths))
