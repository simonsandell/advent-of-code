

with open('input', 'r') as f:
    input = f.read()

ints = [int(x) for x in input.strip().split('\n')]

def find_values_that_sum(ints, sum):
    for i,x in enumerate(ints):
        for y in ints[i+1:]:
            if x + y == sum:
                break
        else:
            continue
        break
    return x,y

x,y = find_values_that_sum(ints, 2020)
print(x*y)

