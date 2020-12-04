from functools import reduce
import re
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

def check_valid_data(pp):
    """
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""
    patterns = {
            'byr': r'[0-9]{4}$',
            'iyr': r'[0-9]{4}$',
            'eyr': r'[0-9]{4}$',
            'hgt': r'[0-9]{2,3}(in|cm)$',
            'hcl': r'#[a-f0-9]{6}$',
            'ecl': r'(amb|blu|brn|gry|grn|hzl|oth)$',
            'pid': r'[0-9]{9}$',
            }
    for key,patt in patterns.items():
        if re.match(patt, pp[key]) is None:
            return False
    if pp['byr'] > '2002' or pp['byr'] < '1920':
        return False
    if pp['iyr'] < '2010' or pp['iyr'] > '2020':
        return False
    if pp['eyr'] < '2020' or pp['eyr'] > '2030':
        return False
    hgt = pp['hgt']
    if 'in' in hgt:
        if hgt[:-2] < '59' or hgt[:-2] > '76':
            return False
    elif hgt[:-2] < '150' or hgt[:-2] > '193':
        return False
    return True

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
    return check_valid_data(passport)

pps = split_into_passports(input)

print(reduce(lambda x,y : x+y,map(lambda x: check_passport_valid(parse_passport(x)), pps)))
