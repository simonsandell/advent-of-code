from functools import reduce

with open("input") as f:
    input = f.read()


def split_into_groups(input):
    return [x.strip() for x in input.split("\n\n")]


def stack_answers(group):
    answers = set()
    for l in [x.strip() for x in group.split("\n")]:
        for c in l:
            answers.add(c)
    return answers


groups = split_into_groups(input)

print(
    reduce(
        lambda x, y: x + y,
        map(lambda x: len(stack_answers(x)), split_into_groups(input)),
    )
)
