# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on ominaisuutena
# akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat.
# Esim sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan
# alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton
# (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus,
# käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = 0

    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + self.nopeus * tunnit

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti, nopeus=160):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus, nopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko, nopeus=120):
        self.bensatankin_koko = bensatankin_koko
        super().__init__(rekisteritunnus, huippunopeus, nopeus)

# Pääohjelma

sähköauto = Sähköauto("ABC-15", "180 km/h", "52.5 kWh")
polttomoottoriauto = Polttomoottoriauto("ACD-123", "165 km/h", "32.3 l")

sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(sähköauto.kuljettu_matka)
print(polttomoottoriauto.kuljettu_matka)