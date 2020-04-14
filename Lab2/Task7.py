#Необходимо составить программу расчета конечной суммы и сравнения полученного результата с контрольным значением.
#1^2 + 3^2 +5^2 +...+(2N-1)^2. Controll N(4N^2 - 1) / 3 
#Ihor Mostovyi
#12.04.2020

def sequence(i):
    if i == 1:
        return 1
    return (2 * i - 1) ** 2 + sequence(i - 1)

def controll(i):
    return i * (4 * (i ** 2) - 1) / 3

def main():
    n = int(input("Enter n\n"))
    if sequence(n) == controll(n):
        print("All is ok!")
    else:
        print("wrong")
    return None

main()