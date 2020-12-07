from solutions.day_7 import Day7


def test_part_1(day_7_input):
    solver = Day7(day_7_input)

    assert solver.part_1() == 4


def test_part_2(day_7_input):

    solver = Day7(day_7_input)
    assert solver.part_2() == 32


def test_part_2_2(day_7_input_2):
    solver = Day7(day_7_input_2)
    assert solver.part_2() == 126
