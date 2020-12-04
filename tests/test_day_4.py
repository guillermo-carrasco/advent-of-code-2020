from solutions.day_4 import Day4


def test_part_1(day_4_input):
    solver = Day4(day_4_input)

    assert solver.part_1() == 2


def test_part_2_invalid(day_4_invalid_passports):
    solver = Day4(day_4_invalid_passports)

    assert solver.part_2() == 0


def test_part_2_valid(day_4_valid_passports):
    solver = Day4(day_4_valid_passports)

    assert solver.part_2() == 4
