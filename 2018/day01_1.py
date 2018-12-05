import os
import sys


def solve():
    accumulator = 0
    for frequency in read:
        accumulator += int(frequency)

    print(accumulator)


if os.environ.get('DEBUG'):
    filename = __file__.split('.')[0] + '.input'
    read = open(filename)
else:
    read = sys.stdin

solve()

read.close
