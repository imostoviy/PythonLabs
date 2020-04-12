#Author: Ihor Mostovyi
#Date: 11/03/2020
from Check import *

a = float(input("Enter one side "))
b = float(input("Enter second side "))
h = float(input("Enter height "))

if check(a, b, h) :
    print("Squere is ", 1 / 2 * h * (a + b))
else :
    print("Incorrect data")
