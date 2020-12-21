"""
--- Day 16: Ticket Translation ---

As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is
on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should
probably figure out what it says before you get to the train station after the next flight.

Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure
out the fields these tickets must have and the valid ranges for values in those fields.

You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the
same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).

The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values
for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is named class

and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).

Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the
order they appear; every ticket has the same format. For example, consider this ticket:

.--------------------------------------------------------.
| ????: 101    ?????: 102   ??????????: 103     ???: 104 |
|                                                        |
| ??: 301  ??: 302             ???????: 303      ??????? |
| ??: 401  ??: 402           ???? ????: 403    ????????? |
'--------------------------------------------------------'

Here, ? represents text in a language you don't understand. This ticket might be represented as
101,102,103,104,301,302,303,401,402,403; of course, the actual train tickets you're looking at are much more complicated.
In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the
second number is always a different specific field, and so on - you just don't know what each position actually means!

Start by determining which tickets are completely invalid; these are tickets that contain values which aren't valid for
any field. Ignore your ticket for now.

For example, suppose you have the following notes:

class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12

It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets by considering
only whether tickets contain values that are not valid for any field. In this example, the values on the first nearby
ticket are all valid for at least one field. This is not true of the other three nearby tickets: the values 4, 55, and
12 are are not valid for any field. Adding together all of the invalid values produces your ticket scanning error
rate: 4 + 55 + 12 = 71.

Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?
"""
from collections import defaultdict


class Day16(object):
    def __init__(self, input_file_path):
        with open(input_file_path, "r") as f:
            ticket_rules, your_ticket, nearby_tickets = f.read().split("\n\n")

        def _parse_ranges(range_str):
            low, high = range_str.split("-")
            return set(range(int(low), int(high) + 1))

        self.rule_ranges = defaultdict(lambda: set())
        for rule_ranges in ticket_rules.split("\n"):
            rule, ranges = rule_ranges.split(": ")
            for _range in ranges.split(" or "):
                self.rule_ranges[rule].update(_parse_ranges(_range))

        self.your_ticket = [int(n) for n in your_ticket.split("\n")[1].split(",")]

        self.nearby_tikets = []
        for ticket in nearby_tickets.split("\n")[1:]:
            self.nearby_tikets.append([int(n) for n in ticket.split(",")])

    def part_1(self):
        allowed_values = {v for _range in self.rule_ranges.values() for v in _range}
        error_rate = 0
        for ticket in self.nearby_tikets:
            for value in ticket:
                if value not in allowed_values:
                    error_rate += value
        return error_rate

    def part_2(self):
        # Figure out the order in the tickets for every rule
        valid_tickets = [self.your_ticket]
        allowed_values = {v for _range in self.rule_ranges.values() for v in _range}
        for ticket in self.nearby_tikets:
            if allowed_values.issuperset(ticket):
                valid_tickets.append(ticket)

        rule_order = {}

        # For each valid ticket, check if the value at index i fits in the ranges for a rule. If they all fit,
        # this i will be the order of the rule
        matched = {r: False for r in set(self.rule_ranges.keys())}
        while not all(matched.values()):
            for i, tickets_row in enumerate(zip(*valid_tickets)):
                matches = []
                order = -1
                for rule in matched.keys():
                    if not matched[rule] and self.rule_ranges[rule].issuperset(tickets_row):
                        matches.append(rule)
                        order = i
                if len(matches) == 1:
                    rule_order[matches[0]] = order
                    matched[matches[0]] = True

        contains_departure = [rule for rule in self.rule_ranges.keys() if rule.startswith("departure")]
        res = 1
        for rule in contains_departure:
            res *= self.your_ticket[rule_order[rule]]

        return res
