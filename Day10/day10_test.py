import day10
from common import get_input

test_input_data = get_input("day10_input_test.txt")
input_data = get_input("day10_input.txt")


def test_day10_part_1():
    number_list = [int(i) for i in test_input_data]
    assert day10.part1(number_list) == 220

# def test_day10_part_2():
#     number_list = [int(i) for i in test_input_data]
#     assert day10.part2(number_list) == 19208
