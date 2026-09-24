# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa julkaisut Aku Ankka
# (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien julkaisujen kaikki tiedot
# toteuttamiesi metodien avulla.
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"{self.nimi}, {self.kirjoittaja}, {self.sivumäärä}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"{self.nimi}, {self.päätoimittaja}")

# Pääohjelma

kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

lehti = Lehti("Aku Ankka", "Aki Hyyppä")

kirja.tulosta_tiedot()
lehti.tulosta_tiedot()