"""
--- Day 3: Toboggan Trajectory ---
With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's
certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will
take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your
puzzle input) of the open squares (.) and trees (#) you can see. For example:

    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#

These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome
stability, the same pattern repeats to the right many times:

    ..##.........##.........##.........##.........##.........##.......  --->
    #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
    .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
    ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
    .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
    ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
    .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
    .#........#.#........#.#........#.#........#.#........#.#........#
    #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
    #...##....##...##....##...##....##...##....##...##....##...##....#
    .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your
map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start
by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position
that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there
was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you
encounter?
"""


class Day3(object):
    def __init__(self, input_file_path):

        self.slope_right = 3
        self.slope_down = 1

        with open(input_file_path, "r") as f:
            self.toboggan = [line.strip() for line in f.readlines()]

        self.pattern_length = len(self.toboggan[0])
        self.toboggan_depth = len(self.toboggan)

    def part_1(self):
        current_pos = current_depth = n_trees = 0
        while current_depth < self.toboggan_depth - 1:
            current_pos = (current_pos + self.slope_right) % self.pattern_length
            current_depth += 1
            if self.toboggan[current_depth][current_pos] == "#":
                n_trees += 1

        return n_trees
