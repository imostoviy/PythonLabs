#Даны натуральные числа n, a1,...,an . Вычислить f (a1) + f(a2) + ... +f (an), где
# f(x) =
# x ** (x + 1) if x % 11 = 0 
# 15 * x if x % 11 == 1
# x / (x - 1) in other cases

def func(x): 
    if x % 11 == 0:
        return x ** (x + 1)
    if x % 11 == 1:
        return 15 * x
    return x / (x - 1)

def main():
    n = int(input("enter count of digits in sequence \n"))

    if n < 0:
        print("Error n < 0")
        return None
    
    sum = 0
    for _ in range(n):
        sum += func(int(input("Enter digit\n")))

    print("Sum is", sum)
    return None

main()