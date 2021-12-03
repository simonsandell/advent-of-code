from functools import reduce

with open("input") as f:
    input = f.read()

forest = []
for l in input.strip().split("\n"):
    forest.append(list(l))
height = len(forest)
width = len(forest[0])


def check_if_pos_tree(right, down):
    if forest[down][right % width] == "#":
        return True
    return False


def get_treecount(slope):
    right, down = slope
    my_pos = [0, 0]
    tree_count = 0
    while my_pos[1] < height - 1:
        my_pos[0] = my_pos[0] + right
        my_pos[1] = my_pos[1] + down
        if check_if_pos_tree(my_pos[0], my_pos[1]):
            tree_count += 1
    return tree_count


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print(reduce(lambda x, y: x * y, map(get_treecount, slopes)))
