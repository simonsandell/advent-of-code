#!/usr/bin/env python
import sys
from collections import deque

infile = sys.argv[1] if len(sys.argv) > 1 else "input"

# start, rest = open(infile).read().split('\n\n')
# for l in rest.strip().split('\n'):
with open(infile) as f:
    lines = f.read().strip().split("\n")


class Node:
    def __init__(self, name, size, parent=None):
        self.name = name
        self.size = size
        self.children = {}
        self.parent = parent

    def add_child(self, node):
        self.children[node.name] = node

    def set_parent(self, node):
        self.parent = node


root = Node("/", 0)
current_node = None
for l in lines:
    cmd = l[:4]
    if cmd == "$ cd":
        target = l.split(" ")[2]
        if target == "..":
            current_node = current_node.parent
        elif target == "/":
            current_node = root
        else:
            current_node = current_node.children[target]
    elif cmd == "$ ls":
        continue
    elif cmd == "dir ":
        name = l.split(" ")[1]
        current_node.add_child(Node(name, 0, current_node))
    else:
        size, name = l.split(" ")
        current_node.add_child(Node(name, int(size), current_node))


def compute_size(node):
    if node.size == 0:
        s = 0
        for c in node.children.keys():
            s += compute_size(node.children[c])
        return s
    return node.size


dirs = deque()
dirs.append(root)
size_sum = 0
while dirs:
    d = dirs.popleft()
    s = 0
    for c in d.children.keys():
        if d.children[c].size == 0:
            dirs.append(d.children[c])
        s += compute_size(d.children[c])
    if s <= 100000:
        size_sum += s
print(size_sum)
