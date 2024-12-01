from io import TextIOWrapper


def solve(input: TextIOWrapper):
    left = []
    freq = dict()
    for line in input:
        l, r = [int(x) for x in line.split(" ") if x != ""]
        left.append(l)
        if r in freq:
            freq[r] += 1
        else:
            freq[r] = 1

    diff = []
    for i in range(len(left)):
        mult = 0
        if left[i] in freq:
            mult = freq[left[i]]

        diff.append(left[i] * mult)

    print(sum(diff))
