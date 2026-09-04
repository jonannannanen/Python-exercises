# Write a program that uses a while loop to print out all numbers
# divisible by three in the range of 1-1000.

first = 1
while first <= 1000:
    if first % 3 == 0:
        print(first)
    first = first + 1