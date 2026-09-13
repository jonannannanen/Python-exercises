# Write a program that asks the user to enter numbers until they
# input an empty string to quit. At the end, the program prints out
# the five greatest numbers sorted in descending order. Hint: You can
# reverse the order of sorted list items by using the sort method with
# the reverse=True argument

numbers = []

user_input = input("Enter number: ")

while user_input != "":
	number = float(user_input)
	numbers.append(number)
	user_input = input("Enter number: ")

numbers.sort(reverse=True)

print(numbers[:5])