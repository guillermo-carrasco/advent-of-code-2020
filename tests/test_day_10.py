from solutions.day_10 import Day10


def test_part_1_1(day_10_input_1):
    solver = Day10(day_10_input_1)

    assert solver.part_1() == 35


def test_part_1_2(day_10_input_2):
    solver = Day10(day_10_input_2)

    assert solver.part_1() == 220


def test_part_2_1(day_10_input_1):

    solver = Day10(day_10_input_1)
    assert solver.part_2() == 8


def test_part_2_2(day_10_input_2):

    solver = Day10(day_10_input_2)
    assert solver.part_2() == 19208
