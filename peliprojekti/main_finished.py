import json

class Player():
	def __init__(self, playername, inventory, location, hp=12, strength=5):
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
	def __init__(self, name, items=None): # kaikissa huoneissa ei välttämättä itemeitä
		self.name = name
		self.items = items
		self.visited = False

class Item():
	def __init__(self, name, effect):
		self.name = name
		self.effect = effect

# TIEDOSTONKÄSITTELYT

def show_intro():
	with open("peliprojekti/intro.txt", "r") as file:
		print(file.read())

def show_instructions():
	with open("peliprojekti/ohjeet.txt", "r") as file:
		print(file.read())

def save_game(player):
	data = {
		"name": player.player.name,
		"hp": player.hp,
		"strength": player.strength,
		"inventory": [item.name for item in player.inventory],
		"location": player.location.name,
		"rooms": {}
	}

	for room in rooms.values():
		data["rooms"][room.name] = {
			"visited": room.visited,
			"items": [item.name for item in room.items]
		}

	with open("savegame.txt", "w") as file:
		json.dump(data, file)

	print("Game saved.")

def load_game():
	with open("savegame.txt", "r") as file:
		data = json.load(file)

for room_name, room_data in data["rooms"].items():
	room = rooms[room_name]
	room.visited = room_data["visited"]
	room.items = [
		items[item_name]
		for item_name in room_data["items"]
	]

	player = Player(
		data["name"],
		[items[name] for name in data["inventory"]],
		rooms[data["locatio"]],
		data["hp"],
		data["strength"]
	)

# TIEDOSTONKÄSITTELYT

def investigate_upstairs(player):
	choice = input("You find a dark corridor that leads to one creaking door. Will you go inside? Y or N")

	if choice == "Y":
		print("The creature in the room attacks you.")

		if lance in player.inventory:
			print("You use the lance to yeet past the creature and leap out of the window.")
			player.lose_hp(6)

			if player.hp > 0:
				print("You survive the fall and managed to get home.")
				return True

			else:
				print("You escaped the creature but not the fall.")
				return True

		if talisman in player.inventory:
			print("The talisman protects you and shields you from more damage. It breaks upon use.")
			player.lose_hp(4)
			player.inventory.remove(talisman)

		else:
			print("You have nothing to protect yourself with.")
			player.lose_hp(8)

		if player.hp > 0 and dark_vial in player.inventory:
			drink_choice = input("Would you like to drink the vial? Y or N")
	
			if drink_choice == "Y":
				print("The vial is filled with poison.") # jekkujekku, ei kannata juoda tuntemattomia nesteitä
				player.lose_hp(12)
	
	elif choice == "N":
		if rabbit_foot in player.inventory:
			print("The creature in the room hears you as you turn back.\nYou reach the staircase and notice that it won't move past it and retreats.")
			print("Your lucky charm turns into dust.")
			player.inventory.remove(rabbit_foot)

		else:
			print("The creature still hears you and attcks you as you turn your back.")
			player.lose_hp(6)

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

def investigate_armory(player):
	if armory.visited == False:
		print("You enter an old armory.")
		armory.visited = True

	else:
		print("You return to the armory. It's still dusty in there.")

	if lance in armory.items:
		choice = input("You see an old lance covered in dust. Will you pick it up? Y or N")

		if choice == "Y":
			player.collect_item(lance)
			armory.items.remove(lance)

		else:
			print("Why would you leave it there?")

# kellari pitää lootata kahteen kertaan että pelin saa pelattua läpi

def investigate_basement(player):
	if basement.visited == False:
		print("You fall into an ancient chapel and crack your back.")
		player.lose_hp(2)
		basement.visited = True

		if player.hp == 0:
			return

	else:
		print("You return to the chapel.")

	if talisman in basement.items:
		choice = input("You find an ancient talisman. Will you pick it up? Y or N")
	
		if choice == "Y":
			player.collect_item(talisman)
			basement.items.remove(talisman)

	else:
		print("You find a hidden staircase where the talisman was.")
		
		if key in basement.items:
			print("Below you find an old brass key.")
			player.collect_item(key)
			basement.items.remove(key)

def leave_the_house(player):

	if key in player.inventory and rabbit_foot in player.inventory:
		print("You unlock the door and escape.")
		print("You survived. Kind of.")
		print("Later you die of infection caught from the rabbit's foot.")
		return True

	elif key in player.inventory and talisman in player.inventory:
		print("You unlock the door and escape.")
		print("As you walk away, you feel the talisman burn in your pocket.")
		print("You survived but something unpleasant followed you home.")
		return True
	
	elif key in player.inventory:
		print("You unlock the door and escape.")
		print("Congratulations. You survived.")
		return True

	# peli on läpäisty kun avain on inventoryssa ja tutkitaan sen jälkeen ulko-ovi

	else:
		print("You find that the door has been sealed shut. You're trapped.")
		return False

def inventory(player):
	for item in player.inventory:
		print(item.name)

rabbit_foot = Item("Rabbit's foot", "luck") # antaa onnea mörön kanssa, mutta jos talosta poistuu sen kanssa, kuolee jalasta saatuun tautiin
dark_vial = Item("Dark vial", "doom") # kun hp:ta menettää, peli kysyy haluaako pelaaja käyttää itemin jos se on kerätty. pullossa on myrkkyä
talisman = Item("Ancient talisman", "protection") # suojelee möröltä, mutta jos talosta poistuu sen kanssa, jokin seuraa sinua kotiin
lance = Item("Lance", "lucky way out?") # vaihtoehtoinen tapa paeta talosta, pelaaja menettää 6 hpta, ja pakenee jos selviää pudotuksesta
key = Item("Key", "a way out")

items = {
	"Rabbit's foot": rabbit_foot,
	"Dark vial": dark_vial,
	"Ancient talisman": talisman,
	"Lance": lance,
	"Key": key
}

# huoneissa itemit listana, koska joissain on monta itemiä, joissain ei mitään

main_floor = Room("Main floor", [])
armory = Room("Armory", [lance])
kitchen = Room("Kitchen", [rabbit_foot, dark_vial])
upstairs = Room("Upstairs", [])
basement = Room("Basement", [talisman, key])

rooms = {
	"Main floor": main_floor,
	"Armory": armory,
	"Kitchen": kitchen,
	"Upstairs": upstairs,
	"Basement": basement
}

# PÄÄOHJELMA

show_intro()
show_instructions()

print("New game, press 1")
print("Continue game, press 2")

choice = input("Choose: ")

player = None

if choice == "1":
	name = input("Enter your name: ")
	age = int(input("Enter your age: "))

	if age < 12:
		print("You are a minor. Game over.")

	else:
		player = Player(name, [], main_floor)

		print("Welcome " +name+ "!")

		command = ""

elif choice == "2":
	player = load_game()

if player is not None:
	command = ""

	while command != "quit" and player.hp > 0:
		print()
		print("Current location: ", player.location.name)
		print("Menu")
		print("Save")
		print("Investigate upstairs")
		print("Investigate main floor")
		print("Investigate basement")
		print("Leave the house")
		print("Inventory")
	
		command = input("Enter command: ")
	
		if command == "Investigate upstairs":
			player.move(upstairs)

			if investigate_upstairs(player):
				break

		elif command == "Investigate main floor":
			room_choice = input("Where would you like to go? Kitchen or armory? K or A")

			if room_choice == "K":
				player.move(kitchen)
				investigate_main_floor(player)

			elif room_choice == "A":
				player.move(armory)
				investigate_armory(player)

		elif command == "Investigate basement":
			player.move(basement)
			investigate_basement(player)

		elif command == "Leave the house":
			if leave_the_house(player):
				break

		elif command == "Inventory":
			inventory(player)

		elif command == "quit":
			print("Bye.")
			break

		else:
			print("Unknown command.")

	if player.hp == 0:
		print("You died.")