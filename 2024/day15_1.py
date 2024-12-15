from io import TextIOWrapper
from typing import List
from helpers import Grid, Direction

"""
--- Day 15: Warehouse Woes ---

You appear back inside your own mini submarine! Each Historian drives their mini submarine in a different direction; maybe the Chief has his own submarine down here somewhere as well?

You look up to see a vast school of lanternfish swimming past you. On closer inspection, they seem quite anxious, so you drive your mini submarine over to see if you can help.

Because lanternfish populations grow rapidly, they need a lot of food, and that food needs to be stored somewhere. That's why these lanternfish have built elaborate warehouse complexes operated by robots!

These lanternfish seem so anxious because they have lost control of the robot that operates one of their most important warehouses! It is currently running amok, pushing around boxes in the warehouse with no regard for lanternfish logistics or lanternfish inventory management strategies.

Right now, none of the lanternfish are brave enough to swim up to an unpredictable robot so they could shut it off. However, if you could anticipate the robot's movements, maybe they could find a safe option.

The lanternfish already have a map of the warehouse and a list of movements the robot will attempt to make (your puzzle input). The problem is that the movements will sometimes fail as boxes are shifted around, making the actual movements of the robot difficult to predict.

For example:

##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
As the robot (@) attempts to move, if there are any boxes (O) in the way, the robot will also attempt to push those boxes. However, if this action would cause the robot or a box to move into a wall (#), nothing moves instead, including the robot. The initial positions of these are shown on the map at the top of the document the lanternfish gave you.

The rest of the document describes the moves (^ for up, v for down, < for left, > for right) that the robot will attempt to make, in order. (The moves form a single giant sequence; they are broken into multiple lines just to make copy-pasting easier. Newlines within the move sequence should be ignored.)

Here is a smaller example to get started:

########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
Were the robot to attempt the given sequence of moves, it would push around the boxes as follows:

Initial state:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move <:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#..@OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.@...#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#..@O..#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#...@O.#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#....@O#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#.....O#
#.#.O@.#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########
The larger example has many more moves; after the robot has finished those moves, the warehouse would look like this:

##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########
The lanternfish use their own custom Goods Positioning System (GPS for short) to track the locations of the boxes. The GPS coordinate of a box is equal to 100 times its distance from the top edge of the map plus its distance from the left edge of the map. (This process does not stop at wall tiles; measure all the way to the edges of the map.)

So, the box shown below has a distance of 1 from the top edge of the map and 4 from the left edge of the map, resulting in a GPS coordinate of 100 * 1 + 4 = 104.

#######
#...O..
#......
The lanternfish would like to know the sum of all boxes' GPS coordinates after the robot finishes moving. In the larger example, the sum of all boxes' GPS coordinates is 10092. In the smaller example, the sum is 2028.

Predict the motion of the robot and boxes in the warehouse. After the robot is finished moving, what is the sum of all boxes' GPS coordinates?

To begin, get your puzzle input.
"""


def solve(input: TextIOWrapper):
    all_text = input.read()
    grid_text = all_text.split("\n\n")[0].splitlines()
    grid = Grid()
    robot_position = None
    for i in range(len(grid_text)):
        grid.append([])
        line = grid_text[i].strip()
        for j in range(len(line)):
            c = line[j]
            grid[i].append(c)
            if c == "@":
                robot_position = (i, j)

    moves_text = all_text.split("\n\n")[1].splitlines()
    moves_text = "".join(moves_text)
    directions: List[Direction] = []
    for c in moves_text:
        if c == "<":
            directions.append(Direction.LEFT)
        elif c == ">":
            directions.append(Direction.RIGHT)
        elif c == "v":
            directions.append(Direction.DOWN)
        elif c == "^":
            directions.append(Direction.UP)

    # print(grid.get_text())
    for direction in directions:
        robot_position = move_robot(robot_position, grid, direction)
        # print(grid.get_text())

    sum = calc_sum_of_boxes_gps_coordinates(grid)
    print(sum)


def move_robot(robot_position, grid: Grid, direction: Direction):
    neighbor_value = grid.get_neighbor_value(
        robot_position[0], robot_position[1], direction
    )
    neighbor_index = grid.get_neighbor_index(
        robot_position[0], robot_position[1], direction
    )
    if neighbor_value == ".":
        grid[robot_position[0]][robot_position[1]] = "."
        grid[neighbor_index[0]][neighbor_index[1]] = "@"
        return neighbor_index

    if neighbor_value == "O":
        current_box_position = neighbor_index
        past_last_box_group_position = None
        while True:
            box_neighbor_value = grid.get_neighbor_value(
                current_box_position[0], current_box_position[1], direction
            )
            box_neighbor_index = grid.get_neighbor_index(
                current_box_position[0], current_box_position[1], direction
            )
            if box_neighbor_value == ".":
                past_last_box_group_position = grid.get_neighbor_index(
                    box_neighbor_index[0], box_neighbor_index[1], direction
                )
                break
            if box_neighbor_value == "#":
                break

            current_box_position = box_neighbor_index

        # if not possible to move boxes return robot position
        if past_last_box_group_position is None:
            return robot_position

        # move boxes
        first_position = neighbor_index
        current_box_position = first_position
        while current_box_position != past_last_box_group_position:
            if current_box_position == first_position:
                grid[current_box_position[0]][current_box_position[1]] = "."
            else:
                grid[current_box_position[0]][current_box_position[1]] = "O"

            current_box_position = grid.get_neighbor_index(
                current_box_position[0], current_box_position[1], direction
            )

        # move robot
        grid[robot_position[0]][robot_position[1]] = "."
        grid[neighbor_index[0]][neighbor_index[1]] = "@"

        return neighbor_index

    return robot_position


def calc_sum_of_boxes_gps_coordinates(grid):
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                sum += 100 * i + j
    return sum
