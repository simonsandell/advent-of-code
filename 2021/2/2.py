
with open('input') as f:
    lines = f.read().strip().split('\n')
instructions = [(x.split(' ')[0], int(x.split(' ')[1])) for x in lines]

hpos = 0
depth = 0
aim = 0

for mode,value in instructions:
    if mode == 'forward':
        hpos += value
        depth += aim*value
    if mode == 'down':
        aim += value
    if mode == 'up':
        aim -= value

print(hpos * depth)

