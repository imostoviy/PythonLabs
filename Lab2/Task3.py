#Вычислить sum(ai - bi), where i in [1; 30],
# ai = if i % 2 != 0 (i+1)/i else 7*i,
# bi = if i % 2 != 0 5 * i  ** 2 else (i ** 3)/(2*i)
#Ihor Mostovyi
#12.02.2020

def main():
    calcAi = lambda i: (i + 1) / i if i % 2 != 0 else 7 * i
    calcBi = lambda i: 5 * (i ** 2) if i % 2 != 0 else (i ** 3) / (2 * i)

    sum = 0
    for i in range(1, 31):
        sum += calcAi(i) - calcBi(i)
    
    print("Sum is ", sum)

main()