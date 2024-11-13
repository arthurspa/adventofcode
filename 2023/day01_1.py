
from io import TextIOWrapper


def solve(input: TextIOWrapper):
    acc = 0
    for line in input:
        firstDigit = -1
        for c in line:
            lastDigit = -1
            if c.isdigit() and firstDigit == -1:
                firstDigit = int(c)
                break
        lastDigit = -1
        for c in line[::-1]:
            if c.isdigit() and lastDigit == -1:
                lastDigit = int(c)
                break
        
        acc = acc + firstDigit*10 + lastDigit
    
    print(acc)


