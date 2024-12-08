from io import TextIOWrapper

"""
--- Part Two ---

Watching over your shoulder as you work, one of The Historians asks if you took the effects of resonant harmonics into your calculations.

Whoops!

After updating your model, it turns out that an antinode occurs at any grid position exactly in line with at least two antennas of the same frequency, regardless of distance. This means that some of the new antinodes will occur at the position of each antenna (unless that antenna is the only one of its frequency).

So, these three T-frequency antennas now create many antinodes:

T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........
In fact, the three T-frequency antennas are all exactly in line with two antennas, so they are all also antinodes! This brings the total number of antinodes in the above example to 9.

The original example now has 34 antinodes, including the antinodes that appear on every antenna:

##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##
Calculate the impact of the signal using this updated model. How many unique locations within the bounds of the map contain an antinode?
"""


def solve(input: TextIOWrapper):
    grid = []
    lines = input.readlines()
    frequencies = dict()
    for i in range(len(lines)):
        grid.append([])
        line = lines[i].strip()
        for j in range(len(line)):
            c = line[j]
            grid[i].append(c)
            if c.isalnum():
                if c not in frequencies:
                    frequencies[c] = []

                frequencies[c].append((i, j))

    rows = len(grid)
    cols = len(grid[0])

    def is_in_grid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    antinodes_coordinates = set()
    for f in frequencies:
        for i in range(len(frequencies[f])):
            antinodes_coordinates.add(frequencies[f][i])
            for j in range(len(frequencies[f])):
                if i == j:
                    continue
                xi, yi = frequencies[f][i]
                xj, yj = frequencies[f][j]
                inc_i, inc_j = (xi - xj, yi - yj)

                x, y = (xi + inc_i, yi + inc_j)
                while is_in_grid(x, y):
                    antinodes_coordinates.add((x, y))
                    x, y = (x + inc_i, y + inc_j)

    print(len(antinodes_coordinates))
