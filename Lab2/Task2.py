#Найти сумму чисел определенных в предыдущей задаче.
#Ihor Mostovyi
#12.04.2020

from Task1 import count

def main():
    sum = 0
    for digit in count():
        sum += digit
    
    print("Sum is ", sum)
    return None

main()