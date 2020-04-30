# Создайте класс SumElements состоящий из методов:
# a) main - в котором создается два двумерных массива (матрицы размером 5х10),
# которые заполняются случайными числами из разных диапазонов, после чего создаются еще две матрицы:
#  - матрица-столбец, каждый элемент которой является суммой элементов исходной матрицы в соответствующей строке;
#  - матрица-строка, каждый элемент которой является суммой элементов исходной матрицы в соответствующем столбце.
# b) PrintMatrix - производит вывод на экран матрицы переданной ему в качестве параметра в форме таблицы.
# Ihor Mostovyi
# 29.04.2020

import numpy as np

class SumElements:
    def main(self):
        start = int(input("Enter the start of diapason 1: "))
        end = int(input("Enter the end of diapason 1: "))
        matrixOne = np.random.randint(start, end, (5, 10))
        
        start = int(input("Enter the start of diapason 2: "))
        end = int(input("Enter the end of diapason 2: "))
        matrixTwo = np.random.randint(start, end, (5, 10))

        self.PrintMatrix(matrixOne)
        self.PrintMatrix(matrixTwo)

        matrixSumOfRows = matrixOne.sum(axis=1).reshape(5, 1)
        matrixSumOfCols = matrixTwo.sum(axis=0).reshape(1, 10)

        self.PrintMatrix(matrixSumOfRows)
        self.PrintMatrix(matrixSumOfCols)
    
    def PrintMatrix(self, matrix):
        print(matrix, "\n")
        return None

def main():
    sumElements1 = SumElements()
    sumElements1.main()
    return None

main()