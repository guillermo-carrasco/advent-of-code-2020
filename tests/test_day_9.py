from solutions.day_9 import Day9


def test_part_1(day_9_input):
    solver = Day9(day_9_input)

    assert solver.part_1(preamble=5) == 127


def test_part_2(day_8_input):

    solver = Day9(day_8_input)
    assert solver.part_2() == 62
