
def get_input():
    with open("inputs/day3_input.txt") as f:
        data = f.read().splitlines()
    return data
    

def get_num_trees(right, down):
    terrain = get_input()
    width = len(terrain[0])
    index = 0
    trees = 0
    for i in range(0, len(terrain), down):
        if terrain[i][index] == "#":
             trees += 1
        index += right 
        index = index % width
    return trees


def get_num_trees_part_2():
    total = 1
    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    for i in slopes:
        total *= get_num_trees(i[0], i[1])
    return total
    

print(get_num_trees_part_2())