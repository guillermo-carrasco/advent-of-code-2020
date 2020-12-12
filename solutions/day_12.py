"""
Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to
take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety,
it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you
quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer
input values. After staring at them for a few minutes, you work out what they probably mean:

    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.

The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship
is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the
following action were F.)

For example:

    F10
    N3
    F7
    R90
    F11

These instructions would be handled as follows:

F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
N3 would move the ship 3 units north to east 10, north 3.
F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
F11 would move the ship 11 units south to east 17, south 8.

At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position
and its north/south position) from its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's
starting position?
"""
import numpy as np


class Day12(object):
    def __init__(self, input_file_path):
        with open(input_file_path, "r") as f:
            self.directions = [(line[0], int(line[1:])) for line in f.readlines()]

        # Change in direction always change position in the same way
        self.navigation = {
            "N": np.array([0, 1]),
            "S": np.array([0, -1]),
            "E": np.array([1, 0]),
            "W": np.array([-1, 0]),
        }
        # The forward movement depends on your current direction
        self.forward_navigation = {
            "north": np.array([0, 1]),
            "south": np.array([0, -1]),
            "east": np.array([1, 0]),
            "west": np.array([-1, 0]),
        }
        # From left or right movements, you can end up in three different directions from your current direction
        self.right_rotation = {
            "north": {90: "east", 180: "south", 270: "west"},
            "south": {90: "west", 180: "north", 270: "east"},
            "east": {90: "south", 180: "west", 270: "north",},
            "west": {90: "north", 180: "east", 270: "south",},
        }
        self.left_rotation = {
            "north": {90: "west", 180: "south", 270: "east"},
            "south": {90: "east", 180: "north", 270: "west"},
            "east": {90: "north", 180: "west", 270: "south",},
            "west": {90: "south", 180: "east", 270: "north",},
        }

    def part_1(self):
        current_position = np.array([0, 0])
        current_direction = "east"
        for direction, steps in self.directions:
            if direction in ["N", "S", "E", "W"]:
                current_position = current_position + self.navigation[direction] * steps
            elif direction == "F":
                current_position = current_position + self.forward_navigation[current_direction] * steps
            elif direction == "L":
                current_direction = self.left_rotation[current_direction][steps]
            elif direction == "R":
                current_direction = self.right_rotation[current_direction][steps]

        return sum(abs(current_position))

    def part_2(self):
        return 0
