import math
pi = math.pi
choice = input("Choose 'R' or 'r' for rectangle and 'C' or 'c' for Circle: ")

if choice == 'R' or choice == 'r':
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    res = length * width
    print("The area of the rectangle is" ,res)
else:
    radius = float(input("Enter the radius of the circle: "))
    res = pi * (radius **2)
    print("The area of the circle is" , round(res,2))
