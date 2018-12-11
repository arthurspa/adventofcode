import re


def solve(read):
    for line in read:
        sequence = line.strip()

    sequence = fully_react(sequence)
    print(len(sequence))


def fully_react(sequence):
    prev_seq_size = len(sequence)
    pattern = r'([a-zA-Z])(?!\1)(?i:\1)'
    sequence = re.sub(pattern, '', sequence)
    while prev_seq_size != len(sequence):
        prev_seq_size = len(sequence)
        sequence = re.sub(pattern, '', sequence)

    return sequence
