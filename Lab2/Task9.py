#У Змея-Горыныча 2000 голов. Сказочный богатырь может срубить ему одним ударом меча 33, 21, 17 или 1 голову, но при этом у Змея вырастает взамен соответственно 48, 0, 14 или 349 голов.
#  Если отрублены все головы, то новые не вырастают. Как богатырю одалеть Змея?
# Ihor Mostovyi
# 12.04.2020

def main():
    heads = 2000
    hit33 = 0
    hit21 = 0
    hit17 = 0
    hit1 = 0

    while heads != 0:
        if heads >= 21:
            hit21 += heads // 21
            heads -= (heads // 21) * 21
            continue
        if heads >= 17:
            hit17 += 1
            heads -= 17
            if heads == 0: break
            heads += 14
            continue
        if heads >= 33:
            hit33 += 1  
            heads -= 33
            if heads == 0: break
            heads += 48
            continue
        hit1 += 1
        heads -= 1
        if heads == 0: break
        heads += 349
    
    print("hit33: ", hit33, "\nhit21: ", hit21, "\nhit17: ", hit17, "\nhit1: ", hit1)
    return None

main()