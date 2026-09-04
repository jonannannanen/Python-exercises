# Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.
# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.

gender = input("State your gender: ")

if gender == "Male":
    hemoglobin = int(input("Insert your hemoglobin: "))
    print(hemoglobin, "g/l")
    if 134 <= hemoglobin <= 167:
        print("Your hemoglobin is normal.")
    elif hemoglobin > 167:
        print("Your hemoglobin is too high.")
    elif hemoglobin < 134:
        print("Your hemoglobin is too low.")

if gender == "Female":
    hemoglobin = int(input("Insert your hemoglobin: "))
    print(hemoglobin, "g/l")
    if 117 <= hemoglobin <= 155:
        print("Your hemoglobin is normal.")
    elif hemoglobin > 155:
        print("Your hemoglobin is too high.")
    elif hemoglobin < 117:
        print("Your hemoglobin is too low.")