#В известной считалочке «Десять негритят» при каждом ее повторении количество негритят уменьшается на 1: 
# Десять негритят пошли купаться в море, десять негритят резвились на просторе, один из них утоп, ему купили гроб. Девять негритят пошли купаться в море...
# Составить программу, которая по заданному в некотором диапазоне случайным образом числу n будет выводить на экран грамматически правильный текст,
#  считалочки согласно варианту (например для считалочки с негритятами, при n=1 – «один негритенок пошел ...», при n=2 – «два негритенка пошли ...» и так далее).
# e) n in [1; 4]
# Ihor Mostovyi
# 25.04.2020

from random import randint

def main():
    afroamericansCount = randint(1, 5)
    result = str(afroamericansCount) + " "
    if afroamericansCount == 1:
        print(result + "негритенок пошел")
        return None
    if (afroamericansCount >= 2) and (afroamericansCount <= 4):
        print(result + "негритенка пошли")
        return None
    if (afroamericansCount >= 5) and (afroamericansCount <= 10):
        print(result + "негритят пошли")
        return None
    print(result)


main()