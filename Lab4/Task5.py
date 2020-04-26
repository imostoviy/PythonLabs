# Даны 5 строк s1, s2, s3, s4 и s5. На основе заданного условия выполнить предложенные действия:
#если строки s4 и s5 имеют равное количество символов, то необходимо увеличить все остальные строки, добавив в их конец 3 знака «!»;
# Ihor Mostovyi
# 25.04.2020

def main():
    stringOne = input("Enter first string\n")
    stringTwo = input("Enter second string\n")
    stringThree = input("Enter third string\n")
    stringFour = input("Enter fourth string\n")
    stringFive = input("Enter fifth string\n")

    if len(stringFour) == len(stringFive):
        stringOne += "!!!"
        stringTwo += "!!!"
        stringThree += "!!!"

    print("String one: ", stringOne, "\nString two: ", stringTwo, "\nString three: ", stringThree, "\nString four: ", stringFour, "\nString five: ", stringFive)
    return None

main()