import math

length = input("Give the length of the rectangle: ")
width = input("Give the width of the rectangle: ")

perimeter = float(length)*2 + float(width)*2
area = float(length)*float(width)

print(f"Perimeter of the rectangle : {perimeter:.2f}")
print(f"Area of the rectangle : {area:.2f}")