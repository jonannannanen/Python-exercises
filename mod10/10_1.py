# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän
# kerroksen numeron. Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h esimerkiksi metodikutsun
# h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
# että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen
# ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten,
# että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin
# alimpaan kerrokseen.
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
# Pääohjelma
hissi = Hissi(1, 5)

hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(1)