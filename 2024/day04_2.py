from io import TextIOWrapper

"""
--- Part Two ---

The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
"""


def solve(input: TextIOWrapper):
    lines = input.read().splitlines()

    count = 0
    for current_x in range(len(lines)):
        for current_y in range(len(lines[0])):
            is_first_diagonal_in_bounds = (
                is_in_bounds(lines, current_x - 1, current_y + 1)
                and is_in_bounds(lines, current_x, current_y)
                and is_in_bounds(lines, current_x + 1, current_y - 1)
            )

            is_second_diagonal_in_bounds = (
                is_in_bounds(lines, current_x + 1, current_y + 1)
                and is_in_bounds(lines, current_x, current_y)
                and is_in_bounds(lines, current_x - 1, current_y - 1)
            )

            if not (is_first_diagonal_in_bounds and is_second_diagonal_in_bounds):
                continue

            if not (
                (
                    lines[current_x - 1][current_y + 1] == "M"
                    and lines[current_x][current_y] == "A"
                    and lines[current_x + 1][current_y - 1] == "S"
                )
                or (
                    lines[current_x - 1][current_y + 1] == "S"
                    and lines[current_x][current_y] == "A"
                    and lines[current_x + 1][current_y - 1] == "M"
                )
            ):
                # print(f" ### {current_x}, {current_y}, {lines[current_x][current_y]}")
                continue

            if not (
                (
                    lines[current_x + 1][current_y + 1] == "M"
                    and lines[current_x][current_y] == "A"
                    and lines[current_x - 1][current_y - 1] == "S"
                )
                or (
                    lines[current_x + 1][current_y + 1] == "S"
                    and lines[current_x][current_y] == "A"
                    and lines[current_x - 1][current_y - 1] == "M"
                )
            ):
                continue

            # if reached here both diagonals matched
            count += 1

    print(count)


def is_in_bounds(lines, current_x, current_y):
    return (
        (current_x >= 0)
        and (current_x < len(lines))
        and (current_y >= 0)
        and (current_y < len(lines[0]))
    )
