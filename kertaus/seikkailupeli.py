class Party():
    def __init__(self):
        self.members = []

    def add_member(self, adventurer):
        self.members.append(adventurer)
        print(f"{adventurer.name} joins the party.")

    def retire_member(self, adventurer):
        if adventurer in self.members:
            self.members.remove(adventurer)
            print(f"{adventurer.name} retires.")
        else:
            print(f"{adventurer.name} not in the party.")

    def show_members(self):
        for member in self.members:
            print(f"{member.name}")

    def show_health(self):
        for member in self.members:
            print(f"{member.name} HP: {member.hp}")

class Adventurer():
    def __init__(self, name, HP=100, stamina=100, attack_damage=10):
        self.name = name
        self.hp = HP
        self.stamina = stamina
        self.attack_damage = attack_damage

    def gainLife(self, healingAmount):
        self.hp += healingAmount
        print(f"{self.name} gains {healingAmount}. HP: {self.hp}.")

    def loseLife(self, lifeloss):
        self.hp -= lifeloss

        if self.hp <= 0:
            print(f"{self.name} died.")
        else:
            print(f"{self.name} loses {lifeloss}. HP: {self.hp}")

class Mage(Adventurer):
    def __init__(self, name):
        super().__init__(name, HP=50, attack_damage=20)

    def partyheal(self, party):
        print("Mage casts partyheal.")
        for member in party.members:
            member.gainLife(50)

class Paladin(Adventurer):
    def __init__(self, name):
        super().__init__(name, HP=150, attack_damage=5)

class Rogue(Adventurer):
    def __init__(self, name):
        super().__init__(name)

playerList = []

player1 = Mage("Gunther")
player2 = Paladin("Mr. Bean")
player3 = Rogue("Morty")

playerList.append(player1)
playerList.append(player2)
playerList.append(player3)

# for i in range(3):
#     player = Adventurer(input("Adventurer name: "))
#     playerList.append(player)

for player in playerList:
    print(player.name)
print("\nParty:\n")
party = Party()

party.add_member(player1)
party.add_member(player2)
party.add_member(player3)

# player1.loseLife(50)
# player2.gainLife(20)
# print(f"Meteor falls on {player3.name}'s head.")
# player3.loseLife(150)
print(f"Mr. Bean gets hit on the head by a goblin.")
player2.loseLife(100)
print(f"Gunther ate a poison mushroom.")
player1.loseLife(20)
print(f"Morty fell down a tree.")
player3.loseLife(20)

party.show_health()

player1.partyheal(party)

print(f"Gunther is exhausted.")
party.retire_member(player1)

party.show_members()