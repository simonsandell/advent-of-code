import requests
import sys

with open('.secret', 'r') as f:
    secret = f.read().strip()
headers = {'Cookie': secret}
input = requests.get(
        f'https://adventofcode.com/2020/day/{int(sys.argv[1])}/input',
        headers=headers
        ).text
with open(f'./{sys.argv[1]}/input', 'w') as f:
    f.write(input)
