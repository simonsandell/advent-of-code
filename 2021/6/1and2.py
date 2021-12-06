with open("input") as f:
    fishes = [int(x) for x in f.read().strip().split(",")]


fish_dist = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
for fish in fishes:
    fish_dist[fish] = fish_dist[fish] + 1

for i in range(256):
    if i == 80:
        print(sum(fish_dist.values()))
    new_dist = fish_dist.copy()
    new_dist[0] = fish_dist[1]
    new_dist[1] = fish_dist[2]
    new_dist[2] = fish_dist[3]
    new_dist[3] = fish_dist[4]
    new_dist[4] = fish_dist[5]
    new_dist[5] = fish_dist[6]
    new_dist[6] = fish_dist[7] + fish_dist[0]
    new_dist[7] = fish_dist[8]
    new_dist[8] = fish_dist[0]
    fish_dist = new_dist
print(sum(fish_dist.values()))
