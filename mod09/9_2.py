# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan
# nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin
# on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa huippunopeutta
# suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton nopeutta nostetaan
# ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee sitten
# hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse
# vielä päivittää.
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, kiihdytä, tämänhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeuden_muutos = kiihdytä
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytys(self, muutos):
        self.nopeuden_muutos

auto1 = Auto("ABC-123", "142 km/h")

print(f"Auton rekisteritunnus on {auto1.rekisteritunnus} ja huippunopeus {auto1.huippunopeus}.\n")
print(f"Tämänhetkinen nopeus: {auto1.tämänhetkinen_nopeus}.\nKuljettu matka: {auto1.kuljettu_matka}.")