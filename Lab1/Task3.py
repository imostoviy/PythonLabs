#Author: Ihor Mostovyi
#Date: 11/03/2020

def main():
    n = float(input("Enter years"))
    n1 = float(input("Enter months"))
    percent = float(input("Enter percent")) / 100
    sum_0 = float(input("Enter first sum"))
    years = n + n1 / 12
    func = lambda s, p, n : s * (1 + p) ** n
    print("sum after ", years, " years is ", func(sum_0, percent, years))
    return None

main()