# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta
# varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen
# palauttaman summan.

numbers = [8, 6, 4, 20]

def calculate_sum(numbers):
    result = sum(numbers)
    return result

result = calculate_sum(numbers)

print(result)