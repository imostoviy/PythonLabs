from math import pi
def main():
    radius = float(input("Enter the radius"))
    height = float(input("Enter height"))
    conevol = 1 / 3 * pi * radius * 2 * height
    cylvol = pi * radius * 2 * height
    spherevol = 3 / 4 * pi * radius ** 3

    print("The volume of conus is ", conevol)
    print("The volume of cylinder is ", cylvol)
    print("The volume of sphere is ", spherevol)
    return None

main()
