class Hero:
    sankarien_määrä = 0


    def __init__(self, nimi, tyyppi, voima, ase, huudahdus="Moikkulii"):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.voima = voima
        self.ase = ase
        self.huudahdus = huudahdus
        Hero.sankarien_määrä = Hero.sankarien_määrä + 1

    def huuda(self, kerrat=1):
        for i in range(kerrat):
            print(f"{self.huudahdus}")

    def näytä_ase(self):
        print(self.ase)


hero1 = Hero("Reinhardt", "tank", "stronk", "Bonk", "Aaaarww")
hero2 = Hero("Tracer", "damage", "piupiu", "fast")

print(f"{hero1.nimi} on {hero1.tyyppi} ja hän on {hero1.voima}, hän sanoo {hero1.huudahdus}")
print(f"{hero2.nimi} on {hero2.tyyppi} ja hän on {hero2.voima}, hän sanoo {hero2.huudahdus}")

hero1.huuda()
hero1.näytä_ase()

hero2.huuda(2)
hero2.näytä_ase()

print(f"Sankarien määrä joukkueessa: {Hero.sankarien_määrä}")
