from functools import reduce
with open('input') as f:
    input = f.read()

def split_into_passports(input):
    return [x.strip() for x in input.split('\n\n')]

def parse_passport(passport):
    parsed = {}
    lines = passport.split('\n')
    for l in lines:
        kvpairs = l.split(' ')
        for kv in kvpairs:
            k,v = kv.split(':')
            parsed[k] = v
    return parsed

def check_passport_valid(passport):
    required_keys = [
            'byr',
            'iyr',
            'eyr',
            'hgt',
            'hcl',
            'ecl',
            'pid',
            ]
    optional_keys = ['cid']
    for k in required_keys:
        if k not in passport.keys():
            return False
    return True

pps = split_into_passports(input)

print(reduce(lambda x,y : x+y,map(lambda x: check_passport_valid(parse_passport(x)), pps)))
