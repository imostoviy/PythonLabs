#Усовершенствуйте программу (задача 6) таким образом, чтобы создать класс SumMatrix состоящий из методов:
#a) main – содержит код задачи 6, в котором полученная матрица обрезана до размера 3х3, а также создается второй двумерный массив (матрица размером 3х3),
#  который заполняется случайными числами в диапазоне от 0 до 5, затем с помощью метода SumMatrix производится их сложение и с помощью метода det вычисляется детерминант результирующей матрицы.
#  Каждая операция должна сопровождаться выводом на экран матриц посредством вызова метода PrintMatrix;
# b) SumMatrix – производит сложение матриц переданных ему в качестве параметров
#Ihor Mostovyi
#29.04.2020

import numpy as np
from Task3 import getMatrix

class SumMatrix:
    def MainMethod(self):
        m1 = getMatrix()
        m1 = m1[:3, :3]
        m2 = np.random.randint(0, 5, (3, 3))
        self.PrintMatrix(m1)
        self.PrintMatrix(m2)

        sumOfMatrix = self.SumMatrix(m1, m2)
        self.PrintMatrix(sumOfMatrix)
        self.det(sumOfMatrix)
        return None

    def PrintMatrix(self, matrix):
        print(matrix)
        return None

    def SumMatrix(self, a, b):
        result = a + b
        return result

    def det(self, matrix):
        print("determinant: ", np.linalg.det(matrix))
        return None

def main():
    sumMatrix = SumMatrix()
    sumMatrix.MainMethod()
    return None
main()