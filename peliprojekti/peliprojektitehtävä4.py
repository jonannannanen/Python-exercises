class Player():
	def __init__(self, playername, inventory, location, hp=10, strength=5):
		self.playername = playername
		self.hp = hp
		self.strength = strength
		self.inventory = inventory
		self.location =location

	def move(self, room):
		self.location = room

	def collect_item(self, item):
		self.inventory.append(item)

	def lose_hp(self, damage):
		self.hp = self.hp - damage
		if self.hp < 0:
			self.hp = 0
		print("You lost", damage, "HP")
		print("HP:", self.hp)

class Room():
	def __init__(self, name, items=None):
		self.name = name
		self.items = items

class Item():
	def __init__(self, name, effect):
		self.name = name
		self.effect = effect

def investigate_upstairs(player):
	choice = input("You find a dark corridor that leads to one creaking door. Will you go inside? Y or N")

	if choice == "Y":
		if talisman in player.inventory:
			player.lose_hp(4)

		else:
			player.lose_hp(8)
	
	if choice == "N":
		if rabbit_foot in player.inventory:
			print("The creature in the room hears you as you turn back.\nYou reach the staircase and notice that it won't move past it and retreats.")
		else:
			player.lose_hp(6)
			print("The creature still hears you and attcks you as you turn your back.")

def investigate_main_floor(player):
	print("You stumble upon an old kitchen.")

	if rabbit_foot in kitchen.items and dark_vial in kitchen.items:
		print("You find an old rabbit's foot and a vial of dark liquid.")
		choice = input("Do you pick the Rabbit's foot (R) or the vial (V)?")
	
		if choice == "R":
			player.collect_item(rabbit_foot)
			kitchen.items.remove(rabbit_foot)
	
		elif choice == "V":
			player.collect_item(dark_vial)
			kitchen.items.remove(dark_vial)

	elif rabbit_foot in kitchen.items:
		choice = input("You find an old Rabbit's foot. Will you pick it up? Y or N")

		if choice == "Y":
			player.collect_item(rabbit_foot)
			kitchen.items.remove(rabbit_foot)

	elif dark_vial in kitchen.items:
		choice = input("You find a vial of dark liquid. Will you pick it up? Y or N")

		if choice == "Y":
			player.collect_item(dark_vial)
			kitchen.items.remove(dark_vial)

	else:
		print("You already looted this place.")

def investigate_basement(player):
	print("You fall into an ancient chapel.")

	if talisman in basement.items:
		choice = input("You find an ancient talisman. Will you pick it up? Y or N")
	
		if choice == "Y":
			player.collect_item(talisman)
			basement.items.remove(talisman)

	else:
		print("You already looted this item.")

def leave_the_house():
	print("You find that the door has been sealed shut. You're trapped.")

def inventory(player):
	for item in player.inventory:
		print(item.name)

rabbit_foot = Item("Rabbit's foot", "luck")
dark_vial = Item("Dark vial", "doom")
talisman = Item("Ancient talisman", "protection")

main_floor = Room("Main floor", [])
kitchen = Room("Kitchen", [rabbit_foot, dark_vial])
upstairs = Room("Upstairs", [])
basement = Room("Basement", [talisman])

name = input("Enter your name: ")

age = int(input("Enter your age: "))

if age < 12:
	print("You are a minor. Game over.")

else:
	player = Player(name, [], main_floor)

	print("Welcome " +name+ "!")

	command = ""

	while command != "quit" or player.hp > 0:
		print()
		print("Current location: ", player.location.name)
		print("Menu")
		print("Investigate upstairs")
		print("Investigate main floor")
		print("Investigate basement")
		print("Leave the house")
		print("Inventory")
	
		command = input("Enter command: ")
	
		if command == "Investigate upstairs":
			player.move(upstairs)
			investigate_upstairs(player)

		elif command == "Investigate main floor":
			player.move(kitchen)
			investigate_main_floor(player)

		elif command == "Investigate basement":
			player.move(basement)
			investigate_basement(player)

		elif command == "Leave the house":
			leave_the_house()

		elif command == "Inventory":
			inventory(player)

		elif command == "quit":
			print("You failed.")

		else:
			print("Unknown command.")

	if player.hp == 0:
		print("You died")