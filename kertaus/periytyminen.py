# # periytyminen esimerkki
# 1. luo varusmiesluokka jolla on nimi, sukunimi
# luo metodiksi ilmoita tedot; joka printtaa nimen ja sukunimen

class Varusmies():
    def __init__(self, nimi, sukunimi):
        self.nimi = nimi
        self.sukunimi = sukunimi

    def ilmoita_tiedot(self):
	    print(f"{self.nimi} {self.sukunimi}")

class Miehistö(Varusmies):
    def __init__(self, nimi, sukunimi, arvo):
        super().__init__(nimi, sukunimi)
        self.arvo = arvo

    def ilmoita_tiedot(self):
        super().ilmoita_tiedot()
        print(f"{self.arvo}")

class Henkilökunta(Miehistö):
    def __init__(self, nimi, sukunimi, arvo, tehtävä):
        super().__init__(nimi, sukunimi, arvo)
        self.tehtävä = tehtävä

    def ilmoita_tiedot(self):
        super().ilmoita_tiedot()
        print(f"{self.tehtävä}")

# varusmies1 = Varusmies(input("Anna etunimesi: "), input("Anna sukunimesi: "))

# varusmies1.ilmoita_tiedot()

miehistö1 = Miehistö(input("Anna etunimesi: "), input("Anna sukunimesi: "), input("Anna sotilasarvo: "))
miehistö1.ilmoita_tiedot()

henk1 = Henkilökunta("Sofia", "Sotilas", "Ylijumala", "Logistiikka")
henk1.ilmoita_tiedot()