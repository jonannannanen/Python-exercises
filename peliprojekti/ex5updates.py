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

		command = input("Enter command: ")

		if command == "Investigate upstairs":
			print("You find a dark corridor that leads to one creaking door.")

		elif command == "Investigate main floor":
			print("You stumble upon an old kitchen.")

		elif command == "Investigate basement":
			print("You fall into an ancient chapel.")

		elif command == "Leave the house":
			print("You find that the door has been sealed shut. You're trapped.")

		elif command == "quit":
			print("You failed.")

		else:
			print("Unknown command.")
