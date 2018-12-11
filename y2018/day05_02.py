import re
import y2018.day05_01 as prev_solution


def solve(read):
    for line in read:
        sequence = line.strip()

    min_len = None
    for num in range(ord('a'), ord('z') + 1):
        shorter_squence = prev_solution.fully_react(remove_unit(num, sequence))
        shorter_squence_len = len(shorter_squence)
        if min_len and shorter_squence_len < min_len:
            min_len = shorter_squence_len
        elif min_len == None:
            min_len = shorter_squence_len

    print(min_len)


def remove_unit(num, sequence):
    letter_lower = chr(num)
    letter_upper = letter_lower.upper()
    shorter_squence = re.sub(f'[{letter_lower}{letter_upper}]', '', sequence)

    return shorter_squence
