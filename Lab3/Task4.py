#Анна и Борис любят играть в разноцветные кубики, причем у каждого из них свой набор и в каждом наборе все кубики различны по цвету.
# Однажды дети заинтересовались, сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах.
# Для этого они занумеровали все цвета случайными числами. На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.
# Номер любого цвета – это целое число в пределах от 0 до 10 ** 9 . В первой строке входного файла записаны числа N и M – количество кубиков у Анны и Бориса соответственно.
# В следующих N строках заданы номера цветов кубиков Анны. В последних M строках номера цветов кубиков Бориса.
# Выведите сначала количество, а затем отсортированные по возрастанию номера цветов таких, что кубики каждого цвета есть в обоих наборах,
# затем количество и отсортированные по убыванию кратные 5 номера остальных цветов у Анны,
# потом количество и отсортированные по возрастанию кратные 3 номера остальных цветов у Бориса.

def getNumbers():
    n = int(input("count of Ann's cubes\n"))
    m = int(input("count of Borise's cubes\n"))
    endOfRange = 10 ** 9

    annsList = set()
    borisList = set()

    while len(annsList) != n:
        digit = int(input("enter number of color for Ann\n"))
        if digit >= 0 and digit < endOfRange:
            annsList.add(digit)
        else:
            print("Enter number from 0 to 10^9\n")

    while len(borisList) != m:
        digit = int(input("enter number of color for Boris\n"))
        if digit >= 0 and digit < endOfRange:
            borisList.add(digit)
        else:
            print("Enter number from 0 to 10^9\n")
    
    return annsList, borisList

def main():
    annsList, borisList = getNumbers()

    intersectionList = list(annsList.intersection(borisList))
    intersectionList.sort()
    print("intersection colors count is", len(intersectionList), "\n colors are\n", intersectionList, "\n")
    
    leftForAnn = list(annsList.difference(set(intersectionList)))
    leftForAnn.sort(reverse = True)
    result = list(filter(lambda x: x % 5 == 0, leftForAnn))
    print("Left for ann with condition\n", result, "\n")
    
    leftForBoris = list(borisList.difference(set(intersectionList)))
    leftForBoris.sort()
    result = list(filter(lambda x: x % 3 == 0, leftForBoris))
    print("Left for boris with condition\n", result, "\n")

    return None

main()


