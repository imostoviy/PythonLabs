#Протабулировать функцию на отрезке [a,b] с шагом h:
#Y = sqrt(2.57 - 0.3 * x) if x < 0 else tan(lgamma(x ** 2 + Pi))
#a = -3, b = 3, h = 0.3

from math import pi, lgamma, tan, sqrt

def function(x: float):
    return sqrt(2.57 - 0.3 * x) if x < 0 else tan(lgamma(x ** 2 + pi))

def main():
    x: float = -3
    while x <= 3:
        print("X = ", x, " Y =", function(x))
        x += 0.3
    
    return None

main()
