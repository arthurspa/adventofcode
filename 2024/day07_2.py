from io import TextIOWrapper


"""
--- Part Two ---

The engineers seem concerned; the total calibration result you gave them is nowhere close to being within safety tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a third type of operator.

The concatenation operator (||) combines the digits from its left and right inputs into a single number. For example, 12 || 345 would become 12345. All operators are still evaluated left-to-right.

Now, apart from the three equations that could be made true using only addition and multiplication, the above example has three more equations that can be made true by inserting operators:

156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
192: 17 8 14 can be made true using 17 || 8 + 14.
Adding up all six test values (the three that could be made before using only + and * plus the new three that can now be made by also using ||) produces the new total calibration result of 11387.

Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. What is their total calibration result?


"""


def solve(input: TextIOWrapper):
    total = 0
    for line in input:
        test_value = int(line.split(":")[0])
        numbers = [int(x) for x in line.split(":")[1].strip().split(" ")]
        if equation_resolves(test_value, numbers):
            total += test_value

    print(total)


def equation_resolves(test_value: int, numbers: list):
    results = set()

    def calculate(i, current_eq_value):
        if i == len(numbers):
            results.add(current_eq_value)
            return

        calculate(i + 1, current_eq_value + numbers[i])
        calculate(i + 1, current_eq_value * numbers[i])
        concatenated = str(current_eq_value) + str(numbers[i])
        calculate(i + 1, int(concatenated))

    calculate(1, numbers[0])

    return test_value in results
