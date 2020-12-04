from solutions.day_4 import Day4


def test_part_1(day_4_input):
    solver = Day4(day_4_input)

    assert solver.part_1() == 2


def test_part_2(day_4_input):
    solver = Day4(day_4_input)

    assert solver.part_1() == -1
