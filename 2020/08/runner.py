class Runner:
    def __init__(self):
        self.pos = 0
        self.acc = 0
        self.visited = set()
        self.call = {"acc": self._acc, "jmp": self._jmp, "nop": self._nop}

    def _acc(self, val):
        self.acc += val
        self.pos += 1

    def _jmp(self, val):
        self.pos += val

    def _nop(self, val):
        self.pos += 1

    def _check_stop(self, len_inst):
        if self.pos == len_inst:
            return True
        if self.pos in self.visited:
            return True
        self.visited.add(self.pos)
        return False

    def run_instructions(self, instructions):
        num_inst = len(instructions)
        while not self._check_stop(num_inst):
            ins, val = instructions[self.pos]
            self.call[ins](val)
        if self.pos == num_inst:
            return True, self.acc
        return False, self.acc
