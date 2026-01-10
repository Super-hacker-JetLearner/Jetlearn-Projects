"homework: make choice program where person chooses linear or quadratic, gets asked for values, and then it gives the values from x=1 to x=10"
import numpy as np
import math


print('-welcome to calculator-')

# print(3**2)

while True:
    print("1. quadratic\n2. linear\n3.quit")
    choice = input('Enter the number of the action you want to take: ')
    if choice == "1":
        print("ax^2 + bx + c")
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        c = float(input("Enter the value of c: "))
        array = np.zeros(10)
        for x in range(0,10):
            array[x] = a*((x+1)*(x+1)) + b*(x+1) + c
        print(array)
        
    if choice == "2":
        print("ax + b")
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        array = np.zeros(10)
        for x in range(0,10):
            array[x] = a*(x+1) + b
        print(array)
    if choice == "3":
        break
        

# x = (-b +- math.sqrt(b**2-4*a*c))/2*a


"solving quadratic equations"
while True:
    print("1. solve quadratic\n2.quit")
    choice = input('Enter the number of the action you want to take: ')
    if choice == "1":
        print("ax^2 + bx + c = 0")
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        c = float(input("Enter the value of c: "))
        if b**2-4*a*c < 0:
            print("0 possible answers")
        else:
            if b == 0:
                print(f"result is {(math.sqrt(b**2-4*a*c))/2*a}")
            else:
                print("2 results possible: ")
                print(f"result 1 is {(-b + math.sqrt(b**2-4*a*c))/2*a}")
                print(f"result 2 is {(-b - math.sqrt(b**2-4*a*c))/2*a}")
    elif choice == "2":
        break
            