import two

def test_check_valid_data():
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
    valid_max = {
            'byr': '2002',
            'iyr': '2020',
            'eyr': '2030',
            'hgt': '193cm',
            'hcl': '#1a1a1a',
            'ecl': 'oth',
            'pid': '000000000',
            }
    assert two.check_valid_data(valid_max)
    valid_min = {
            'byr': '1920',
            'iyr': '2010',
            'eyr': '2020',
            'hgt': '59in',
            'hcl': '#1a1a1a',
            'ecl': 'amb',
            'pid': '999999999',
            }
    assert two.check_valid_data(valid_min)

