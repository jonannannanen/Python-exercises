import random

heittojen_summa = 0

def heitä_noppaa(kerrat, tahkot=6):
    summa = 0
    for kerta in range(kerrat):
        summa += random.randint(1,tahkot)
    return summa

heittojen_summa = heitä_noppaa(4,21)

print(f"Heittojen summa: {heittojen_summa}")