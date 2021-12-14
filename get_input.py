#!/usr/bin/env python
import sys, os, datetime, subprocess, shutil
import requests

rootpath = (
    subprocess.run(["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE)
    .stdout.decode()
    .strip()
)
year = sys.argv[1] if len(sys.argv) > 1 else datetime.datetime.now().year
day = sys.argv[2] if len(sys.argv) > 2 else datetime.datetime.now().day

with open(".secret", "r") as f:
    secret = f.read().strip()
headers = {"Cookie": secret}
input = requests.get(
    f"https://adventofcode.com/{year}/day/{day}/input", headers=headers
).text
path = f"{rootpath}/{year}/{day}/"
os.makedirs(path, exist_ok=True)
with open(path + "input", "w") as f:
    f.write(input)
shutil.copyfile("template.py", path + "1.py")
