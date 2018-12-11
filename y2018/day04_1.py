import re
import functools


def solve(read):
    sorted_lines = read_and_sort(read)
    sleepy_guard, _ = get_sleepy_guard(sorted_lines)
    guard_id = sleepy_guard['guard_id']
    most_sleep_minutes, _ = get_most_sleep_minutes(sleepy_guard)

    print(guard_id * most_sleep_minutes)


def get_most_sleep_minutes(sleepy_guard):
    sleep_ranges = sleepy_guard['sleep_ranges']
    time_table = [[0]*60 for _ in range(len(sleep_ranges))]

    for i in range(len(sleep_ranges)):
        start = sleep_ranges[i][0]
        stop = sleep_ranges[i][1]
        for j in range(start, stop + 1):
            time_table[i][j] += 1
    
    most_sleep_minute = 0
    times_slept = 0
    for minute in range(60):
        minutes_total = 0
        for j in range(len(sleep_ranges)):
            minutes_total += time_table[j][minute]
        
        if minutes_total > times_slept:
            times_slept = minutes_total
            most_sleep_minute = minute

        times_slept = max(times_slept, minutes_total)
    
    # times_slept is needed for solution day04_2
    return most_sleep_minute, times_slept



def get_sleepy_guard(lines):
    guards = {}
    sleepy_guard = None
    current_guard_id = None
    start_sleep_minutes = None
    for line in lines:
        temp_guard_id = get_guard_id(line)
        if temp_guard_id:  # shift change
            current_guard_id = temp_guard_id
            if current_guard_id not in guards:
                guards[temp_guard_id] = {
                    'guard_id' : int(current_guard_id),
                    'total_sleep_time': 0,
                    'sleep_ranges': []
                }
        else:
            guard = guards[current_guard_id]
            if 'asleep' in line:  # guard falls asleep
                start_sleep_minutes = get_minutes_only(line)
            else:  # guard wakes up
                stop_sleep_minutes = get_minutes_only(line) - 1

                spleep_time = stop_sleep_minutes - start_sleep_minutes
                guard['total_sleep_time'] += spleep_time

                sleep_time_range = (start_sleep_minutes, stop_sleep_minutes)
                guard['sleep_ranges'].append(sleep_time_range)

            if not sleepy_guard:
                sleepy_guard = guard
            elif guard['total_sleep_time'] > sleepy_guard['total_sleep_time']:
                sleepy_guard = guard

    # guards variable is needed for day04_2
    return sleepy_guard, guards


def read_and_sort(read):
    lines = []
    for line in read:
        line = line.strip()
        lines.append(line)

    lines.sort(key=functools.cmp_to_key(time_comp))

    return lines


def time_comp(l1, l2):
    y1, m1, d1, h1, mm1 = get_time(l1)
    y2, m2, d2, h2, mm2 = get_time(l2)

    if (
        (y1 < y2) or
        ((y1 == y2) and (m1 < m2)) or
        ((y1 == y2) and (m1 == m2) and (d1 < d2)) or
        ((y1 == y2) and (m1 == m2) and (d1 == d2) and (h1 < h2)) or
        ((y1 == y2) and (m1 == m2) and (d1 == d2) and (h1 == h2) and (mm1 < mm2))
    ):
        return -1
    elif (
        (y1 > y2) or
        ((y1 == y2) and (m1 > m2)) or
        ((y1 == y2) and (m1 == m2) and (d1 > d2)) or
        ((y1 == y2) and (m1 == m2) and (d1 == d2) and (h1 > h2)) or
        ((y1 == y2) and (m1 == m2) and (d1 == d2) and (h1 == h2) and (mm1 > mm2))
    ):
        return 1
    else:
        return 0


def get_time(line):
    time_pattern = '\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\]'

    time_match = re.match(time_pattern, line)
    year, month, day, hour, minutes = [
        time_match.group(i+1) for i in range(5)]

    return int(year), int(month), int(day), int(hour), int(minutes)


def get_minutes_only(line):
    _, _, _, _, minutes = get_time(line)
    return int(minutes)


def get_guard_id(line):
    guard_id_pattern = '#(\d+)'
    guard_id_match = re.search(guard_id_pattern, line)

    if guard_id_match:
        return int(guard_id_match.group(1))
    else:
        return None
