with open("input") as f:
    input = f.read()


def parse_int(inp):
    val = int(inp[1:])
    if inp[0] == "-":
        return -1 * val
    return val


def parse_input(inp):
    instructions = []
    for l in inp.strip().split("\n"):
        ins = l[:3]
        val = parse_int(l[4:])
        instructions.append((ins, val))
    return instructions


instructions = parse_input(input)
pos = 0
visited = set()
accu = 0


def acc(val):
    global pos, accu
    accu += val
    pos += 1


def jmp(val):
    global pos
    pos += val


def nop(val):
    global pos
    pos += 1


def check_loop():
    global visited
    if pos in visited:
        print(accu)
        exit()
    visited.add(pos)


call = {"acc": acc, "jmp": jmp, "nop": nop}

while True:
    check_loop()
    ins, val = instructions[pos]
    call[ins](val)
