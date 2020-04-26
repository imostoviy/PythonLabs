#Дан список 3 слов различной длины разделенных пробелами. Составить программу упорядочения списка слов:
#в порядке присутствия в начале слова заданной буквы;
#Ihor Mostovyi
# 25.04.2020

def main():
    string = input("Enter words\n")
    words = string.split(" ")
    words = list(map(lambda s: s.lower(), words))
    
    letter = input("Enter letter\n")[0]
    letter.lower()

    words.sort(key= lambda s: s[0] == letter, reverse= True)
    print(words)

    return None

main()