# Write a program that asks the user to 
# enter a mass in medieval units:
# talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams
# and outputs the result to the user:
# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.

import math

talents = input("Enter talents: ")
pounds = input("Enter pounds: ")
lots = input("Enter lots: ")

lot_in_grams = float(lots)*13,3
pound_in_lots = float()