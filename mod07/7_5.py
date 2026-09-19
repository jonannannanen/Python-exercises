# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma
# palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu
# lista paitsi että siitä on karsittu pois kaikki parittomat luvut. Kirjoita
# testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat
# sen jälkeen sekä alkuperäisen että karsitun listan.

numbers = [8, 6, 4, 81, 84]

def remove_odd(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers

result = remove_odd(numbers)

print("Kaikki luvut: ", numbers)
print("Parilliset luvut: ", result)