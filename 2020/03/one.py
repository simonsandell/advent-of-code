
with open('input') as f:
    input = f.read()

forest = []
for l in input.strip().split('\n'):
    forest.append(list(l))
height = len(forest)
width = len(forest[0])


def check_if_pos_tree(right, down):
    if forest[down][right % width] == '#':
        return True
    return False

my_pos = [0,0]
tree_count = 0
for i in range(height - 1):
    my_pos[0] = my_pos[0] + 3
    my_pos[1] = my_pos[1] + 1
    if check_if_pos_tree(my_pos[0], my_pos[1]):
        tree_count +=1
print(tree_count)

