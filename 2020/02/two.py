
with open('input', 'r') as f:
    input = f.read()


def parse_input(line):
    pos1,pos2 = (int(x) for x in line.split(' ')[0].split('-'))
    letter = line.split(' ')[1].split(':')[0]
    pw = line.split(':')[1].strip()
    return pos1,pos2,letter,pw

def check_rule(pos1,pos2, letter, pw):
    if (pw[pos1-1] != letter and pw[pos2-1] != letter) or (pw[pos1-1] == letter and pw[pos2-1] == letter):
        return False
    return True

count_passed = 0
lines = input.strip().split('\n')
for l in lines:
    if check_rule(*parse_input(l)):
        count_passed += 1
print(count_passed, len(lines))
