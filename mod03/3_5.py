# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13.3 grams.
import math

talents = input("Enter talents: ")
pounds = input("Enter pounds: ")
lots = input("Enter lots: ")

talents = float(talents)
pounds = float(pounds)
lots = float(lots)
# In grams
talents_in_grams = talents*20*32*13.3
pounds_in_grams = pounds*32*13.3
lots_in_grams = lots*13.3
# In kg
talents_in_kg = talents_in_grams/1000
pounds_in_kg = pounds_in_grams/1000
lots_in_kg = lots_in_grams/1000

print(f"Talents in grams: {talents_in_grams:.2f}")
print(f"Talents in kg: {talents_in_kg:.2f}")
print(f"Pounds in grams: {pounds_in_grams:.2f}")
print(f"Pounds in kg: {pounds_in_kg:.2f}")
print(f"Lots in grams: {lots_in_grams:.2f}")
print(f"Lots in kg: {lots_in_kg:.2f}")