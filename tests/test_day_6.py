from solutions.day_6 import Day6


def test_part_1(day_6_input):
    solver = Day6(day_6_input)

    assert solver.part_1() == 11


def test_part_2(day_6_input):
    solver = Day6(day_6_input)

    assert solver.part_2() == 6
