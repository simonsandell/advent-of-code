from copy import deepcopy

class Seatings:

    def __str__(self):
        s = ''
        for i in range(self.height):
            for j in range(self.width):
                s += self.seats[(i,j)]
            s += '\n'
        return s

    def __init__(self):
        self.seats = None
        self.width = None
        self.height = None

    def parse_input(self, input):
        self.seats = {}
        self.height = len(input.strip().split('\n')) 
        self.width = len(input.split('\n')[0])
        for i,l in enumerate([x.strip() for x in input.strip().split('\n')]):
            for j,c in enumerate(list(l)):
                self.seats[(i,j)] = c

    def count_occupied(self):
        c = 0
        for v in self.seats.values():
            if v == '#':
                c += 1
        return c

    def _add(tup, tup2):
        return tuple(map(sum, zip(tup,tup2)))

    def get_adjacent(self, pos):
        diffs = {
                (0, -1),
                (0, +1),
                (-1, -1),
                (+1, +1),
                (+1, -1),
                (-1, +1),
                (-1, 0),
                (+1, 0),
                }
        res = set()
        for diff in diffs:
            if Seatings._add(diff, pos) not in self.seats.keys():
                continue
            if self.seats[Seatings._add(pos,diff)] != '.':
                res.add(Seatings._add(pos, diff))
            else:
                ddiff = (diff[0], diff[1])
                while True:
                    ddiff = Seatings._add(diff, ddiff)
                    if Seatings._add(pos, ddiff) not in self.seats.keys():
                        break
                    if self.seats[Seatings._add(pos, ddiff)] != '.':
                        res.add(Seatings._add(pos, ddiff))
                        break
        return res

    def check_rule_one(self, pos):
        if self.seats[pos] != 'L':
            return False
        for adj in self.get_adjacent(pos):
            if self.seats[adj] == '#':
                return False
        return True

    def check_rule_two(self, pos):
        if self.seats[pos] != '#':
            return False
        c = 0
        for adj in self.get_adjacent(pos):
            if self.seats[adj] == '#':
                c += 1
        if c >= 5:
            return True
        return False

    def update(self):
        new_state = deepcopy(self.seats)
        for i in range(self.height):
            for j in range(self.width):
                if self.check_rule_one((i,j)):
                    new_state[(i,j)] = '#'
                if self.check_rule_two((i,j)):
                    new_state[(i,j)] = 'L'
        if self.seats == new_state:
            return False
        self.seats = new_state
        return True
