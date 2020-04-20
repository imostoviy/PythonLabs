#Даны два списка чисел, которые могут содержать до 10000 чисел каждый. Выведите все числа, которые входят как в первый, так и во второй список в порядке:
#возрастания и все кратны 3;
# Ihor Mostoviy
# 20.04.2020

import random
from datetime import datetime
from Helpers import getStartRange, makeRandomList

def main():
    ragneToGetFrom = getStartRange()

    setOne = set(makeRandomList(ragneToGetFrom))
    setTwo = set(makeRandomList(ragneToGetFrom))
    intersection = list(setOne.intersection(setTwo))
    intersection.sort()
    print(list(filter(lambda x: x % 3 == 0, intersection)))
    return None

main()