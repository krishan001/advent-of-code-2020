from common import get_input
from itertools import combinations


def sumOfAnyTwo(target, sublist):
    for i in range(0, len(sublist)):
        if target - sublist[i] in sublist[1:]:
            return True
    return False


def part1(numbers, preamble_size, valid):
    if valid:
        target = numbers[preamble_size+1]
        valid = sumOfAnyTwo(target, numbers[1: preamble_size+1])
        if not valid: 
            return valid, target
    valid, target = part1(numbers[1:], preamble_size, valid)
    if not valid:
        return valid, target


def part2(input_numbers, target):
    L = [num for num in input_numbers if num < target]
    lists = [L[i:i+j] for i in range(0,len(L)) for j in range(1,len(L) - i + 1)]
    for l in lists:
        if sum(l) == target and len(l) != 1:
            return min(l) + max(l)
