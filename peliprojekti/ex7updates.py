items = []

def investigate_upstairs():
	print("You find a dark corridor that leads to one creaking door.")

def investigate_main_floor():
	print("You stumble upon an old kitchen.")
	item = input("You find an old rabbit's foot and a vial of dark liquid. Which one do you pick?")
	items.append(item)

def investigate_basement():
	print("You fall into an ancient chapel.")

def leave_the_house():
	print("You find that the door has been sealed shut. You're trapped.")

def inventory():
	print(items)

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 12:
	print("You are a minor. Game over.")

else:
	print("Welcome " +name+ "!")
	# game starts

	command = ""

	while command != "quit":
		print()
		print("Menu")
		print("Investigate upstairs")
		print("Investigate main floor")
		print("Investigate basement")
		print("Leave the house")
		print("Inventory")
	
		command = input("Enter command: ")
	
		if command == "Investigate upstairs":
			investigate_upstairs()

		elif command == "Investigate main floor":
			investigate_main_floor()

		elif command == "Investigate basement":
			investigate_basement()

		elif command == "Leave the house":
			leave_the_house()

		elif command == "Show items":
			inventory()

		elif command == "quit":
			print("You failed.")

		else:
			print("Unknown command.")