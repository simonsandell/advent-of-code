from functools import reduce
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
    if len(string.split(' ')) == 3:
        return str(eval(string))
    if '(' in string:
        par_expr = extract_paranthesis(string[string.index('('):])
        par_val = evaluate_expression(par_expr)
        return evaluate_expression(string.replace('(' + par_expr + ')', par_val))
    if '+' not in string or  '*' not in string:
        return str(eval(string))
    else:
        terms = string.split(' * ')
        first = terms[0]
        rest = ' * '.join(terms[1:])
        return str(int(evaluate_expression(terms[0])) * int(evaluate_expression(rest)))

sum = 0
for line in [x.strip() for x in inp.strip().split('\n')]:
    sum += int(evaluate_expression(line))
print(sum)


