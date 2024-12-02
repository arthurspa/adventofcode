from io import TextIOWrapper


def solve(input: TextIOWrapper):
    safe_reports = 0
    for line in input:
        levels = [int(x) for x in line.strip().split(" ")]

        if is_safe(levels):
            safe_reports += 1
        else:
            for i in range(len(levels)):
                if is_safe(levels[:i] + levels[i + 1 :]):
                    safe_reports += 1
                    break

    print(safe_reports)


def is_safe(levels):
    level_order = None
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if abs(diff) > 3 or abs(diff) == 0:
            return False
        if level_order is None:
            level_order = diff > 0

        current_order = diff > 0
        if current_order != level_order:
            return False

    return True
