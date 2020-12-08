from common import get_input

def get_split_instructions(instructions):
    split_instructions = []
    for line in instructions:
        split_line = line.split(" ")
        split_instructions.append([split_line[0], split_line[1][:1], int(split_line[1][1:])])
    return split_instructions


def change_acc(acc, sign, number):
    if sign == "+": 
        acc += number 
    elif sign == "-":
        acc -= number
    return acc


def get_jmp(i, sign, number):
    if sign == "+":
        i += number
    if sign == "-":
        i-= number
    return i


def swap_jmp_nop(instructions, i, initial, new_value):
        instructions[i][0] = instructions[i][0].replace(initial, new_value)
        corrupted, acc = part_1(instructions)
        return corrupted, acc


def part_1(instructions):
    acc = 0
    visited = []
    i = 0
    while i < len(instructions):
        if i in visited:
            return True, acc
        else:
            visited.append(i)
        if instructions[i][0] == "acc":
            acc = change_acc(acc, instructions[i][1], instructions[i][2])
        if instructions[i][0] == "jmp":
            i = get_jmp(i, instructions[i][1], instructions[i][2])
        else:
            i += 1
    return False, acc


def part_2(instructions):
    visited = []
    new, initial = "", ""
    corrupted = True
    for i in range(0, len(instructions)):
        if instructions[i][0] == "jmp" and i not in visited:
            initial = "jmp"
            new = "nop"
            corrupted, acc = swap_jmp_nop(instructions, i, initial, new)
        elif instructions[i][0] == "nop" and i not in visited:
            initial = "nop"
            new = "jmp"
            corrupted, acc = swap_jmp_nop(instructions, i, initial, new)

        if  corrupted == False:
            return acc
        
        instructions[i][0] = instructions[i][0].replace(new, initial)
        visited.append(i)

    return None


def main():
    data = get_input("day8_input.txt")
    split_instructions = (get_split_instructions(data))
    print(part_1(split_instructions))
    print(part_2(split_instructions))

if __name__ == "__main__":
    main()