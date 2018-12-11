import y2018.day04_1 as prev_solution


def solve(read):
    sorted_lines = prev_solution.read_and_sort(read)
    _, guards = prev_solution.get_sleepy_guard(sorted_lines)

    guard_rank = []
    for guard_id in guards:
        guard = guards[guard_id]
        most_sleep_minutes, times_slept = prev_solution.get_most_sleep_minutes(
            guard)
        guard_rank.append({
            'guard_id': guard_id,
            'most_sleep_minutes': most_sleep_minutes,
            'times_slept': times_slept
        })

    max_times_slept = 0
    winner = {}
    for rank in guard_rank:
        if rank['times_slept'] > max_times_slept:
            max_times_slept = rank['times_slept']
            winner = rank

    print(winner['guard_id']*winner['most_sleep_minutes'])
