from seatings import Seatings

with open("input") as f:
    input = f.read()

seatings = Seatings()
seatings.parse_input(input)

while seatings.update():
    pass
print(seatings)
print(seatings.count_occupied())
