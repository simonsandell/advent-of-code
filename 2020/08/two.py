from runner import Runner
with open('input') as f:
    input = f.read()

def parse_int(inp):
    val = int(inp[1:])
    if inp[0] == '-':
        return -1*val
    return val

def parse_input(inp):
    instructions = []
    for l in inp.strip().split('\n'):
        ins = l[:3]
        val = parse_int(l[4:])
        instructions.append((ins,val))
    return instructions

instructions = parse_input(input)

def run(instructions):
    finished, acc = Runner().run_instructions(instructions)
    if finished:
        print(acc)
        exit()

for i in range(len(instructions)):
    inst = instructions[i]
    if inst[0] == 'jmp':
        instructions[i] = ('nop', inst[1])
        run(instructions)
        instructions[i] = inst
    if inst[0] == 'nop':
        instructions[i] = ('jmp', inst[1])
        run(instructions)
        instructions[i] = inst
