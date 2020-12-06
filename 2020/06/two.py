from functools import reduce
with open('input') as f:
    input = f.read()

def split_into_groups(input):
    return [x.strip() for x in input.split('\n\n')]

def stack_answers(group):
    answers = list()
    full_answers = set()
    num_persons = 0
    for l in [x.strip() for x in group.split('\n')]:
        num_persons +=1
        for c in l:
            answers.append(c)
    for ans in answers:
        if answers.count(ans) == num_persons:
            full_answers.add(ans)
    return full_answers

groups = split_into_groups(input)

print(reduce(lambda x,y: x+y, map(lambda x: len(stack_answers(x)), split_into_groups(input))))
