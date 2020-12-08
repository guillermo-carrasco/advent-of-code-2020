from solutions.day_8 import Day8


def test_part_1(day_8_input):
    solver = Day8(day_8_input)

    assert solver.part_1() == 5


def test_part_2(day_8_input):

    solver = Day8(day_8_input)
    assert solver.part_2() == 8
