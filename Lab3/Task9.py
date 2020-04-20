#Список содержит названия городов Украины, области к которым они относятся, количество жителей в них и общую площадь территории. На основе данного создать списки, которые:
# разбивают текущий на группы: в одном – города, отсортированные по алфавиту, в другом – по возрастанию количества жителей;
# Ihor Mostovyi
# 20.04.2020

def main():
    regions = [["Vinitsya", "Vinnitska", 1575808, 26513],
               ["Lytsk", "Volunska", 1038457, 20143],
               ["Dnipro", "Dnipropetrovska", 3231140, 31914],
               ["Donetsk", "Donetska", 4200461, 26517],
               ["Shitomur", "Shitomurska", 1231239, 29832],
               ["Ushgorod", "Zakarpatska", 1258115, 12777], 
               ["Zaporishya", "Zaporizka", 1723171, 27180],
               ["Ivano-Frankivsk", "Ivano-Frankivska", 1377496, 13928],
               ["Kyiv", "Kyivska", 1754284, 28131],
               ["Kropuvnuckui", "Kirivigradska", 956250, 24588],
               ["Luhansk", "Luhanska", 2167802, 26684],
               ["Lviv", "Lvivska", 2529608, 21883],
               ["Mukolaiv", "Mukolaivska", 1141324, 24598],
               ["Odesa", "Odeska", 2383075, 33310],
               ["Poltava", "Poltavska", 1466786, 28748],
               ["Rivne", "Rivnenka", 1160647, 20047],
               ["Symu", "Symska", 1094284, 23834],
               ["Ternopil", "Ternopilska", 1052312, 13823],
               ["Harkiv", "harkivska", 2694007, 31415],
               ["Herson", "Hersonska", 1046981, 28461],
               ["Kamyanec-Podilskuy", "Hmelnucka", 1274409, 20629],
               ["Cherkasy", "Cherkaska", 1220364, 20900],
               ["Chernivci", "Chernivecka", 906600, 8097],
               ["Chernigiv", "Chernivecka", 1020078, 31865]]

    regionsCopy = [region for region in regions]
    regions.sort(key = lambda x: x[1])
    regionsCopy.sort(key = lambda x: x[2])

    print("Sorted by town names\n", regions, "\n")
    print("Sorted by population\n", regionsCopy)
    return None

main()