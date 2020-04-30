#Для ведения рейтинга группы сформировать таблицу, содержащую список студентов,
#  список предметов одного семестра и результирующий рейтинг по ним (использовать данные прошлого семестра – результаты сессии/аттестации).
#  Составить программу обработки этих данных, позволяющую:
# a) вычислить средний рейтинг группы по всем предметам
# b) вычислить средний рейтинг группы по каждому из предметов;
# c) вывести на экран фамилии студентов с наибольшим рейтингом;
# d) вывести на экран фамилии студентов с наименьшим рейтингом.
#Результаты сохранить в текстовый файл.
#Ihor Mostovyi
#29.04.2020

import numpy as np
import operator
import os, sys

def main():
    inputFile = open(os.path.join(sys.path[0], "text3.txt"), 'r')
    
    students = dict()
    subjects = dict()
    for line in inputFile:
        if (line.__contains__("ПІБ")):
            subj = line.split()
            for i in range(1, len(subj), 1):
                subjects[subj[i]] = 0
            continue
        strs = line.split()
        student = strs[0]
        marks = [int(i) for i in strs[1:len(strs)]]
        students[student] = marks
    inputFile.close()
    
    subjectIndex = 0
    for key1, _ in subjects.items():
        marksSum = 0
        for _, value2 in students.items():
            marksSum += value2[subjectIndex]
        subjectIndex += 1
        subjects[key1] = (marksSum / len(students))
    
    outputFile = open(os.path.join(sys.path[0], 'task2_result.txt'), 'w')
    print("Average rating of subjects:")
    outputFile.writelines("Average rating of subjects:")
    for key, value in subjects.items():
       print(str(key) + " - " + str(value))
       outputFile.writelines(str(key) + " - " + str(value))

    rating = dict()
    for key, value in students.items():
        MarksSum = 0
        for mark in value:
            MarksSum += mark
        rating[key] = (MarksSum / len(value))
    print()
    outputFile.write("\n")
    print("Average rating of group:")
    outputFile.writelines("Average rating of group:")
    for key, value in rating.items():
        print(str(key) + " - " + str(value))
        outputFile.writelines(str(key) + " - " + str(value))
    print()
    outputFile.write("\n")

    rating = sorted(rating.items(), key=operator.itemgetter(1))
    maxRating = rating[len(rating)-1]
    print("Max rating:", maxRating)
    outputFile.writelines("Max rating:")
    for rate in rating:
        if (rate[1] == maxRating[1]):
            print(rate)
            outputFile.writelines(str(rate) + " ")
    print()
    outputFile.write("\n")
    
    minRating = rating[0]
    print("Min rating:")
    outputFile.writelines("Min rating:")
    for rating in rating:
        if (rating[1] == minRating[1]):
            print(rating)
            outputFile.writelines(str(rating) + " ")

    outputFile.close()
    return None

main()
