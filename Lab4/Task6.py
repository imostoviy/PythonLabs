#Задана строка произвольной длинны содержащая информацию по специальности, на которой вы учитесь (в виде одного предложения, обязательно содержащего фразу «Прикладная математика»). Определить:
#содержит ли строка буквы «т» и если да, то указать их индекс
#Ihor Mostovyi
#25.04.2020

def main():
    string = "Моя спеціальність - системний аналіз. До чого тут \"Прикладная математика\" ".lower()
    indexes = []
    
    for i in range(0, len(string)):
        if string[i] == "т":
            indexes.append(i)
    
    print(indexes)
    return None

main()