with open("input") as f:
    outp_joltages = [int(x) for x in f.read().strip().split("\n")]

ones = 0
twoes = 0
threes = 0

sorted_joltages = sorted(outp_joltages)
len_bef = len(sorted_joltages)
sorted_joltages.insert(0, 0)
sorted_joltages.append(sorted_joltages[-1] + 3)
assert len_bef + 2 == len(sorted_joltages)

for i, j in zip(sorted_joltages[:-1], sorted_joltages[1:]):
    if j - i == 1:
        ones += 1
    if j - i == 2:
        twoes += 1
    if j - i == 3:
        threes += 1


print(ones, twoes, threes)
print(ones * threes)
