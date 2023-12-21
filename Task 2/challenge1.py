import math
print("Please enter the length of 3 sides of a triangle: ")

side1 = int(input("side 1: "))
side2 = int(input("side 2: "))
side3 = int(input("side 3: "))

if (side1 +side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2):
    s = (side1 + side2 + side3)/2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s-side3))
    print("The Area of the triangle is:")
    print(area)
else:
    print("Sorry, these numbers cant be the sides of a triangle.")