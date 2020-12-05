"""
--- Day 4: Passport Processing ---
You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While
these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually
valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport
scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the same
time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required
fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value
pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm

    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929

    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm

    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in

The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt
(the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials,
not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields.
Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so
this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file,
how many passports are valid?

The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are
getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for
automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present and valid according to the above rules
"""
import re


def _is_int(n):
    try:
        _ = int(n)
        return True
    except ValueError:
        return False


class Passport(object):

    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    def __init__(self, values: dict):

        self.has_required_fields = all([field in values for field in self.required_fields])

        for i, v in values.items():
            setattr(self, i, v)

    def is_valid(self, strict=False):
        if strict and self.has_required_fields:
            # BYR
            if _is_int(self.byr) and (int(self.byr) < 1920 or int(self.byr) > 2002):
                return False

            # IYR
            if _is_int(self.iyr) and (int(self.iyr) < 2010 or int(self.iyr) > 2020):
                return False

            # EYR
            if _is_int(self.eyr) and (int(self.eyr) < 2020 or int(self.eyr) > 2030):
                return False

            # HGT
            if len(self.hgt) < 4:
                return False
            unit = self.hgt[-2:]
            hgt = self.hgt[:-2]
            if not _is_int(hgt):
                return False
            if (
                unit not in ["cm", "in"]
                or (unit == "cm" and (int(hgt) < 150 or int(hgt) > 193))
                or (unit == "in" and (int(hgt) < 59 or int(hgt) > 76))
            ):
                return False

            # HCL
            hcl_pattern = "#[0-9, a-f]{6}"
            if not re.match(hcl_pattern, self.hcl):
                return False

            # ECL
            if self.ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False

            # PID
            pid_pattern = "^[0-9]{9}$"
            if not re.match(pid_pattern, self.pid):
                return False

            return True
        else:
            return self.has_required_fields


class Day4(object):
    def __init__(self, input_file_path):
        def _parse_passport(passport_str):
            passport_str = passport_str.replace("\n", " ")
            passport_items = passport_str.split(" ")
            return {i_v.split(":")[0]: i_v.split(":")[1] for i_v in passport_items}

        with open(input_file_path, "r") as f:
            passports = f.read().strip()

        self.passports = [Passport(_parse_passport(passport)) for passport in passports.split("\n\n")]

    def part_1(self):
        return sum([passport.is_valid(strict=False) for passport in self.passports])

    def part_2(self):
        return sum([passport.is_valid(strict=True) for passport in self.passports])