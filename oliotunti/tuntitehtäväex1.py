# Kirjoita Pelaaja-luokka, jonka ominaisuuksia ovat nimi, elämät, kolikot ja pisteet
# Kirjoita luokkaan alustaja joka saa parametrina hahmon nimen. Uuden hahmon:
# elämät asetetaan automaattisesti arvoon 3 
# kolikot asetetaan arvoon 0
# pisteet asetetaan arvoon 0

class Pelaaja:
    def __init__(self, nimi, elämät=3, kolikot=0, pisteet=0):
        self.nimi = nimi
        self.elämät = elämät
        self.kolikot = kolikot
        self.pisteet = pisteet

# Pääohjelma main

pelaaja1 = Pelaaja("Mario")

print(f"{pelaaja1.nimi}\n{pelaaja1.elämät}")
print(f"{pelaaja1.kolikot}\n{pelaaja1.pisteet}")