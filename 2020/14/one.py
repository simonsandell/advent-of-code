with open('input') as f:
    input = f.read().strip()

def parse_mask(m):
    mask = m.replace('mask = ','')
    o_mask = 0
    a_mask = (2**36) - 1
    for i,c in enumerate(mask):
        if c == '1':
            o_mask += 2**(35-i)
        if c == '0':
            a_mask -= 2**(35-i)
    return o_mask, a_mask

def parse_mem(m):
    return [int(x) for x in m.replace('mem[','').split('] = ')]

def mask_value(val, o, a):
    return (val | o) & a

def load_program(input):
    memory = {}
    om = 0
    am = 0
    for l in [x.strip() for x in input.split('\n')]:
        if 'mask' in l:
            om, am = parse_mask(l)
        if 'mem' in l:
            key, val = parse_mem(l)
            memory[key] = mask_value(val, om, am)
    return memory

print(sum(list(load_program(input).values())))
