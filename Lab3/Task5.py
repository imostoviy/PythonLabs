#Анна и Николай играют в игру.
#Август загадал натуральное число от 1 до n (задается пользователем).
#Анна пытается угадать это число, для этого она называет некоторые множества натуральных чисел. 
#Николай отвечает Анне YES, если среди названных ей чисел есть задуманное или NO – в противном случае. 
#После нескольких заданных вопросов Анна запуталась в том, какие вопросы она задавала и какие ответы получила и просит вас помочь ей определить, какие числа мог задумать Николай.
#Первая строка входных данных содержит число 2n – наименьшее число, которое мог загадать Николай.
#Далее идут строки, содержащие вопросы Анны. 
#Каждая строка представляет собой набор чисел, разделенных символами подчеркивания. 
#После каждой строки с вопросом идет ответ Николая: YES или NO. 
#Наконец, последняя строка входных данных содержит одно слово HELP.Вы должны вывести (через апостроф, в порядке возрастания) все числа кратные 11, которые мог задумать Николай.
#Ihor Mostovyi
#20.04.2020

def testString(n, string):
    splitedList = string.split("_")
    if str(n) in splitedList:
        print("YES\n")
        return None
    print("NO\n")
    return None

def main():
    n = int((int(input("Enter 2*n\n"))) / 2)
    string = input("Enter sequence devided buy '_'")
    
    while string != "HELP":
        testString(n, string)
        string = input("Enter sequence devided buy '_'")

    listOfDigits = list(filter(lambda x: x % 11 == 0, list(range(1, n + 1))))
    print("Possible digits are: \n")
    for i in listOfDigits:
        print(i, "' ")
    return None

main()