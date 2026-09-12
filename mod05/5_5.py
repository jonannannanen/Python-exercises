# Write a program that asks the user for a username and password
# If either or both are incorrect, the program ask the user
# to enter the username and password again. This continues until
# the login information is correct or wrong credentials have been
# entered five times. If the information is correct, the program
# prints out Welcome. After five failed attempts the program prints out
# Access denied. The correct username is python and password rules.

attempts = 0

while attempts < 5:
    user_input = input("Enter username: ")
    user_input_p = input("Enter password: ")

    if user_input == "python" and user_input_p == "rules":
        print("Welcome")
        break

    elif user_input != "python" and user_input_p == "rules":
        print("Wrong username.")
        attempts = attempts + 1

    elif user_input == "python" and user_input_p != "rules":
        print("Wrong password.")
        attempts = attempts + 1

    else:
        attempts = attempts + 1

if attempts == 5:
    print("Access denied")