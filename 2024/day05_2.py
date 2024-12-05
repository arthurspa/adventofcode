from io import TextIOWrapper

"""
--- Part Two ---

While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.

For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:

75,97,47,61,53 becomes 97,75,47,61,53.
61,13,29 becomes 61,29,13.
97,13,75,29,47 becomes 97,75,47,29,13.
After taking only the incorrectly-ordered updates and ordering them correctly, their middle page numbers are 47, 29, and 47. Adding these together produces 123.

Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?

Answer:  
"""


def solve(input: TextIOWrapper):
    rules_b_a = dict()
    rules_a_b = dict()
    updates = []

    reading_rules = True
    for line in input:
        if line == "\n":
            reading_rules = False
            continue

        if reading_rules:
            before, after = line.strip().split("|")
            before = int(before)
            after = int(after)
            if before in rules_b_a:
                rules_b_a[before].append(after)
            else:
                rules_b_a[before] = []
                rules_b_a[before].append(after)

            if after in rules_a_b:
                rules_a_b[after].append(before)
            else:
                rules_a_b[after] = []
                rules_a_b[after].append(before)

        else:
            update = [int(x) for x in line.split(",")]
            updates.append(update)

    def is_update_in_order(update):
        for i in range(len(update)):
            for j in range(len(update)):
                if i == j:
                    continue
                if i < j:
                    before = update[i]
                    after = update[j]
                else:
                    before = update[j]
                    after = update[i]

                if after in rules_b_a and before in rules_b_a[after]:
                    return False

                if before in rules_a_b and after in rules_a_b[before]:
                    return False

        return True

    def order_update(update):
        update_happened = True
        while update_happened:
            update_happened = False
            for i in range(len(update)):
                for j in range(len(update)):
                    if i == j:
                        continue
                    if i < j:
                        before = update[i]
                        after = update[j]
                    else:
                        before = update[j]
                        after = update[i]

                    if after in rules_b_a and before in rules_b_a[after]:
                        update_happened = True
                        update[i], update[j] = update[j], update[i]
                        break

                    if before in rules_a_b and after in rules_a_b[before]:
                        update_happened = True
                        update[i], update[j] = update[j], update[i]
                        break

        return update

    count = 0
    for update in updates:
        if not is_update_in_order(update):
            middle = (len(update) - 1) // 2
            ordered_update = order_update(update)
            count += ordered_update[middle]

    print(count)
