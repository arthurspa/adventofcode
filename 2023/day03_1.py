from io import TextIOWrapper

# --- Day 3: Gear Ratios ---

# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

# "Aaah!"

# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:

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
# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.


# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?


engineSchematic = []


def solve(input: TextIOWrapper):
    partNumbers = []
    for line in input:
        chars = []
        line = line.strip()
        for c in line:
            chars.append(c)

        engineSchematic.append(chars)

    for i in range(len(engineSchematic)):
        currentPartNumberStr = ""
        adjSymbolFound = False
        for j in range(len(engineSchematic[i])):
            c = engineSchematic[i][j]
            if c.isdigit():
                currentPartNumberStr += c
                if hasAdjSymbol(i, j):
                    adjSymbolFound = True
            if (
                j + 1 == len(engineSchematic[i])
                or not engineSchematic[i][j + 1].isdigit()
            ):
                if currentPartNumberStr != "":
                    if adjSymbolFound:
                        partNumbers.append(int(currentPartNumberStr))
                    currentPartNumberStr = ""
                adjSymbolFound = False

    # 549908 is the right answer
    print(sum(partNumbers))


def hasAdjSymbol(i, j):
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
            # print(f"{i}, {j} - {engineSchematic[i][j]}")
            return True
    return False


def isSymbol(i, j):
    return not engineSchematic[i][j].isdigit() and engineSchematic[i][j] != "."


def isInRange(i, j):
    return (
        i >= 0 and i < len(engineSchematic) and j >= 0 and j < len(engineSchematic[i])
    )
