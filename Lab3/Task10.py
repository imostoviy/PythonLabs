# Создать словарь-разговорник по указанной в варианте теме, содержащий 10 слов вида: слово на украинском и его перевод.
# Вывести на экран измененный словарь, в котором первым идет слово на инострранном из входного словаря, а рядом его украинский перевод.
# украинско-польский, тема словаря – здоровье
# Ihor Mostovyi
# 20.04.2020

def main():
    ucrainianPolandDictionaty = {"Здоровий": "Zdrowe",
                                 "Зарядка": "Ładowanie",
                                 "Хвороба": "Choroba",
                                 "Спорт": "Sports",
                                 "Тренування": "Szkolenie",
                                 "Грип": "Grypa",
                                 "М'язи": "Mięśnie",
                                 "Жир": "Tłuszcz",
                                 "Каріес": "Próchnica",
                                 "Сильний": "Silny"}

    poland_ukrainian_dictionary = dict()
    for key, value in ucrainianPolandDictionaty.items():
        poland_ukrainian_dictionary[value] = key

    for key, value in poland_ukrainian_dictionary.items():
        print(key, '-', value)

main()