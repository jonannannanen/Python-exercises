# Modify the function above so that it gets the number
# of sides on the dice as a parameter. With the modified function
# you can for example roll a 21-sided role-playing dice.
# The difference to the last exercise is that the dice rolling in
# the main program continues until the program gets the maximum number
# on the dice, which is asked from the user at the beginning.

import random

sides = int(input("How many sides does the dice have?: "))

def roll_dice(sides):
	result = random.randint(1, sides)
	return result

result = roll_dice(sides)

print(result)

while result != (sides):
	result = roll_dice(sides)
	print(result)