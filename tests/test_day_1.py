from solutions.day_1 import Day1


def test_part_1(day_1_input):
    solver = Day1(day_1_input)

    assert solver.part_1(2020) == 514579


def test_part_2(day_1_input):
    solver = Day1(day_1_input)

    assert solver.part_2(2020) == 241861950
