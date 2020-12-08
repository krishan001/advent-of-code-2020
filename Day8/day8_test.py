import day8
from common import get_input
input_data = get_input("day8_input_test.txt")
def test_day8_part_1():
    global input_data
    part_1_input_data = day8.get_split_instructions(input_data)
    assert day8.part_1(part_1_input_data) == (True, 5)

def test_day8_part_2():
    global input_data
    part_2_input_data = day8.get_split_instructions(input_data)
    assert day8.part_2(part_2_input_data) == 8
