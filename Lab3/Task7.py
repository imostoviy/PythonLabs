#Дан список слов (пользователь вводит фразу, содержащую не менее 15 слов)
#x1,...,xn и слово y (ключевое слово выбирается указанием его индекса во
#фразе). Определить входит ли хотя бы одно из слов xi в y (как подслово).
# Количество действий не должно превосходить константы согласно варианту, умноженной на суммарную длину всех слов (из основного списка и того в котором происходит поиск).
# K=1/2
# Ihor Mostovyi
# 20.04.2020

def calculateConst(string):
    listOfWords = string.split(" ")
    lengthOfWords = 0
    for word in listOfWords:
        lengthOfWords += len(word)
    return lengthOfWords


def main():
    string = input("Enter phrases, splited by whitespaces\n")
    listOfWords = string.split(" ")

    k = calculateConst(string)
    k1 = 1
    inp = "Enter key word(you nead to choose index between 0 and " + str(len(listOfWords) - 1) + "\n"

    n = int(input(inp))

    if n < 0 or n >= len(listOfWords):
        print("Did u read condition??!")
        return None

    keyword = listOfWords[n]
    keywordLen = len(keyword)
    
    contain = False

    for word in listOfWords:
        if word == keyword:
            k1 += 1
            continue

        if len(word) < keywordLen:
            k1 += 1
            continue

        if keyword in word:
            k1 += 1
            contain = True
            break

    print("Does contain ", contain, "\n", k1,  "complexity should be less than ", k)
    return None


main()