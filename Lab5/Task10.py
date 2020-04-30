#Создайте текстовый файл, содержащий следующие данные: названия городов для заданных в варианте областей Украины,
# # численность населения городов, площадь городов, количество больниц и ВУЗов. 
# Составить программу, которая сохраняет в строки текстового файла отсортированные по убыванию области в зависимости от:
# a) 1 строка: площади занимаемой территории (после названия области вывести отсортированный список городов каждой области);
# b) 2 строка: плотности населения в них;
# c) 3 строка: количества больниц, приходящихся на 1000 человек;
# d) 4 строка: количества ВУЗов, приходящихся на 1000 человек.
# Ihor Mostovyi
# 29.04.2020

import numpy as np
import os, sys

def main():
    input_file = open(os.path.join(sys.path[0], "text4.txt"), 'r')
    Cities = dict()
    Information = list()

    for line in input_file:
        if (line == "\n"):
            continue
        if (line.__contains__("Місто")):
            inf = line.split()
            for i in range(0, len(inf), 1):
                Information.append(inf[i])
            continue
        strs = line.split()
        key = strs[0]
        value = [i for i in strs[1:len(strs)]]
        Cities[key] = value
    input_file.close()
    print(str(Cities))

    Set_areas = set()
    for key, value in Cities.items():
        Set_areas.add(value[0])
    Area_square = dict()
    Area_density = dict()
    Area_hospital = dict()
    Area_university = dict()
    for area in Set_areas:
        Area_square[area] = list()
        Area_density[area] = list()
        Area_hospital[area] = list()
        Area_university[area] = list()
    for key, value in Cities.items():
        List = Area_square[value[0]]
        List.append([key, float(value[2])])
        Area_square[value[0]] = List
        
        List = Area_density[value[0]]
        List.append([key, float(value[1]) / float(value[2])])
        Area_density[value[0]] = List
        
        List = Area_hospital[value[0]]
        List.append([key, (1000 * float(value[3])) / float(value[1])])
        Area_hospital[value[0]] = List
        
        List = Area_university[value[0]]
        List.append([key, (1000 * float(value[3])) / float(value[1])])
        Area_university[value[0]] = List

    outputFile = open(os.path.join(sys.path[0], 'task3_result.txt'), 'w')
    print("\nAreas_square:")
    outputFile.write("\nAreas_square:\n")
    printing(Area_square, outputFile)
    print("\nAreas_density:")
    outputFile.write("\nAreas_density:\n")
    printing(Area_density, outputFile)
    print("\nArea_hospital:")
    outputFile.write("\nArea_hospital:\n")
    printing(Area_hospital, outputFile)
    print("\nArea_university:")
    outputFile.write("\nArea_university:")
    printing(Area_university, outputFile)
    outputFile.close()

    return None

def printing(Areas, output_file):
    for key, value in Areas.items():
        print(str(key) + ":")
        output_file.write(str(key) + ":")
        for city in value:
            print(str(city))
            output_file.write(str(city))
    return None

main()
