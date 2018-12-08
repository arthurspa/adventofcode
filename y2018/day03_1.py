class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2


def solve(read):
    rectangles = []
    max_width = 0
    max_height = 0
    for line in read:
        rectangle = createRectangle(line)
        rectangles.append(rectangle)
        max_width = max(max_width, rectangle.p2.x)
        max_height = max(max_height, rectangle.p2.y)

    grid = buildGrid(max_width, max_height)
    grid = fillGrid(grid, rectangles)
    intersection_area = calc_intersection_area(grid)

    print(intersection_area)


def calc_intersection_area(grid):
    area = 0
    for row in grid:
        for value in row:
            if value > 1:
                area += 1
    return area


def fillGrid(grid, rectangles):
    for rect in rectangles:
        for x in range(rect.p1.x, rect.p2.x + 1):
            for y in range(rect.p1.y, rect.p2.y + 1):
                grid[x][y] += 1

    return grid


def createRectangle(line: str):
    '''
    The rectangle is defined by two diagonal points
    p1 (top left) and p2 (bottom right), for example:
    
    ........
    ..111...
    ..111...
    ........

    This claim rectangle would be defined by:
    p1 (3,2) and
    p2 (5,3)
    
    '''
    line = line.strip()  # remove \n
    partial = line.split(' ')

    left = int(partial[2].replace(':', '').split(',')[0])
    top = int(partial[2].replace(':', '').split(',')[1])
    width = int(partial[3].split('x')[0])
    height = int(partial[3].split('x')[1])

    p1 = Point(left + 1, top + 1)
    p2 = Point(left + width, top + height)
    rectangle = Rectangle(p1, p2)

    return rectangle


def buildGrid(max_width, max_height):
    return [[0] * (max_height + 1) for _ in range(max_width + 1)]
