with open('input') as f:
    inp = f.read()

def parse_input(input):
    r = {}
    for i,n in enumerate(eval('[' + input + ']')):
        r[n] = (i, None)
    return r,n,i

items,last,turn = parse_input(inp)

def add_item(num, turn):
    if num not in items:
        items[num] = (turn,None)
    else:
        prev = items[num]
        items[num] = (turn, prev[0])

def get_age(num):
    return items[num][0] - items[num][1]

while turn < 29999999:
    turn +=1
    if items[last][1] is None:
        last = 0
    else:
        last = get_age(last)
    add_item(last, turn)
    print(turn, last)
