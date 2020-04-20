#Сгенерировать два списка чисел со значениями из заданного диапазона, которые могут содержать до 100000 чисел каждый. Посчитайте, сколько чисел:
#нечетных, повторяющихся в обоих списках, а также их количество;
#Ihor Mostovyi
#20.04.2020

import collections
from datetime import datetime
from Helpers import getStartRange, makeRandomList

def calculate(listTocount: list):
    dictionary = {}
    for item, count in collections.Counter(listTocount).items():
        if (count > 1 and item % 2 != 0):
            dictionary[item] = count

    return dictionary

def main():
    rangeToGetForm = getStartRange()

    dictOne = calculate(makeRandomList(rangeToGetForm))
    dictTwo = calculate(makeRandomList(rangeToGetForm))

    print("count of digits that satisfy the condition if first list \n", dictOne, "\n and in second\n", dictTwo)
    print("\n", datetime.now())
    
    return None

main()
