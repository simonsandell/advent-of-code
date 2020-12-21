
with open('input') as f:
    inp = f.read()



def extract_paranthesis(string):
    p = 0
    cr = 1
    while cr > 0:
        p+=1
        if string[p] == ')':
            cr -= 1
        if string[p] == '(':
            cr += 1
    return string[1:p]

def evaluate_expression(string):
    string = string.strip()
    if len(string.split(' ')) == 1:
        return string
    f = string.split(' ')[0]
    if f.isnumeric():
        string = string.replace(f,'',1).strip()
    elif f[0] == '(':
        f = evaluate_expression(
                extract_paranthesis(string)
                )
        string = string.replace(
                '(' + extract_paranthesis(string) + ')',
                '',
                1
                ).strip()
    else:
        raise Exception(string)
    o = string.split(' ')[0]
    string = string.replace(o,'',1).strip()
    s = string.split(' ')[0]
    if s.isnumeric():
        ev = eval(' '.join([f,o,s]))
        return evaluate_expression(str(ev) + ' ' + string.replace(s, '' , 1).strip())
    elif s[0] == '(':
        s = evaluate_expression(
                extract_paranthesis(string)
                )
        ev = eval(' '.join([f,o,s]))
        return evaluate_expression(str(ev) + ' ' + string.replace(
            '(' + extract_paranthesis(string) + ')',
            '',
            1
            )
            )
    else:
        raise Exception(string)

sum = 0
for line in [x.strip() for x in inp.strip().split('\n')]:
    sum += int(evaluate_expression(line))
print(sum)


