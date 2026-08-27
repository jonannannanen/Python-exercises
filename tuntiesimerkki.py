import math

radius_of_circle = input("Gice the radius of the circle: ")
side_of_square = input("Give the side of the square: ")

area_of_square = float(side_of_square)**2
radius_of_circle = math.pi*(float(radius_of_circle*2))

print(f"Area of circle: {radius_of_circle: .2f}")
print(f"Area of square: {area_of_square: .2f}")