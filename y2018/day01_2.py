def solve(read):
    accumulator = 0
    frequencies = [int(f) for f in read]
    visited_frequencies = set([0])
    not_found = True
    while not_found:
        for f in frequencies:
            accumulator += f
            if accumulator in visited_frequencies:
                print(accumulator)
                not_found = False
                break
            else:
                visited_frequencies.add(accumulator)
