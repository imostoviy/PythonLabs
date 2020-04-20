#Извлечение и удаление элементов списка.
#Создать список, состоящий из целых чисел указанного диапазона.
# Удалить из каждого списка первый элемент все последующие со значением кратным 10 и найти их количество.
#Ihor Mostovyi 
#20.04.2020

from datetime import datetime

def main():
    start = (int(input("Enter start of range\n")))
    end = (int(input("Enter end of range\n"))) + 1

    if end < start:
        temp = start
        start = end
        end = temp
    
    myList = list(range(start, end))
    del myList[0]

    result = list(filter(lambda i: i % 10 != 0, myList))
    count = len(result)

    print(result, "\n")
    print("count of ellemnts ", count, "\n")
    print(datetime.now())

    return None

main()