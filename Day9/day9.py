from common import get_input
"""
Refactored the code to be neater and more readable.
"""

def sumOfAnyTwo(target, sublist):
    sublist = [x for x in sublist if x < target]
    for num in sorted(sublist, reverse = True):
        if target - num in sublist:
            return True
    return False


def part1(numbers, preamble_size):
    shortened_list = numbers[preamble_size:]
    for i in range(preamble_size, len(shortened_list)):
        sublist = numbers[i - preamble_size: i]
        result = sumOfAnyTwo(numbers[i], sublist)
        if not result:
            return numbers[i]


def part2(input_numbers, target):
    for i in range(0, len(input_numbers)):
        for j in range(i+1, len(input_numbers)):
            l = input_numbers[i:j]
            if sum(l) == target:
                return min(l) + max(l)