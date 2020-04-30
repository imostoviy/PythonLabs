#Усовершенствуйте программу (задача 7) таким образом, чтобы создать класс Expression
#состоящий из методов:
#a) main – содержит код задачи 6, в котором полученная матрица обрезана до размера
#3х3, а также создается второй двумерный массив (матрица размером 3х3), который заполняется случайными числами в диапазоне от 0 до 5,
# затем с помощью метода ExpressionMatrix производится их сложение по формуле и с помощью метода det вычисляется детерминант результирующей матрицы. 
# Каждая операция должнасопровождаться выводом на экран матриц посредством вызова метода PrintMatrix.
#b) ExpressionMatrix – производит вычисление 3*A+5*B.
#Ihor Mosovyi
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

        result = self.ExpressionMatrix(m1, m2)
        self.PrintMatrix(result)
        print("determinant: ", self.det(result))
        return None

    def PrintMatrix(self, matrix):
        print(matrix, "\n")
        return None

    def ExpressionMatrix(self, a, b):
        a = 3*a
        b = 5*b
        self.PrintMatrix(a)
        self.PrintMatrix(b)
        return a + b

    def det(self, matrix):
        return np.linalg.det(matrix)

def main():
    sumMatrix = SumMatrix()
    sumMatrix.MainMethod()
    return None
main()