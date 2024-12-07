from io import TextIOWrapper

"""
--- Day 6: Guard Gallivant ---

The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.
Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:

....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. Including the guard's starting position, the positions visited by the guard before leaving the area are marked with an X:

....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
In this example, the guard will visit 41 distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?

"""


def solve(input: TextIOWrapper):
    grid = []
    current_position = (0, 0)
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
                current_position = (i, j, 0)

    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    while True:
        visited.add(current_position[:2])
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
                next_position = (current_position[0] - 1, current_position[1])
            elif next_direction == 1:
                next_position = (current_position[0], current_position[1] + 1)
            elif next_direction == 2:
                next_position = (current_position[0] + 1, current_position[1])
            elif next_direction == 3:
                next_position = (current_position[0], current_position[1] - 1)
        else:
            next_direction = current_position[2]

        current_position = (next_position[0], next_position[1], next_direction)
        if (
            current_position[0] < 0
            or current_position[0] >= rows
            or current_position[1] < 0
            or current_position[1] >= cols
        ):
            break

    print(len(visited))
