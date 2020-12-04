from solutions.day_3 import Day3


def test_part_1(day_3_input):
    solver = Day3(day_3_input)

    assert solver.part_1() == 7


def test_part_2(day_3_input):
    solver = Day3(day_3_input)

    assert solver.part_2() == 336
