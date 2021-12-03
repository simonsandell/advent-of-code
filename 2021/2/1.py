
with open('input') as f:
    lines = f.read().strip().split('\n')
instructions = [(x.split(' ')[0], int(x.split(' ')[1])) for x in lines]

hpos = 0
depth = 0

for mode,value in instructions:
    if mode == 'forward':
        hpos += value
    if mode == 'down':
        depth += value
    if mode == 'up':
        depth -= value

print(hpos * depth)

