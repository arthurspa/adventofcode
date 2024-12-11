from functools import lru_cache
from io import TextIOWrapper


"""
--- Part Two ---

The Historians sure are taking a long time. To be fair, the infinite corridors are very large.

How many stones would you have after blinking a total of 75 times?
"""


def solve(input: TextIOWrapper):
    initial_stones = [int(x) for x in input.read().split()]

    mem = dict()

    @lru_cache(None)
    def blink(stone, num_blinks, stones_count):
        hash = (stone, num_blinks)
        if hash in mem:
            return mem[hash]

        if num_blinks == 75:
            mem[hash] = stones_count
            return stones_count

        if stone == 0:
            return blink(1, num_blinks + 1, stones_count)

        if len(str(stone)) % 2 == 0:
            engraving_str = str(stone)
            engraving_left = int(engraving_str[: len(engraving_str) // 2])
            engraving_right = int(engraving_str[len(engraving_str) // 2 :])
            left = blink(engraving_left, num_blinks + 1, stones_count)
            right = blink(engraving_right, num_blinks + 1, stones_count)
            return left + right

        return blink(stone * 2024, num_blinks + 1, stones_count)

    total_count = 0
    for stone in initial_stones:
        initial_blink_count = 0
        initial_count = 1  # the stone we started with
        total_count += blink(stone, initial_blink_count, initial_count)
        # print("total_count so far", total_count)

    print(total_count)
