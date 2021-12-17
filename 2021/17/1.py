#!/usr/bin/env python
import sys
from math import copysign

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

xr, yr = open(infile).read().strip().replace("target area: ", "").split(", ")
xrange = [int(x) for x in xr.split("=")[1].split("..")]
yrange = [int(y) for y in yr.split("=")[1].split("..")]


class State:
    def __init__(self):
        self.x = None
        self.y = None
        self.xv = None
        self.yv = None
        self.target_xmin = None
        self.target_xmax = None
        self.target_ymin = None
        self.target_ymax = None

    def step(self):
        self.x += self.xv
        if self.xv != 0:
            self.xv = copysign(abs(self.xv) - 1, self.xv)
        self.y += self.yv
        self.yv -= 1

    def get_target_dist(self):
        xdist = 0
        ydist = 0
        if self.x < self.target_xmin:
            xdist = self.target_xmin - self.x
        elif self.x > self.target_xmax:
            xdist = self.target_xmax - self.x
        if self.y < self.target_ymin:
            ydist = self.target_ymin - self.y
        elif self.y > self.target_ymax:
            ydist = self.target_ymax - self.y
        return xdist, ydist

    def find_x_velocities(self):
        vels = []
        for v in range(0, self.target_xmax + 2):
            self.x = 0
            self.y = 0
            self.xv = v
            self.yv = 0
            hit = False
            steps = 0
            while True:
                steps += 1
                self.step()
                xdist, _ = self.get_target_dist()
                if xdist == 0:
                    hit = True
                if self.xv <= 0:
                    break
                if xdist < 0:
                    break
            if hit:
                vels.append((v, steps))
        return vels

    def simulate(self, xv, yv):
        max_h = 0
        self.x = 0
        self.y = 0
        self.xv = xv
        self.yv = yv
        hit = False
        steps = 0
        while not hit:
            steps += 1
            self.step()
            max_h = max(self.y, max_h)
            xd, yd = self.get_target_dist()
            if not xd and not yd:
                hit = True
            if xd < 0 or yd > 0:
                break
        if hit:
            return max_h, steps
        return 0, steps


state = State()
state.target_xmin = xrange[0]
state.target_xmax = xrange[1]
state.target_ymin = yrange[0]
state.target_ymax = yrange[1]
xvels = state.find_x_velocities()

max_heights = []
for xv, maxsteps in xvels:
    for yv in range(0, 100):
        maxh, steps = state.simulate(xv, yv)
        max_heights.append(maxh)


print(max(max_heights))
