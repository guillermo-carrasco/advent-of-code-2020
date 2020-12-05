from solutions.day_5 import Day5


def test_part_1(day_5_input):
    solver = Day5(day_5_input)

    assert solver.part_1() == 820


def test_part_2():
    solver = Day5("data/day_5.txt")

    assert solver.part_2() == 711
