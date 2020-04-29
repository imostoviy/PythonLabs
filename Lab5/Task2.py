#Заданы 2 одномерных массива состоящие из n целых чисел, которые заполняются
#случайным образом. Составить программу формирования третьего массива: включая в него сначала все элементы первого, затем второго массивов
#Ihor Mostovyi
#29.04.2020

import numpy as np

def main():
    n = int(input("Enter the count of elements in array n: "))
    firstArrray = np.random.randint(0, 100, n)
    secondArrray = np.random.randint(0, 100, n)

    print("First array: ", firstArrray, "\n")
    print("Second array: ", secondArrray, "\n")
    print("Third array: ", np.concatenate((firstArrray, secondArrray), axis=0), "\n")

    return None
main()