import hashlib

with open("input") as f:
    secret = f.read().strip()


def check(secret, n):
    if n:
        v = secret + str(n)
    else:
        v = secret
    return hashlib.md5(v.encode("utf-8")).hexdigest()[:6] == "000000"


n = 0
while not check(secret, n):
    n += 1
print(n)
