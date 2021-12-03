with open("input", "r") as f:
    input = f.read()

ints = [int(x) for x in input.strip().split("\n")]


def find_three_values_that_sum(ints, sum):
    for i, x in enumerate(ints[:-2]):
        for j, y in enumerate(ints[i + 1 : -1]):
            for z in ints[i + j + 1 :]:
                if x + y + z == sum:
                    break
            else:
                continue
            break
        else:
            continue
        break
    return x, y, z


x, y, z = find_three_values_that_sum(ints, 2020)
print(x * y * z)
