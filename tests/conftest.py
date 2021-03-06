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


@pytest.fixture(scope="function")
def day_4_valid_passports(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
        "hcl:#623a2f",
        "",
        "eyr:2029 ecl:blu cid:129 byr:1989",
        "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
        "",
        "hcl:#888785",
        "hgt:164cm byr:2001 iyr:2015 cid:88",
        "pid:545766238 ecl:hzl",
        "eyr:2022",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_4_invalid_passports(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "eyr:1972 cid:100" "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
        "",
        "iyr:2019",
        "hcl:#602927 eyr:1967 hgt:170cm",
        "ecl:grn pid:012533040 byr:1946",
        "",
        "hcl:dab227 iyr:2012",
        "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
        "",
        "hgt:59cm ecl:zzz",
        "eyr:2038 hcl:74454a iyr:2023",
        "pid:3556412378 byr:2007",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_5_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "FBFBBFFRLR",
        "BFFFBBFRRR",
        "FFFBBBFRRR",
        "BBFFBBFRLL",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_6_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "abc",
        "",
        "a",
        "b",
        "c",
        "",
        "ab",
        "ac",
        "",
        "a",
        "a",
        "a",
        "a",
        "",
        "b",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_7_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "light red bags contain 1 bright white bag, 2 muted yellow bags.",
        "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
        "bright white bags contain 1 shiny gold bag.",
        "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
        "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
        "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
        "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
        "faded blue bags contain no other bags.",
        "dotted black bags contain no other bags.",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_7_input_2(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "shiny gold bags contain 2 dark red bags.",
        "dark red bags contain 2 dark orange bags.",
        "dark orange bags contain 2 dark yellow bags.",
        "dark yellow bags contain 2 dark green bags.",
        "dark green bags contain 2 dark blue bags.",
        "dark blue bags contain 2 dark violet bags.",
        "dark violet bags contain no other bags.",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_8_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_9_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "35",
        "20",
        "15",
        "25",
        "47",
        "40",
        "62",
        "55",
        "65",
        "95",
        "102",
        "117",
        "150",
        "182",
        "127",
        "219",
        "299",
        "277",
        "309",
        "576",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_10_input_1(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "16",
        "10",
        "15",
        "5",
        "1",
        "11",
        "7",
        "19",
        "6",
        "12",
        "4",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_10_input_2(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "28",
        "33",
        "18",
        "42",
        "31",
        "14",
        "46",
        "20",
        "48",
        "47",
        "24",
        "23",
        "49",
        "45",
        "19",
        "38",
        "39",
        "11",
        "1",
        "32",
        "25",
        "35",
        "8",
        "17",
        "7",
        "9",
        "4",
        "2",
        "34",
        "10",
        "3",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_11_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_12_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "F10",
        "N3",
        "F7",
        "R90",
        "F11",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_13_input(tmp_path):
    p = tmp_path / "input.txt"
    content = ["939", "7,13,x,x,59,x,31,19"]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_14_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_14_input_2(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "mask = 000000000000000000000000000000X1001X",
        "mem[42] = 100",
        "mask = 00000000000000000000000000000000X0XX",
        "mem[26] = 1",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_15_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "8,0,17,4,1,12",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_16_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "class: 1-3 or 5-7",
        "row: 6-11 or 33-44",
        "seat: 13-40 or 45-50",
        "",
        "your ticket:",
        "7, 1, 14",
        "",
        "nearby tickets:",
        "7,3,47",
        "40,4,50",
        "55,2,20",
        "38,6,12",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_16_input_2(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        "class: 0-1 or 4-19",
        "row: 0-5 or 8-19",
        "seat: 0-13 or 16-19",
        "",
        "your ticket:",
        "11,12,13",
        "",
        "nearby tickets:",
        "3,9,18",
        "15,1,5",
        "5,14,9",
    ]
    p.write_text("\n".join(content))

    return p


@pytest.fixture(scope="function")
def day_17_input(tmp_path):
    p = tmp_path / "input.txt"
    content = [
        ".#.",
        "..#",
        "###",
    ]
    p.write_text("\n".join(content))

    return p
