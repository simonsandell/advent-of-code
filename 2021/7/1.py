with open("input") as f:
    positions = [int(x) for x in f.read().strip().split(",")]

minp = min(positions)
maxp = max(positions)

position_dist = dict()
for p in positions:
    if p not in position_dist:
        position_dist[p] = 0
    position_dist[p] += 1


def compute_cost(pos, dest):
    c = 0
    for k, v in pos.items():
        c += abs(k - dest) * v
    return c


cost_dist = dict()
for p in range(minp, maxp + 1):
    cost_dist[p] = compute_cost(position_dist, p)

print(cost_dist[min(cost_dist, key=cost_dist.get)])
