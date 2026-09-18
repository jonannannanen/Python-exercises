# Write a function that gets the quantity of gasoline in American
# gallons and returns the number converted to litres. Write a main
# program that asks for a volume in gallons from the user and converts
# the value to liters. The conversion must be done by using the function.
# Conversions continue until the user inputs a negative value.
# 1 gallon = 3,785 liters

gallons = int(input("Gallons: "))

def liters(gallons):
    result = gallons * 3.785
    return result

result = liters(gallons)

print(result)

while result <= 0: