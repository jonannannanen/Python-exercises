# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. Tee pääohjelman alussa lista,
# joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti “ABC-1”, “ABC-2” jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        if self.tämänhetkinen_nopeus + muutos > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus + muutos < 0:
            self.tämänhetkinen_nopeus = 0
        else:
            self.tämänhetkinen_nopeus = self.tämänhetkinen_nopeus + muutos

    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + self.tämänhetkinen_nopeus * tunnit

import random

autot = []

for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

kilpailu_loppu = False

while True:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)

    for auto in autot:
        if auto.kuljettu_matka >= 10000:
            kilpailu_loppu = True

    if kilpailu_loppu:
        break

print("Rekisteri, huippunopeus, nopeus, matka")

for auto in autot:
    print(f"{auto.rekisteritunnus}, {auto.huippunopeus}, {auto.tämänhetkinen_nopeus}, {auto.kuljettu_matka}")