from typing import List, Tuple


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end="")
        print()
    print("")


def is_in_grid(i, j, grid) -> bool:
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])


def get_directions(with_diagonals: bool = False):
    if with_diagonals:
        return [
            (-1, 0),  # up
            (0, 1),  # right
            (1, 0),  # down
            (0, -1),  # left
            (-1, 1),  # up-right
            (1, 1),  # down-right
            (-1, -1),  # up-left
            (1, -1),  # down-left
        ]
    else:
        return [
            (1, 0),  # down
            (0, 1),  # right
            (-1, 0),  # up
            (0, -1),  # left
        ]


class Direction:
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)
    UP_RIGHT = (-1, 1)
    DOWN_RIGHT = (1, 1)
    UP_LEFT = (-1, -1)
    DOWN_LEFT = (1, -1)

    def all(with_diagonals: bool = False):
        if with_diagonals:
            return [
                Direction.UP,
                Direction.RIGHT,
                Direction.DOWN,
                Direction.LEFT,
                Direction.UP_RIGHT,
                Direction.DOWN_RIGHT,
                Direction.UP_LEFT,
                Direction.DOWN_LEFT,
            ]
        else:
            return [
                Direction.DOWN,
                Direction.RIGHT,
                Direction.UP,
                Direction.LEFT,
            ]


class Grid(list):
    def __init__(self, grid: List = []):
        super().__init__(grid)

    def is_in_grid(self, i, j) -> bool:
        return 0 <= i < len(self) and 0 <= j < len(self[i])

    def get_neighbor_value(self, i, j, direction: Direction):
        ni, nj = i + direction[0], j + direction[1]
        if not self.is_in_grid(ni, nj):
            return None

        return self[ni][nj]

    def get_neighbor_index(self, i, j, direction: Direction) -> Tuple[int]:
        ni, nj = i + direction[0], j + direction[1]
        if not self.is_in_grid(ni, nj):
            return None

        return (ni, nj)

    def get_text(self) -> str:
        text = ""
        for i in range(len(self)):
            for j in range(len(self[i])):
                text += str(self[i][j])
            text += "\n"

        return text
