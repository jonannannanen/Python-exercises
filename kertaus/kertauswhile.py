# while loop

# user input niin kauan kunnes user antaa quit stringin

print("Komennot:\nJatka\nOhje\nLopeta\nSeis")
user_command = input("Anna komento")

while user_command != "Lopeta":
    if user_command == "Jatka":
        print("Jatketaan seuraavaan")

    elif user_command == "Ohje":
        print("Katso ohje")

    elif user_command == "Seis":
        print("Abort")
        break

    user_command = input("Anna uusi komento")

else:
    print("Looppi ei toteutunut")

print("End")