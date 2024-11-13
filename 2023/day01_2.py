
from io import TextIOWrapper


def solve(input: TextIOWrapper):
    acc = 0
    for line in input:
        all_digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                all_digits.append(int(c))
                continue

            digitFromStr = checkForStr(line[i:])
            if digitFromStr > -1:
                all_digits.append(digitFromStr)

        number = all_digits[0]*10 + all_digits[-1]
        # print(number)
        acc = acc + number
    
    print(acc)


def checkForStr(line: str) -> int:

    if line.startswith('one'):
        return 1
    if line.startswith('two'):
        return 2
    if line.startswith('three'):
        return 3
    if line.startswith('four'):
        return 4
    if line.startswith('five'):
        return 5
    if line.startswith('six'):
        return 6
    if line.startswith('seven'):
        return 7
    if line.startswith('eight'):
        return 8
    if line.startswith('nine'):
        return 9
    if line.startswith('ten'):
        return 10
    
    return -1

