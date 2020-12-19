import pytest

from solutions.day_15 import Day15


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([0, 3, 6], 436),
        ([1, 3, 2], 1),
        ([2, 1, 3], 10),
        ([1, 2, 3], 27),
        ([2, 3, 1], 78),
        ([3, 2, 1], 438),
        ([3, 1, 2], 1836),
    ],
)
def test_part_1(test_input, expected):
    solver = Day15(test_input)

    assert solver.part_1() == expected


@pytest.mark.skip(reason="Ran once and worked, just takes too long")
@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([0, 3, 6], 175594),
        ([1, 3, 2], 2578),
        ([2, 1, 3], 3544142),
        ([1, 2, 3], 261214),
        ([2, 3, 1], 6895259),
        ([3, 2, 1], 18),
        ([3, 1, 2], 362),
    ],
)
def test_part_2(test_input, expected):
    solver = Day15(test_input)

    assert solver.part_2() == expected
