#Создать стек, информационными полями которого являются: улица, номер дома и номер квартиры.
#Добавить в стек сведения о новой квартире. 
#Организовать просмотр данных стека, предварительно удалив из него все адреса с нечетными номерами домов, и определить количество домов на заданной улице.
#Ihor Mostovyi
#20.04.2020

def main():
    stack = [["Street 1", 12, 3],
             ["Street 1", 13, 4],
             ["Street 2", 2, 3],
             ["Street 3", 126, 13],
             ["Street 3", 11, 33],
             ["Street 3", 121, 13],
             ["Street 3", 141, 86]]

    print("Stack at start\n", stack )
    
    print("Add new flat\n")
    street = input("Enter street")
    house = int(input("Enter house number"))
    flat = int(input("Enter flat number"))
    stack.insert(0, [street, house, flat])
    print("Stack state \n", stack)

    filtred = list(filter(lambda x: x[1] % 2 == 0, stack))
    print("Stack lookup\n", filtred)

    filtred2 = list(filter(lambda x: x[0] == "Street 3", stack))
    houses = set()
    for adress in filtred2:
        houses.add(adress[1])
    
    print("Count of houses on Street 3 is ", len(houses))
    return None

main()