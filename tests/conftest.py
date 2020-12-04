import pytest


@pytest.fixture(scope="function")
def day_1_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "1721",
        "979",
        "366",
        "299",
        "675",
        "1456",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_2_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_3_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_4_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
        "",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
        "hcl:#cfa07d byr:1929",
        "",
        "hcl:#ae17e1 iyr:2013",
        "eyr:2024",
        "ecl:brn pid:760753108 byr:1931",
        "hgt:179cm",
        "",
        "hcl:#cfa07d eyr:2025 pid:166559648",
        "iyr:2011 ecl:brn hgt:59in",
    ]
    p.write_text("\n".join(content))

    return p
