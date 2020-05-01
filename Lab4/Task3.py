#Составить шуточную программу, которая выдавала бы в заданном формате «оперативную информацию» о тех или иных происшествиях. «Информация» образуется на базе какого-то
# опорного текста с пропусками, которые замещаются данными, выбранными из соответствующих массивов случайным образом. Варианты тематики:
# медицина
# Ihor Mostovyi
# 25.04.2020

from random import choice

def main():
    medicineFacts = ["Some of the earliest named doctors were women",
                     "Cataract surgery was possible in the sixth century BC",
                     "A ‘tree of life’ tackled scurvy",
                     "If you want a cure for everything, try theriac",
                     "General anaesthesia helped cancer patients at the beginning of the 19th century",
                     "A ‘leech craze’ hit 19th-century Europe",
                     "Ugandan surgeons developed life-saving caesarean operations"]

    string = str(input("Input begіn phrase: "))
    print(string + ". " + choice(medicineFacts))
    return None
main()