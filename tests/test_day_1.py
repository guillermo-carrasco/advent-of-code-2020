import random

from solutions.day_1 import Day1


def test_part_1(day_1_input):
    solver = Day1(day_1_input)

    assert solver.part_1(2020) == 514579


def test_part_2(day_1_input):
    solver = Day1(day_1_input)

    assert solver.part_2(2020) == 241861950


def generate_test_case(length, max_int):
    numbers = list(range(2021))
    i = 0
    j = len(numbers) - 1
    possible_pairs = []
    while i <= j:
        possible_pairs.append((numbers[i], numbers[j]))
        i += 1
        j -= 1

    a, b = possible_pairs[random.randint(0, len(possible_pairs) - 1)]
    test_case = [a, b]
    for _ in range(length - 2):
        n = random.randint(0, max_int)
        while n == a or n == b:
            n = random.randint(0, max_int)
        test_case.append(n)

    with open('test.txt', 'w') as f:
        f.writelines([str(n) + '\n' for n in test_case])
