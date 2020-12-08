import re

def get_info(line):
    parts = line.split(" ")
    minNum = int(parts[0].split("-")[0])
    maxNum = int(parts[0].split("-")[1])
    target = parts[1].split(":")[0]
    password = parts[2]
    return minNum, maxNum, target, password


def get_total_number():
    total = 0
    with open("inputs/day2_inputs.txt") as f:
        for line in f:
            minNum, maxNum, target, password = get_info(line)
            count = len(re.findall(target,password))
            if minNum <= count <= maxNum:
                total += 1
    return total


def get_positions():
    total = 0
    with open("inputs/day2_inputs.txt") as f:
        for line in f:
            minNum, maxNum, target, password = get_info(line)
            if (password[minNum-1] == target) != (password[maxNum - 1] == target):
                total += 1
    return total


if __name__ == "__main__":
    print("Total Number: ", get_total_number())
    print("In one position: ", get_positions())