from solutions.day_12 import Day12


def test_part_1(day_12_input):
    solver = Day12(day_12_input)

    assert solver.part_1() == 25


def test_part_2(day_12_input):
    solver = Day12(day_12_input)

    assert solver.part_2() == 26
