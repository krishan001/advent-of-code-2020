import math


def get_input():
    with open("inputs/day5_input.txt") as f:
        data = f.read().splitlines()
    return data


def getHighestBoardingPass(data):
    highest = 0
    all_ids = []
    for boardingPass in data:
        seatID = calcSeatID(boardingPass)
        all_ids.append(seatID)
        if seatID > highest:
            highest = seatID
    return all_ids, highest


def findSeat(ids, highest):
    for i in range(0, highest):
        if i not in ids and i + 1 in ids and i - 1 in ids:
            return i


def calcSeatID(line):
    row = line[:7]
    col = line[7:]
    row_num = calc_num(row, "F", "B", 127)
    col_num = calc_num(col, "L", "R", 7)
    return (row_num * 8) + col_num 


def calc_num(line, upper_char, lower_char, top_index):
    bottom_index = 0
    for c in line:
        if (c == upper_char):
            top_index = int(top_index/2) + int(bottom_index/2)
        if c == lower_char:
            temp = top_index
            bottom_index = math.ceil(temp/2) + int(bottom_index/2)
    return top_index


def main():
    data = get_input()
    all_ids, highest = getHighestBoardingPass(data)
    print(findSeat(all_ids, highest))


if __name__ == "__main__":
    main()