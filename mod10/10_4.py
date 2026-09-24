# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
# pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja
# autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:
# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo kunkin
# auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
# kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa
# tapauksessa palautetaan False.
# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä “Suuri romuralli”. Luotavalle kilpailulle annetaan kymmenen auton lista
# samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka
# jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla
# kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.
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

class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus_kilometreinä, osallistuvat_autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_kilometreinä = pituus_kilometreinä
        self.osallistuvat_autot = osallistuvat_autot

    def tunti_kuluu(self):
        for auto in self.osallistuvat_autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteritunnus':<15} {'Huippunopeus':<15} {'Nopeus':<10} {'Matka':<10}")

        for auto in self.osallistuvat_autot:
            print(f"{auto.rekisteritunnus:<15} {auto.huippunopeus:<15} {auto.tämänhetkinen_nopeus:<10} {auto.kuljettu_matka:<10}")

    def kilpailu_ohi(self):
        for auto in self.osallistuvat_autot:
            if auto.kuljettu_matka >= self.pituus_kilometreinä:
                return True
        
        return False
    
import random

autot = []

for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit = tunnit + 1

    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()
