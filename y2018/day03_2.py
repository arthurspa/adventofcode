class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, p1: Point, p2: Point, id: str):
        self.p1 = p1
        self.p2 = p2
        self.id = id


def solve(read):
    rectangles = []
    for line in read:
        rectangle = createRectangle(line)
        rectangles.append(rectangle)

    non_overlapping_rectangle = find_non_overlapping_rectangle(rectangles)

    print(non_overlapping_rectangle.id)


def find_non_overlapping_rectangle(rectangles):
    for i in range(len(rectangles)):
        overlap = False
        for j in range(len(rectangles)):
            if i != j and rectangles_overlap(rectangles[i], rectangles[j]):
                overlap = True
                break
        if overlap == False:
            return rectangles[i]

def rectangles_overlap(ret1: Rectangle, ret2: Rectangle):
    # If one rectangle is above top edge of other rectangle
    if (ret1.p2.y < ret2.p1.y) or (ret2.p2.y < ret1.p1.y):
        return False
    # If one rectangle is on left side of left edge of other rectangle
    if (ret1.p2.x < ret2.p1.x) or (ret2.p2.x < ret1.p1.x):
        return False

    return True


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

    id = partial[0].replace('#', '')
    left = int(partial[2].replace(':', '').split(',')[0])
    top = int(partial[2].replace(':', '').split(',')[1])
    width = int(partial[3].split('x')[0])
    height = int(partial[3].split('x')[1])

    p1 = Point(left + 1, top + 1)
    p2 = Point(left + width, top + height)
    rectangle = Rectangle(p1, p2, id)

    return rectangle
