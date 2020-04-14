#Даны натуральное число n и действительные числа a1,...,an . Вычислить: min(a2,a4,...) + max(a2,a4,...)
#Ihor Mostovyi
#12.04.2020

def main():
    n = int(input("enter count of digits in sequence \n"))

    if n < 0:
        print("Error n < 0")
        return None
    
    min = 0
    max = 0
    for i in range(n):
        digit = int(input("Enter digit\n"))
        if i % 2 == 0:
            continue
        if digit < min:
            min = digit
        if digit > max:
            max = digit

    print("Min is ", min, ", max is ", max)
    return None

main()