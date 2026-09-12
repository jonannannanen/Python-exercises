# Write a game where the computer draws a random integer between 1 and 10
# The user tries to guess the number until they guess the right number
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.

import random

integer = random.randint(1, 10)

guess = int(input("Guess: "))
while guess != integer:
    if guess < integer:
        print("Too low.")
    else:
        print("Too high.")
    guess = int(input("Guess again: "))
print("Correct.")