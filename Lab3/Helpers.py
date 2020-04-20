import random

def makeRandomList(rangeToGetForm: range):
    n = random.randint(1, 10000)
    randomList = []
    for _ in range(0, n + 1):
        rand = random.choice(rangeToGetForm)
        randomList.append(rand)

    return randomList


def getStartRange(): 
    start = (int(input("Enter start of range\n")))
    end = (int(input("Enter end of range\n")))

    if end < start:
        temp = start
        start = end
        end = temp

    return range(start, end + 1)