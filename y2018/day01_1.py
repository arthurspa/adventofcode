def solve(read):
    accumulator = 0
    for frequency in read:
        accumulator += int(frequency)

    print(accumulator)
