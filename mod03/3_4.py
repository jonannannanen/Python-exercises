import math

number1 = input("Give an integer number: ")
number2 = input("Give second integer number: ")
number3 = input("Give third integer number: ")

sum = float(number1) + float(number2) + float(number3)
product = float(number1) * float(number2) * float(number3)
average = float(sum)/3

print(f"Sum of numbers: {sum:.2f}")
print(f"Product of numbers: {product:.2f}")
print(f"Average of numbers: {average:.2f}")