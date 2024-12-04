from io import TextIOWrapper

"""
--- Day 4: Ceres Search ---

"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?


"""

xmas = "XMAS"

all_directions = [
    (dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)
]


def solve(input: TextIOWrapper):
    lines = input.read().splitlines()

    count = 0
    for current_x in range(len(lines)):
        for current_y in range(len(lines[0])):
            for direction_x, direction_y in all_directions:
                word_found_in_direction = True
                for i in range(len(xmas)):
                    current_xmas_character = xmas[i]
                    # print(f"{current_x + i * direction_x}, {current_y + i * direction_y}, {current_xmas_character}")
                    if (
                        # check bounds
                        (current_x + i * direction_x < 0)
                        or (current_x + i * direction_x >= len(lines))
                        or (current_y + i * direction_y < 0)
                        or (current_y + i * direction_y >= len(lines[0]))
                        # check character
                        or lines[current_x + i * direction_x][
                            current_y + i * direction_y
                        ]
                        != current_xmas_character
                    ):
                        word_found_in_direction = False
                        break

                if word_found_in_direction:
                    count += 1

    print(count)
