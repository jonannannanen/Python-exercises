class Kilpailija:
    def __init__(self, nimi, huippunopeus, nopeus=0, kuljettu_matka=0):
        self.nimi = nimi
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, muutos):
        self.nopeus += muutos
    def anti_kiihdytä(self, muutos):
            self.nopeus -= muutos

            if self.nopeus < 0:
                self.nopeus = 0

    

        