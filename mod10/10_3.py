# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee
# kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
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

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alin_kerros)


# Pääohjelma
talo = Talo(1, 5, 3)

talo.aja_hissiä(1, 2)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 3)

talo.palohälytys()