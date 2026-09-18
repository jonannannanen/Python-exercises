class PirateShip:
    def __init__(self, name, cannon_count, crew_count, gold_count=0):
        self.name = name
        self.cannon_count = cannon_count
        self.crew_count = crew_count
        self.gold_count = gold_count

    def find_treasure(self, määrä):
        self.gold_count += määrä

    def lose_treasure(self, määrä):
        self.gold_count -= määrä

        if self.gold_count < 0:
            self.gold_count = 0

laiva = PirateShip("The Black Pearl", cannon_count=12, crew_count=40)

laiva.find_treasure(200)
laiva.find_treasure(75)
laiva.lose_treasure(100)

print(f"Name: {laiva.name}\nCannons: {laiva.cannon_count}\nCrew: {laiva.crew_count}\nGold: {laiva.gold_count}")

