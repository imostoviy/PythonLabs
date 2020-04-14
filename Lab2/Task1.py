#Даны натуральные числа n, a1,...,an .Определить количество членов ak последовательности:
#удовлетворяющих условию ak < (a(k-1) + a(k+1))/2;
#Ihor Mostovyi
#12.04.2020

def count():
    satisfiedDigits = []
    n = int(input("Enter count of digits. N >= 3\n"))
    if n < 3:
        print("Did u read condition?????!")
        return []
    
    check = lambda first, second, third: second < (first + second) / 2
    first = int(input("enter digit\n"))
    second = int(input("enter digit\n"))
    
    for _ in range(n - 2):
        third = int(input("enter digit\n"))
        
        if check(first, second, third) : 
            satisfiedDigits.append(second)

        first = second
        second = third
    
    return satisfiedDigits

def main():
    print("count of digits, that satisfy the condition is ", len(count()))