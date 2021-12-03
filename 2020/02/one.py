with open("input", "r") as f:
    input = f.read()


def parse_input(line):
    min, max = (int(x) for x in line.split(" ")[0].split("-"))
    letter = line.split(" ")[1].split(":")[0]
    pw = line.split(":")[1].strip()
    return min, max, letter, pw


def check_rule(min, max, letter, pw):
    c = pw.count(letter)
    if c < min or c > max:
        return False
    return True


count_passed = 0
for l in input.strip().split("\n"):
    if check_rule(*parse_input(l)):
        count_passed += 1
print(count_passed)
