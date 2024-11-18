from io import TextIOWrapper

# --- Part Two ---

# The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

# You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

# Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

# The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

# This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

# Consider the same engine schematic again:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

# What is the sum of all of the gear ratios in your engine schematic?


engineSchematic = []


def solve(input: TextIOWrapper):
    potentialGears = dict()
    for line in input:
        chars = []
        line = line.strip()
        for c in line:
            chars.append(c)

        engineSchematic.append(chars)

    for i in range(len(engineSchematic)):
        currentPartNumberStr = ""
        adjSymbolFound = False
        uniqueAdjSymbols = []
        for j in range(len(engineSchematic[i])):
            c = engineSchematic[i][j]
            if c.isdigit():
                currentPartNumberStr += c
                adjSymbols = allAdjSymbols(i, j)
                if len(adjSymbols) > 0:
                    adjSymbolFound = True
                    for adjSymbol in adjSymbols:
                        if adjSymbol not in uniqueAdjSymbols:
                            uniqueAdjSymbols.append(adjSymbol)
            if (
                j + 1 == len(engineSchematic[i])
                or not engineSchematic[i][j + 1].isdigit()
            ):
                if currentPartNumberStr != "":
                    if adjSymbolFound:
                        for adjSymbol in uniqueAdjSymbols:
                            if engineSchematic[adjSymbol[0]][adjSymbol[1]] == "*":
                                if adjSymbol not in potentialGears:
                                    potentialGears[adjSymbol] = []
                                    potentialGears[adjSymbol].append(
                                        int(currentPartNumberStr)
                                    )
                                else:
                                    potentialGears[adjSymbol].append(
                                        int(currentPartNumberStr)
                                    )
                    currentPartNumberStr = ""
                    uniqueAdjSymbols = []
                adjSymbolFound = False

    sumOfGears = 0
    for key in potentialGears:
        if len(potentialGears[key]) == 2:
            sumOfGears += potentialGears[key][0] * potentialGears[key][1]
    print(sumOfGears)


def allAdjSymbols(i, j):
    allSymbols = []
    surroudings = [
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
        (i - 1, j - 1),
        (i - 1, j + 1),
        (i + 1, j - 1),
        (i + 1, j + 1),
    ]
    for i, j in surroudings:
        if isInRange(i, j) and isSymbol(i, j):
            allSymbols.append((i, j))
    return allSymbols


def isSymbol(i, j):
    return not engineSchematic[i][j].isdigit() and engineSchematic[i][j] != "."


def isInRange(i, j):
    return (
        i >= 0 and i < len(engineSchematic) and j >= 0 and j < len(engineSchematic[i])
    )
