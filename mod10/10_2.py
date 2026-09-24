# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja
# ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin
# numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
class Hissi:
    hissien_määrä = 0
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_alas(self):
        self.nykyinen_kerros = self.nykyinen_kerros - 1
        print(f"Kerros: {self.nykyinen_kerros}")

    def kerros_ylös(self):
        self.nykyinen_kerros = self.nykyinen_kerros + 1
        print(f"Kerros: {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohde):
        while self.nykyinen_kerros < kohde:
            self.kerros_ylös()

        while self.nykyinen_kerros > kohde:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumäärä):
        self.hissit = []

        for i in range(hissien_lukumäärä):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohdekerros)

# Pääohjelma
talo = Talo(1, 5, 3)


talo.aja_hissiä(1, 2)
