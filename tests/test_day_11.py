from solutions.day_11 import Day11


def test_part_1(day_11_input):
    solver = Day11(day_11_input)

    assert solver.part_1() == 37
