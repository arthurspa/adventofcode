from io import TextIOWrapper
from helpers import Grid, Direction
import re
import os

"""
--- Part Two ---

During the bathroom break, someone notices that these robots seem awfully similar to ones built and used at the North Pole. If they're the same type of robots, they should have a hard-coded Easter egg: very rarely, most of the robots should arrange themselves into a picture of a Christmas tree.

What is the fewest number of seconds that must elapse for the robots to display the Easter egg?
"""


class Robot:
    def __init__(self, px: int, py: int, vx: int, vy: int):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def tick(self, seconds: int, rows, cols):
        self.px = (self.px + self.vx * seconds) % cols
        self.py = (self.py + self.vy * seconds) % rows

    def is_in_quadrant(self, quadrant: tuple):
        if (
            self.py >= quadrant[0]
            and self.py < quadrant[1]
            and self.px >= quadrant[2]
            and self.px < quadrant[3]
        ):
            return True

        return False


def solve(input: TextIOWrapper):
    output_folder = "day14_2_output"
    os.makedirs(output_folder, exist_ok=True)
    lines = input.readlines()

    rows = 103
    cols = 101
    max_iteration = 20000  # seconds

    def simulate(seconds: int):
        grid = Grid()
        for i in range(rows):
            grid.append([])
            for _ in range(cols):
                grid[i].append(" ")

        coordinates_with_robots = set()
        for line in lines:
            px, py, vx, vy = re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)[0]
            robot = Robot(int(px), int(py), int(vx), int(vy))
            robot.tick(seconds, rows, cols)
            grid[robot.py][robot.px] = "."
            coordinates_with_robots.add((robot.py, robot.px))

        robots_with_neighbors = 0
        for coordinate in coordinates_with_robots:
            right_neighbor = grid.get_neighbor_value(
                coordinate[0], coordinate[1], Direction.RIGHT
            )
            left_neighbor = grid.get_neighbor_value(
                coordinate[0], coordinate[1], Direction.LEFT
            )

            if right_neighbor == "." or left_neighbor == ".":
                robots_with_neighbors += 1

        return robots_with_neighbors, grid

    max_robots_with_neighbors = 0
    grid_with_max_robots_with_neighbors = None
    seconds_of_max_robots_with_neighbors = 0
    for seconds in range(1, max_iteration):
        robots_with_neighbors, grid = simulate(seconds)
        if robots_with_neighbors > max_robots_with_neighbors:
            seconds_of_max_robots_with_neighbors = seconds
            grid_with_max_robots_with_neighbors = grid
            max_robots_with_neighbors = robots_with_neighbors

    text = grid_with_max_robots_with_neighbors.get_text()
    with open(f"day14_2_output/{seconds_of_max_robots_with_neighbors}", "w") as f:
        f.write(text)

    print(seconds_of_max_robots_with_neighbors)
