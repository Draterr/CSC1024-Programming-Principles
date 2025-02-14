import math
radius = float(input("Enter the radius of a sphere: "))

diameter = radius * 2
circumference = 2 * math.pi * radius
surface_area = 4*math.pi*radius**2
volume = (4/3)*math.pi*radius**3

print(f"The diameter is {diameter}, The circumference is {circumference}, The surface_area is {surface_area}, The volume is {volume}")
