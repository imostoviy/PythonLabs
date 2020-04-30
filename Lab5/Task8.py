#Имеется таблица данных о витаминном составе плодов и ягод: (text2.txt)
#Найти
#a) в каком из фруктов содержание заданного витамина максимально;
#b) массу каждого фрукта, необходимую для получения определенного количества заданного витамина;
#c) количественное содержание витаминов в заданном наборе определенных фруктов.
#Ihor Mostovyi
#29.04.2020

import numpy as np
import os, sys

def main():
    input_file = open(os.path.join(sys.path[0], "text2.txt"), 'r')
    fruits = dict()
    vitamins = list()

    for line in input_file:
        if (line.__contains__("Вид")):
            vit = line.split()
            for i in range(1, len(vit) - 1, 1):
                vitamins.append(vit[i])
            continue

        strs = line.split()
        fruit = strs[0]
        vitaminsValues = [float(i) for i in strs[1:len(strs)]]
        fruits[fruit] = vitaminsValues

    input_file.close()

    print("All vitamins: " ,vitamins)
    for key, value in fruits.items():
        print(key, " - ", value)

    search_vitamin = str(input("\nEnter a vitamin: "))
    indexOfEnteredVitamin = vitamins.index(search_vitamin)
    
    maxvalueOfVitamin = 0
    fruit = ""
    for key, value in fruits.items():
        if (value[indexOfEnteredVitamin] > maxvalueOfVitamin):
            maxvalueOfVitamin = value[indexOfEnteredVitamin]
            fruit = key
    print("\nFruit: ", fruit, ", weight of vitamin = ", maxvalueOfVitamin, "\n")

    requestedWeightOfVitamin = float(input("Enter count of vitamine: "))
    for key, value in fruits.items():
        count = value[indexOfEnteredVitamin]
        weight = value[len(value)-1]
        print("Fruit: ", key, ", weight = ", (requestedWeightOfVitamin * weight) / count)
    
    fruitsList = input("\nEnter fruits, separator mark is ',' ").split(",")
    vitaminsCount = [0 for i in range(0, len(vitamins), 1)]
    for key, value in fruits.items():
        if (fruitsList.__contains__(key)):
            for i in range(0, len(value) - 1, 1):
                vitaminsCount[i] += value[i]
    print("Count of vitamines: ", vitaminsCount)
    
    return None

main()
