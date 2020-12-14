from solutions.day_14 import Day14


def test_part_1(day_14_input):
    solver = Day14(day_14_input)

    assert solver.part_1() == 165


def test_part_2(day_14_input_2):
    solver = Day14(day_14_input_2)

    assert solver.part_2() == 208
