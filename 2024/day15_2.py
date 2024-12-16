from io import TextIOWrapper
from typing import List
from helpers import Grid, Direction

"""
--- Part Two ---

The lanternfish use your information to find a safe moment to swim in and turn off the malfunctioning robot! Just as they start preparing a festival in your honor, reports start coming in that a second warehouse's robot is also malfunctioning.

This warehouse's layout is surprisingly similar to the one you just helped. There is one key difference: everything except the robot is twice as wide! The robot's list of movements doesn't change.

To get the wider warehouse's map, start with your original map and, for each tile, make the following changes:

If the tile is #, the new map contains ## instead.
If the tile is O, the new map contains [] instead.
If the tile is ., the new map contains .. instead.
If the tile is @, the new map contains @. instead.
This will produce a new warehouse map which is twice as wide and with wide boxes that are represented by []. (The robot does not change size.)

The larger example from before would now look like this:

####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################
Because boxes are now twice as wide but the robot is still the same size and speed, boxes can be aligned such that they directly push two other boxes at once. For example, consider this situation:

#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
After appropriately resizing this map, the robot would push around these boxes as follows:

Initial state:
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############

Move <:
##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############

Move ^:
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############
This warehouse also uses GPS to locate the boxes. For these larger boxes, distances are measured from the edge of the map to the closest edge of the box in question. So, the box shown below has a distance of 1 from the top edge of the map and 5 from the left edge of the map, resulting in a GPS coordinate of 100 * 1 + 5 = 105.

##########
##...[]...
##........
In the scaled-up version of the larger example from above, after the robot has finished all of its moves, the warehouse would look like this:

####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################
The sum of these boxes' GPS coordinates is 9021.

Predict the motion of the robot and boxes in this new, scaled-up warehouse. What is the sum of all boxes' final GPS coordinates?
"""


def solve(input: TextIOWrapper):
    all_text = input.read()
    grid_text = all_text.split("\n\n")[0].splitlines()
    grid = Grid()
    for direction_index in range(len(grid_text)):
        grid.append([])
        line = grid_text[direction_index].strip()
        for j in range(len(line)):
            c = line[j]
            if c == "O":
                grid[direction_index].append("[")
                grid[direction_index].append("]")
            if c == "#":
                grid[direction_index].append("#")
                grid[direction_index].append("#")
            if c == ".":
                grid[direction_index].append(".")
                grid[direction_index].append(".")
            if c == "@":
                robot_position = (direction_index, j)
                grid[direction_index].append("@")
                grid[direction_index].append(".")

    # find initial robot position
    robot_position = None
    for direction_index in range(len(grid)):
        for j in range(len(grid[direction_index])):
            if grid[direction_index][j] == "@":
                robot_position = (direction_index, j)
                break

        if robot_position is not None:
            break

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
    for direction_index in range(len(directions)):
        direction = directions[direction_index]
        robot_position = move_robot(robot_position, grid, direction)
        # if not check_grid_valid(grid):
        #     print(grid.get_text())
        #     break
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

    if neighbor_value in ["[", "]"]:
        if not move_box_if_possible(neighbor_index, grid, direction):
            return robot_position

        # move robot
        grid[robot_position[0]][robot_position[1]] = "."
        grid[neighbor_index[0]][neighbor_index[1]] = "@"

        return neighbor_index

    return robot_position


class Box:
    def __init__(self, left_side_pos, right_side_pos):
        self.left_side_pos = left_side_pos
        self.right_side_pos = right_side_pos
        self.prev_left_filled = False
        self.prev_right_filled = False

    def __hash__(self):
        return hash((self.left_side_pos, self.right_side_pos))


def get_box(first_box_side_position, grid: Grid):
    first_box_side = grid[first_box_side_position[0]][first_box_side_position[1]]
    if first_box_side == "[":
        return Box(
            first_box_side_position,
            (first_box_side_position[0], first_box_side_position[1] + 1),
        )
    else:
        return Box(
            (first_box_side_position[0], first_box_side_position[1] - 1),
            first_box_side_position,
        )


def box_has_obstacle_in_direction(box: Box, grid: Grid, direction: Direction):
    left_neighbor_value = grid.get_neighbor_value(
        box.left_side_pos[0], box.left_side_pos[1], direction
    )
    right_neighbor_value = grid.get_neighbor_value(
        box.right_side_pos[0], box.right_side_pos[1], direction
    )

    return left_neighbor_value == "#" or right_neighbor_value == "#"


def get_neighbor_boxes(box: Box, grid: Grid, direction: Direction):
    left_neighbor_value = grid.get_neighbor_value(
        box.left_side_pos[0], box.left_side_pos[1], direction
    )

    # neighbor box is in the middle
    if left_neighbor_value == "[":
        left_neighbor_index = grid.get_neighbor_index(
            box.left_side_pos[0], box.left_side_pos[1], direction
        )
        b = get_box(left_neighbor_index, grid)
        b.prev_left_filled = True
        b.prev_right_filled = True
        return [b]

    boxes = []
    if left_neighbor_value == "]":
        left_neighbor_index = grid.get_neighbor_index(
            box.left_side_pos[0], box.left_side_pos[1], direction
        )
        b = get_box(left_neighbor_index, grid)
        b.prev_right_filled = True
        boxes.append(b)

    right_neighbor_value = grid.get_neighbor_value(
        box.right_side_pos[0], box.right_side_pos[1], direction
    )
    if right_neighbor_value == "[":
        right_neighbor_index = grid.get_neighbor_index(
            box.right_side_pos[0], box.right_side_pos[1], direction
        )
        b = get_box(right_neighbor_index, grid)
        b.prev_left_filled = True
        boxes.append(b)

    return boxes


def move_box_if_possible(first_box_side_position, grid: Grid, direction: Direction):
    if direction in [Direction.RIGHT, Direction.LEFT]:
        current_box_position = first_box_side_position
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
            return False

        # move boxes
        current_box_position = first_box_side_position
        index = 0
        while current_box_position != past_last_box_group_position:
            if current_box_position == first_box_side_position:
                grid[current_box_position[0]][current_box_position[1]] = "."
            elif index % 2 != 0:
                if direction == Direction.RIGHT:
                    grid[current_box_position[0]][current_box_position[1]] = "["
                else:
                    grid[current_box_position[0]][current_box_position[1]] = "]"
            elif index % 2 == 0:
                if direction == Direction.RIGHT:
                    grid[current_box_position[0]][current_box_position[1]] = "]"
                else:
                    grid[current_box_position[0]][current_box_position[1]] = "["

            current_box_position = grid.get_neighbor_index(
                current_box_position[0], current_box_position[1], direction
            )
            index += 1

        return True
    else:
        first_box = get_box(first_box_side_position, grid)
        box_group: List[Box] = [first_box]
        boxes: List[Box] = [first_box]
        boxes_seen: set[Box] = set()
        can_be_moved = True
        while len(box_group) > 0:
            current_box = box_group.pop()
            if current_box in boxes_seen:
                continue

            boxes_seen.add(current_box)

            if box_has_obstacle_in_direction(current_box, grid, direction):
                can_be_moved = False
                break
            neighbor_boxes = get_neighbor_boxes(current_box, grid, direction)
            if len(neighbor_boxes) == 0:
                continue

            box_group.extend(neighbor_boxes)
            for nb in neighbor_boxes:
                found = False
                for b in boxes:
                    if b.__hash__() == nb.__hash__():
                        b.prev_left_filled = b.prev_left_filled or nb.prev_left_filled
                        b.prev_right_filled = (
                            b.prev_right_filled or nb.prev_right_filled
                        )
                        found = True
                        break
                if not found:
                    boxes.append(nb)

        if not can_be_moved:
            return False

        # move boxes
        for box in boxes:
            left_neighbor_index = grid.get_neighbor_index(
                box.left_side_pos[0], box.left_side_pos[1], direction
            )
            grid[left_neighbor_index[0]][left_neighbor_index[1]] = "["
            right_neighbor_index = grid.get_neighbor_index(
                box.right_side_pos[0], box.right_side_pos[1], direction
            )
            grid[right_neighbor_index[0]][right_neighbor_index[1]] = "]"

        # clear paths
        for box in boxes:
            if not box.prev_left_filled:
                grid[box.left_side_pos[0]][box.left_side_pos[1]] = "."

            if not box.prev_right_filled:
                grid[box.right_side_pos[0]][box.right_side_pos[1]] = "."

        return True

    return False


def calc_sum_of_boxes_gps_coordinates(grid):
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "[":
                sum += 100 * i + j
    return sum


def check_grid_valid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "[" and grid[i][j + 1] != "]":
                return False

    return True
