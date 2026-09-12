# Write a program that converts inches to centimeters
# until the user inputs a negative value. Then the program ends.

inches = float(input("Enter inches: "))

while inches >= 0:
    cm = inches * 2.54
    print(cm)

    inches = float(input("Enter inches: "))