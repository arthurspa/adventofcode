from io import TextIOWrapper


def solve(input: TextIOWrapper):
    left, right = [], []
    for line in input:
        l, r = [int(x) for x in line.split(" ") if x != ""]
        left.append(l)
        right.append(r)

    left.sort()
    right.sort()

    diff = []
    for i in range(len(left)):
        diff.append(abs(left[i] - right[i]))

    print(diff)
