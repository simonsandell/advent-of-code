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
        res.add((int(num),desc + ' ' + col))
    return res

def parse_input(input):
    rules = dict()
    for line in input.strip().split('\n'):
        key,rest = line.split(' bags contain ')
        val = parse_content(rest)
        rules[key] = val
    return rules

rules = parse_input(input)

def count_bags_inside(color, rules=rules):
    if len(rules[color]) == 0:
        return 0
    sum = 0
    for factor,ch in rules[color]:
        sum += factor*(1 + count_bags_inside(ch))
    return sum

print(count_bags_inside('shiny gold'))
