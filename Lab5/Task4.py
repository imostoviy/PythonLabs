#Усовершенствуйте программу (задача 6) таким образом, чтобы создать класс
#Determinant состоящий из методов:
#a) main – содержит код задачи 6, в котором полученная матрица обрезана до размера
#3х3, а также обеспечивается ее вывод на экран в табличном формате путем вызова метода PrintMatrix и производится вычисление детерминанта матрицы путем вызова метода det;
#b) det – статический метод, возвращающий для переданной ему в качестве параметра матрицы значение ее детерминанта, вычисленного по правилу треугольника;
#c) PrintMatrix – производит вывод на экран матрицы переданной ему в качестве параметра в форме таблицы 3х3.
#Ihor Mostovyi
#29.04.2020

import numpy as np
import Task3 as t3

class Determinant:
    def MainMethod(self):
        matrix = t3.getMatrix()
        matrix = matrix[:3, :3]
        self.PrintMatrix(matrix)
        det = self.det(matrix)
        print(det)
        self.check(det, matrix)
    
    def PrintMatrix(self, matrix):
        print(matrix)
    
    def det(self, matrix):
        det = 0
        det += matrix[0, 0] * matrix[1, 1] * matrix[2, 2]
        det += matrix[2, 0] * matrix[0, 1] * matrix[1, 2]
        det += matrix[1, 0] * matrix[0, 2] * matrix[2, 1]
        det -= matrix[2, 0] * matrix[1, 1] * matrix[0, 2]
        det -= matrix[1, 0] * matrix[0, 1] * matrix[2, 2]
        det -= matrix[0, 0] * matrix[2, 1] * matrix[1, 2]
        return det
    
    def check(self, det, matrix):
        library_value = np.linalg.det(matrix)
        print("Library value of determinant = ", str(library_value))
        if (abs(det - library_value) <= 0.0000001):
            print("U deam good, boy")
        else:
            print("Go and read Math books!")

def main():
    detMatrix = Determinant()
    detMatrix.MainMethod()

main()