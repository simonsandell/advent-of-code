import re
from functools import reduce

with open('input') as f:
    input = f.read()

def parse_content(str):
    res = set()
    if str == 'no other bags.':
        return res
    for bags in str.replace('.', '').split(', '):
        num,desc,col,_ = bags.split(' ')
        res.add(desc + ' ' + col)
    return res

def parse_input(input):
    rules = dict()
    for line in input.strip().split('\n'):
        key,rest = line.split(' bags contain ')
        val = parse_content(rest)
        rules[key] = val
    return rules

rules = parse_input(input)

def check_color_contains_color(parent, seeked):
    if len(rules[parent]) == 0:
        return False
    if seeked in rules[parent]:
        return True
    for ch in rules[parent]:
        if check_color_contains_color(ch, seeked):
            return True
    return False
print(reduce(lambda x,y: x+y, map(lambda x: check_color_contains_color(x, 'shiny gold'), rules.keys())))
