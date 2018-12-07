
def solve(read):
    all_ids = [line[:-1] for line in read]
    id1, id2, differ_index = find_correct_ids(all_ids)
    string_excluded_differ = id1[:differ_index] + id1[differ_index + 1:]
    intersection = ''.join([c for c in string_excluded_differ])
    print(intersection)


def find_correct_ids(all_ids):
    for i in range(len(all_ids)-1):
        for j in range(i, len(all_ids)):
            id1 = all_ids[i]
            id2 = all_ids[j]
            diff_count = 0
            differ_index = 0
            for k in range(len(id1)):
                if id1[k] != id2[k]:
                    diff_count += 1
                    differ_index = k
                if diff_count > 1:
                    break

            if diff_count == 1:
                return id1, id2, differ_index
