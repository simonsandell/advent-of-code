import requests
import sys
import datetime
import subprocess
rootpath = subprocess.run(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE).stdout.decode().strip()
year = datetime.datetime.now().year

with open('.secret', 'r') as f:
    secret = f.read().strip()
headers = {'Cookie': secret}
input = requests.get(
        f'https://adventofcode.com/{year}/day/{int(sys.argv[1])}/input',
        headers=headers
        ).text
with open(f'{rootpath}/{year}/{sys.argv[1]}/input', 'w') as f:
    f.write(input)
