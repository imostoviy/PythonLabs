#Составить программу вывода на экран:
#первых 100 нечетных натуральных нечетных чисел и распечатать его в виде матрицы 10X10
#Ihor Mostovyi
#29.04.2020

import numpy as np

def getMatrix():
    array = np.array([i for i in range(1, 200, 2)], int)
    array = array.reshape((10, 10))
    return array

def printing():
    matrix = getMatrix()
    print(len(matrix)*len(matrix[0]))
    print(matrix)
    return None

def main():
    printing()
    return None

#main()