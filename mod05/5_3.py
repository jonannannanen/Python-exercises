# Write a program that asks the user to enter numbers until they
# enter an empty string to quit. Finally, the program prints out
# the smallest and largest number from the numbers it received.

number = (input("Enter number: "))

if number != "":
    number = float(number)

    smallest = number
    largest = number

    number = input("Enter a number: ")

    while number != "":
        number = float(number)

        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

        number = input("Enter a number: ")

    print("Smallest number:", smallest)
    print("Largest number:", largest)
