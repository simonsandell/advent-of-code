import one

input = """ecl:amb
pid:690616023
byr:1994 iyr:2014 hgt:172cm hcl:#c0946f eyr:2022

eyr:1980 cid:97
hcl:z ecl:#102145 iyr:2011 byr:1945
pid:187cm hgt:179in

ecl:amb
iyr:2011
cid:113
eyr:2021 hcl:#b6652a pid:004682943 byr:1940
hgt:173cm"""


def test_split():
    assert len(one.split_into_passports(input)) == 3


def test_parse():
    assert (
        one.parse_passport(
            """pid:69
byr:1994 iyr:2014 hgt:172cm hcl:#c0946f eyr:2022"""
        )
        == {
            "pid": "69",
            "byr": "1994",
            "iyr": "2014",
            "hgt": "172cm",
            "hcl": "#c0946f",
            "eyr": "2022",
        }
    )


def test_check():
    sp = one.split_into_passports(input)
    parsed = [one.parse_passport(x) for x in sp]

    assert one.check_passport_valid(parsed[0])
    assert one.check_passport_valid(parsed[1])
    assert one.check_passport_valid(parsed[2])
