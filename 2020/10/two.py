from functools import reduce

with open("input") as f:
    outp_joltages = [int(x) for x in f.read().strip().split("\n")]

sort = sorted(outp_joltages)
ints = [0, *sort, sort[-1] + 3]


def get_diff(ints):
    res = []
    for i, j in zip(ints[:-1], ints[1:]):
        if j - i == 1:
            res.append(1)
        if j - i == 2:
            res.append(2)
        if j - i == 3:
            res.append(3)
    return res


diffs = get_diff(ints)


def count_contigous_ones(diffs):
    count = {i: 0 for i in range(len(diffs))}
    s = 0
    for i in diffs:
        if i == 3:
            count[s] += 1
            s = 0
        else:
            s += 1
    count.pop(0)
    zerokeys = [x for x in count.keys() if count[x] == 0]
    [count.pop(z) for z in zerokeys]
    return count


print(count_contigous_ones(diffs))


def get_num_permutations(i):
    if i == 0:
        return 1
    if i == 1:
        return 1
    if i == 2:
        return 2
    if i == 3:
        return 4
    if i == 4:
        return 7


prod = 1
for key, val in count_contigous_ones(diffs).items():
    if val != 0:
        prod *= get_num_permutations(key) ** val
print(prod)
