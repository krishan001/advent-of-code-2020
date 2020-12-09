import day9
from common import get_input

test_input_data = get_input("day9_input_test.txt")
input_data = get_input("day9_input.txt")


def test_day9_part_1():
    number_list = [int(i) for i in input_data]
    test_number_list = [int(i) for i in test_input_data]
    assert day9.part1(test_number_list, 5, True) == (False, 127)
    assert day9.part1(number_list, 25, True) == (False, 1124361034)

def test_day9_part_2():
    number_list = [int(i) for i in input_data]
    test_number_list = [int(i) for i in test_input_data]
    assert day9.part2(test_number_list, 127) == 62
    assert day9.part2(number_list, 1124361034) == 129444555
