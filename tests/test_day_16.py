from solutions.day_16 import Day16


def test_part_1(day_16_input):
    solver = Day16(day_16_input)

    assert solver.part_1() == 71


def test_part_2():
    solver = Day16("data/day_16.txt")

    assert solver.part_2() == 2587271823407
