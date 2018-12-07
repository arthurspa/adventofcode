def solve(read):

    two_count = 0
    three_count = 0
    for line in read:
        line = line[:-1] # remove \n character
        letters_count = {}
        for c in line:
            if c in letters_count:
                letters_count[c] += 1
            else:
                letters_count[c] = 1

        two_found = False
        three_found = False
        for letter in letters_count:
            if letters_count[letter] == 2 and not two_found:
                two_count += 1
                two_found = True
            if letters_count[letter] == 3 and not three_found:
                three_count += 1
                three_found = True

    print(two_count * three_count)
