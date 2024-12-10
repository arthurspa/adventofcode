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
            (1, 0),  # up
            (0, 1),  # right
            (-1, 0),  # down
            (0, -1),  # left
            (1, 1),  # up-right
            (-1, 1),  # down-right
            (1, -1),  # up-left
            (-1, -1),  # down-left
        ]
    else:
        return [
            (1, 0),  # up
            (0, 1),  # right
            (-1, 0),  # down
            (0, -1),  # left
        ]
