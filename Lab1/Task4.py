#Author: Ihor Mostovyi
#Date: 11/03/2020

import math 

def devisionByZero():
    print("Deviding by zero. Abort")
    return None

def funcOne(x, a, b, c):
    if 1 + a * b == 0 or a + b == 0 or c == 0:
        devisionByZero()
        return None
    
    devisor = x ** 2 + 1 / (1 + a * b)
    if devisor == 0 :
        devisionByZero()
        return None
    
    print("Fist func ", (x ** 3 + a * b / c) / devisor + a * b * c / (a + b), "\n")
    return None

def funcTwo(x, a, b, c):
    if x < 0 :
        print("Can't count sqrt from subzero number. Abort")
        return None
    
    if math.cos(x) == 0 :
        print("Can't count tan. Abort")
        return None

    print("Second func ", (math.sin(x) ** (x ** 0.5) - math.cos(x)) / 3 * math.tan(x) )
    return None

x = float(input("Enter x "))
a = float(input("Enter a "))
b = float(input("Enter b "))
c = float(input("Enter c "))

funcOne(x, a, b, c)
funcTwo(x, a, b, c)
