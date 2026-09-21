# Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum
# of the numbers. Use a for loop.

import random

number_of_dice = int(input("How many dice would you like to roll?: "))

total = 0

for i in range(number_of_dice):

	roll = random.randint(1, 6)
	total += roll

print(f"You rolled: {total}")