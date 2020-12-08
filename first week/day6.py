from collections import Counter
from common import read_data_blank_line_separator as read_data


def get_total(answers):
    total = 0
    for group in answers:
        total += len(group)
    return total


def get_total_part_2(answers):
    total = 0
    for group in answers:
        for c in Counter(group):
            if Counter(group)[c] == len(group.split(" ")):
                total += 1
    return total


def get_set(answers):
    lst = []
    for group in answers:
        lst.append("".join(set(group)).replace(" ", ""))
    return lst


def main():
    answers = read_data("inputs/day6_input.txt")
    answers = get_set(answers)
    new_answers = read_data("inputs/day6_input.txt")
    print(get_total(answers))
    print(get_total_part_2(new_answers))


if __name__ == "__main__":
    main()
