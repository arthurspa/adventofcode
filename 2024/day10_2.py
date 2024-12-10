from io import TextIOWrapper

import helpers

"""
--- Part Two ---

The reindeer spends a few minutes reviewing your hiking trail map before realizing something, disappearing for a few minutes, and finally returning with yet another slightly-charred piece of paper.

The paper describes a second way to measure a trailhead called its rating. A trailhead's rating is the number of distinct hiking trails which begin at that trailhead. For example:

.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....
The above map has a single trailhead; its rating is 3 because there are exactly three distinct hiking trails which begin at that position:

.....0.   .....0.   .....0.
..4321.   .....1.   .....1.
..5....   .....2.   .....2.
..6....   ..6543.   .....3.
..7....   ..7....   .....4.
..8....   ..8....   ..8765.
..9....   ..9....   ..9....
Here is a map containing a single trailhead with rating 13:

..90..9
...1.98
...2..7
6543456
765.987
876....
987....
This map contains a single trailhead with rating 227 (because there are 121 distinct hiking trails that lead to the 9 on the right edge and 106 that lead to the 9 on the bottom edge):

012345
123456
234567
345678
4.6789
56789.
Here's the larger example from before:

89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
Considering its trailheads in reading order, they have ratings of 20, 24, 10, 4, 1, 4, 5, 8, and 5. The sum of all trailhead ratings in this larger example topographic map is 81.

You're not sure how, but the reindeer seems to have crafted some tiny flags out of toothpicks and bits of paper and is using them to mark trailheads on your topographic map. What is the sum of the ratings of all trailheads?

"""


def solve(input: TextIOWrapper):
    lines = input.readlines()
    grid = []
    trailheads = []
    for i in range(len(lines)):
        grid.append([])
        line = lines[i].strip()
        for j in range(len(line)):
            c = line[j]
            if c == ".":
                grid[i].append(c)
            else:
                height = int(c)
                if height == 0:
                    trailheads.append((i, j))
                grid[i].append(height)

    total_score = 0
    for trailhead in trailheads:
        total_score += calculate_score(trailhead, grid)

    # print_grid(grid)

    print(total_score)


def calculate_score(trailhead, grid):
    def traverse(i, j):
        # if grid[i][j] == 9 and (i, j) not in reached_nines:
        #     reached_nines.add((i, j))
        #     return 1
        if grid[i][j] == 9 and (i, j):
            return 1

        current_height = grid[i][j]
        score = 0
        for di, dj in helpers.get_directions():
            ni, nj = i + di, j + dj
            if helpers.is_in_grid(ni, nj, grid) and grid[ni][nj] == current_height + 1:
                score += traverse(ni, nj)

        return score

    return traverse(trailhead[0], trailhead[1])
