#Дано натуральное число n, записанное в виде строки. Записать это число с сокращенными обозначениями разрядов принятых в математике (например, 1523 – 1 тыс. 5 сот. 2 дес. 3 ед.).
#6975
#Ihor Mostovyi
#25.04.2020

def main():
    number = input("Enter number with length of [1;4]\n")
    length = len(number)

    if length < 1 or length > 4:
        print("Fatal error")
        return None

    try:
        _ = int(number)
    except:
        print("Where is the digit?!")
        return None

    if length == 1:
        print(number[0], "од.")
        return None
    if length == 2:
        print(number[0], "дес. ", number[1], "од.")
        return None
    if length == 3:
        print(number[0], "сот. ", number[1], "дес. ", number[2], "од.")
        return None
    if length == 4:
        print(number[0], "тис. ", number[1], "сот. ", number[2], "дес. ", number[3], "од.")
        return None

    return None

main()
    
    