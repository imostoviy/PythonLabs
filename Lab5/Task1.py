#Сохраните текстовый файл, содержащий несколько строк стихотворения украинского поэта.
# Считайте данные из файла в строковый массив и организуйте вывод данных на экран. 
# Подсчитайте количество слов и букв в словах, найдите слово максимальной и минимальной длины, отсортируйте массив по возрастанию и сохраните данные в файл.
# Создайте одномерный массив из значений, соответствующих количествам букв в словах и вычислите, используя функции NumPy:
# cреднее гармоническое элементов данного массива и логарифма его максимального элемента;
# Ihor Mostovyi
# 29.04.2020

import numpy as np
from math import log10 as log
import os, sys

def main():
    input_file = open(os.path.join(sys.path[0], 'text1.txt'), 'r')
    lines = []

    for line in input_file:
        if (line == "\n"):
            continue
        str_arr = line.split(" ")
        for j in range(0, len(str_arr), 1):
            lines.append(str_arr[j].rstrip())
    input_file.close()

    words = np.array([word for word in lines], str)
    words = sorted(words, key=lambda x: len(x), reverse=False)
    wordsLengths = np.array([len(word) for word in words], int)
    minLengthWord = words[0]
    maxLengthWord = words[len(words) - 1] 
    print("Count of words: " + str(len(words)), "\n")
    print("Word with min len (", len(minLengthWord), "): ", minLengthWord)
    print("\nWord with max len (", len(maxLengthWord), "): ", maxLengthWord)

    harmonicMean = len(wordsLengths) / np.sum(1.0/wordsLengths)
    print("Harmonic mean is: ", harmonicMean)

    print("Log of max length word is: Log(", len(maxLengthWord), ") = ", log(len(maxLengthWord)))
    
    output_file = open(os.path.join(sys.path[0], 'task1_result.txt'), 'w')
    output_file.write("List of words: " + str(lines) + "\n")

    output_file.write("Count of words: " + str(len(words)) + "\n")

    output_file.write("Count of letters in each word: " + str(len(words)) + "\n")
    a = np.array([len(word) for word in lines], int)

    output_file.write("Initial array: " + str(a) + "\n")
    
    output_file.write("Sorted array: " + str(wordsLengths) + "\n")

    Sum = a.sum()
    print("Sum of elements of array = ", Sum)
    
    output_file.close()

    return None
main()