"""
--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the
tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize
you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can
predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#).
For example, the initial seat layout might look like this:

    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL

Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and
always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat
(one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are
applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

    #.##.##.##
    #######.##
    #.#.#..#..
    ####.##.##
    #.##.##.##
    #.#####.##
    ..#.#.....
    ##########
    #.######.#
    #.#####.##

After a second round, the seats with four or more occupied adjacent seats become empty again:

    #.LL.L#.##
    #LLLLLL.L#
    L.L.L..L..
    #LLL.LL.L#
    #.LL.LL.LL
    #.LLLL#.##
    ..L.L.....
    #LLLLLLLL#
    #.LLLLLL.L
    #.#LLLL.##

This process continues for three more rounds:

    #.##.L#.##
    #L###LL.L#
    L.#.#..#..
    #L##.##.L#
    #.##.LL.LL
    #.###L#.##
    ..#.#.....
    #L######L#
    #.LL###L.L
    #.#L###.##
    #.#L.L#.##
    #LLL#LL.L#
    L.L.L..#..
    #LLL.##.L#
    #.LL.LL.LL
    #.LL#L#.##
    ..L.L.....
    #L#LLLL#L#
    #.LLLLLL.L
    #.#L#L#.##
    #.#L.L#.##
    #LLL#LL.L#
    L.#.L..#..
    #L##.##.L#
    #.#L.LL.LL
    #.#L#L#.##
    ..L.L.....
    #L#L##L#L#
    #.LLLLLL.L
    #.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no
seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up
occupied?
"""
from copy import deepcopy


class Day11(object):
    def __init__(self, input_file_path):
        with open(input_file_path, "r") as f:
            self.original_seats = [list(line.strip()) for line in f.readlines()]

    @staticmethod
    def adjacent_occupied(seats, i, j):
        n_occupied = 0
        # Diagonal up left
        if i - 1 >= 0 and j - 1 >= 0 and seats[i - 1][j - 1] == "#":
            n_occupied += 1
        # Up
        if i - 1 >= 0 and seats[i - 1][j] == "#":
            n_occupied += 1
        # Diagonal up right
        if i - 1 >= 0 and j + 1 < len(seats[0]) and seats[i - 1][j + 1] == "#":
            n_occupied += 1
        # Right
        if j + 1 < len(seats[0]) and seats[i][j + 1] == "#":
            n_occupied += 1
        # Diagonal down right
        if i + 1 < len(seats) and j + 1 < len(seats[0]) and seats[i + 1][j + 1] == "#":
            n_occupied += 1
        # Down
        if i + 1 < len(seats) and seats[i + 1][j] == "#":
            n_occupied += 1
        # Diagonal down left
        if i + 1 < len(seats) and j - 1 >= 0 and seats[i + 1][j - 1] == "#":
            n_occupied += 1
        # Left
        if j - 1 >= 0 and seats[i][j - 1] == "#":
            n_occupied += 1

        return n_occupied

    @staticmethod
    def are_sittings_equal(seating1, seating2):
        return "".join(["".join(s) for s in seating1]) == "".join(["".join(s) for s in seating2])

    @staticmethod
    def n_occupied_seats(seating):
        return "".join(["".join(s) for s in seating]).count("#")

    def part_1(self):
        changes = True
        current_seating = deepcopy(self.original_seats)
        while changes:
            new_sitting = deepcopy(current_seating)
            for i in range(len(current_seating)):
                for j in range(len(current_seating[0])):
                    if current_seating[i][j] == "L" and self.adjacent_occupied(current_seating, i, j) == 0:
                        new_sitting[i][j] = "#"
                    elif current_seating[i][j] == "#" and self.adjacent_occupied(current_seating, i, j) >= 4:
                        new_sitting[i][j] = "L"

            if self.are_sittings_equal(current_seating, new_sitting):
                changes = False
            else:
                current_seating = deepcopy(new_sitting)

        return self.n_occupied_seats(current_seating)

    def part_2(self):
        return 0
