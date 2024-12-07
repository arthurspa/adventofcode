from io import TextIOWrapper

"""
--- Part Two ---

While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the lab. From the safety of a supply closet, you time travel through the last few months and record the nightly status of the lab's guard post on the walls of the closet.

Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is simply too large for them to safely search the lab without getting caught.

Fortunately, they are pretty sure that adding a single new obstruction won't cause a time paradox. They'd like to place the new obstruction in such a way that the guard will get stuck in a loop, making the rest of the lab safe to search.

To have the lowest chance of creating a time paradox, The Historians would like to know all of the possible positions for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.

In the above example, there are only 6 different positions where a new obstruction would cause the guard to get stuck in a loop. The diagrams of these six situations use O to mark the new obstruction, | to show a position where the guard moves up/down, - to show a position where the guard moves left/right, and + to show a position where the guard moves both up/down and left/right.

Option one, put a printing press next to the guard's starting position:

....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.O^---+.
........#.
#.........
......#...
Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
......O.#.
#.........
......#...
Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----+O#.
#+----+...
......#...
Option four, put an alchemical retroencabulator near the bottom left corner:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
..|...|.#.
#O+---+...
......#...
Option five, put the alchemical retroencabulator a bit to the right instead:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..O+-+...
......#...
Option six, put a tank of sovereign glue right next to the tank of universal solvent:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#O..
It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into position without the guard noticing. The important thing is having enough options that you can find one that minimizes time paradoxes, and in this example, there are 6 different positions you could choose.

You need to get the guard stuck in a loop by adding a single new obstruction. How many different positions could you choose for this obstruction?
"""


def solve(input: TextIOWrapper):
    grid = []
    initial_position = (0, 0, 0)
    lines = input.readlines()
    for i in range(len(lines)):
        grid.append([])
        line = lines[i].strip()
        for j in range(len(line)):
            c = line[j]
            if c == ".":
                grid[i].append(0)
            elif c == "#":
                grid[i].append(1)
            elif c == "^":
                grid[i].append(0)
                initial_position = (i, j, 0)

    rows = len(grid)
    cols = len(grid[0])
    current = 0
    num_loops_found = 0
    for i in range(rows):
        for j in range(cols):
            current += 1
            original_value = grid[i][j]

            if original_value == 1 or (i, j, 0) == initial_position:
                continue

            grid[i][j] = 1
            # find loop
            if has_loop(initial_position, grid):
                print(f"({i}, {j}): loops found: {num_loops_found}")
                num_loops_found += 1

            # restore original value
            grid[i][j] = original_value

    print(num_loops_found)
    # print(has_loop(initial_position, grid))


def has_loop(initial_position, grid):
    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    current_position = initial_position
    while True:
        visited.add(current_position)
        direction = current_position[2]
        if direction == 0:
            next_position = (current_position[0] - 1, current_position[1])
        elif direction == 1:
            next_position = (current_position[0], current_position[1] + 1)
        elif direction == 2:
            next_position = (current_position[0] + 1, current_position[1])
        elif direction == 3:
            next_position = (current_position[0], current_position[1] - 1)

        if (
            0 <= next_position[0] < rows
            and 0 <= next_position[1] < cols
            and grid[next_position[0]][next_position[1]] == 1
        ):
            next_direction = (direction + 1) % 4
            if next_direction == 0:
                tmp_position = (current_position[0] - 1, current_position[1])
                if is_obstacle(tmp_position[0], tmp_position[1], grid):
                    next_position = current_position[:2]
                else:
                    next_position = tmp_position
            elif next_direction == 1:
                tmp_position = (current_position[0], current_position[1] + 1)
                if is_obstacle(tmp_position[0], tmp_position[1], grid):
                    next_position = current_position[:2]
                else:
                    next_position = tmp_position
            elif next_direction == 2:
                tmp_position = (current_position[0] + 1, current_position[1])
                if is_obstacle(tmp_position[0], tmp_position[1], grid):
                    next_position = current_position[:2]
                else:
                    next_position = tmp_position
            elif next_direction == 3:
                tmp_position = (current_position[0], current_position[1] - 1)
                if is_obstacle(tmp_position[0], tmp_position[1], grid):
                    next_position = current_position[:2]
                else:
                    next_position = tmp_position
        else:
            next_direction = current_position[2]

        current_position = (next_position[0], next_position[1], next_direction)
        if current_position in visited:
            return True

        if (
            current_position[0] < 0
            or current_position[0] >= rows
            or current_position[1] < 0
            or current_position[1] >= cols
        ):
            break

    return False


def is_obstacle(x, y, grid):
    if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
        return grid[x][y] == 1

    return False
