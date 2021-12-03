from copy import deepcopy


class Seatings:
    def __str__(self):
        s = ""
        for i in range(self.height):
            for j in range(self.width):
                s += self.seats[(i, j)]
            s += "\n"
        return s

    def __init__(self):
        self.seats = None
        self.width = None
        self.height = None

    def parse_input(self, input):
        self.seats = {}
        self.height = len(input.strip().split("\n"))
        self.width = len(input.split("\n")[0])
        for i, l in enumerate([x.strip() for x in input.strip().split("\n")]):
            for j, c in enumerate(list(l)):
                self.seats[(i, j)] = c

    def count_occupied(self):
        c = 0
        for v in self.seats.values():
            if v == "#":
                c += 1
        return c

    def get_adjacent(self, pos):
        res = {
            (pos[0], pos[1] - 1),
            (pos[0], pos[1] + 1),
            (pos[0] - 1, pos[1] - 1),
            (pos[0] + 1, pos[1] + 1),
            (pos[0] + 1, pos[1] - 1),
            (pos[0] - 1, pos[1] + 1),
            (pos[0] - 1, pos[1]),
            (pos[0] + 1, pos[1]),
        }
        if pos[0] == 0:
            res.discard((pos[0] - 1, pos[1] + 1))
            res.discard((pos[0] - 1, pos[1]))
            res.discard((pos[0] - 1, pos[1] - 1))
        if pos[0] == self.height - 1:
            res.discard((pos[0] + 1, pos[1] + 1))
            res.discard((pos[0] + 1, pos[1] - 1))
            res.discard((pos[0] + 1, pos[1]))
        if pos[1] == 0:
            res.discard((pos[0] - 1, pos[1] - 1))
            res.discard((pos[0] + 1, pos[1] - 1))
            res.discard((pos[0], pos[1] - 1))
        if pos[1] == self.width - 1:
            res.discard((pos[0] - 1, pos[1] + 1))
            res.discard((pos[0] + 1, pos[1] + 1))
            res.discard((pos[0], pos[1] + 1))
        return res

    def check_rule_one(self, pos):
        if self.seats[pos] != "L":
            return False
        for adj in self.get_adjacent(pos):
            if self.seats[adj] == "#":
                return False
        return True

    def check_rule_two(self, pos):
        if self.seats[pos] != "#":
            return False
        c = 0
        for adj in self.get_adjacent(pos):
            if self.seats[adj] == "#":
                c += 1
        if c >= 4:
            return True
        return False

    def update(self):
        new_state = deepcopy(self.seats)
        for i in range(self.height):
            for j in range(self.width):
                if self.check_rule_one((i, j)):
                    new_state[(i, j)] = "#"
                if self.check_rule_two((i, j)):
                    new_state[(i, j)] = "L"
        if self.seats == new_state:
            return False
        self.seats = new_state
        return True
