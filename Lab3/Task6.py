#Политическая жизнь некоторой страны очень оживленная.
#  В стране действует K политических партий, каждая из которых регулярно проводит некие политические акции. Дни, когда хотя бы одна из партий объявляет политические акции, при условии, что это не суббота или воскресенье (когда и так никто не работает), наносят большой ущерб экономике страны.
# i-я партия объявляет политические акции строго каждые bi дней, начиная с дня с номером ai .
# То есть i-я партия объявляет политические акции в дни ai , ai + bi , ai + 2bi и т.д.
# Если в какой-то день несколько партий объявляет политические акции, то это считается одной общенациональной политической акцией.
# В календаре страны в 2017 году n дней, пронумерованных от 1 до N.
# Первый день года является понедельником, шестой и седьмой дни недели – выходные. 
# Программа получает на вход число дней в году n и число политических партий 1 <= k <= 250 .
#  Далее идет K строк, описывающие графики проведения политических акций. i-я строка содержит числа ai и bi ( 1 <= ai , bi <= n ).
#  Выведите единственное число: количество политических акций, произошедших в течение года.
# Ihor Mostovyi
# 20.04.2020
def main():
    k = int(input("Enter count of clubs\n"))
    n = int(input("Enter count of days\n"))
    clubs = []

    while len(clubs) != k:
        string = input("Enter ai and bi, 1<=ai, bi<=n\n")
        numbers = string.split(" ", 1)
        a = int(numbers[0])
        b = int(numbers[1])
        
        if a < 1 or b > n:
            print("invalid string\n")
            continue
        
        days = set(filter(lambda x: x % 6 != 0 and x % 7 != 0, list(range(int(numbers[0]), n + 1, int(numbers[1])))))
        clubs.append(days)

    greatDays = clubs[0]
    for days in clubs:
        greatDays = greatDays.intersection(days)
    
    daysWithoutGreatDays = list(map(lambda x: x.difference(greatDays), clubs))
    
    result = len(greatDays)
    for days in daysWithoutGreatDays:
        result += len(days)
    
    print("Result is ", result)
    return None

main()