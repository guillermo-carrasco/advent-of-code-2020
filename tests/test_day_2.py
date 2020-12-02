from solutions.day_2 import Day2


def test_part_1(day_2_input):
    solver = Day2(day_2_input)

    assert solver.part_1() == 2


def test_part_2(day_2_input):
    solver = Day2(day_2_input)

    assert solver.part_2() == 1
