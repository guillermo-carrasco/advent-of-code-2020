from solutions.day_13 import Day13


def test_part_1(day_13_input):
    solver = Day13(day_13_input)

    assert solver.part_1() == 295


def test_part_2(day_13_input):
    solver = Day13(day_13_input)

    assert solver.part_2() == 1068781
