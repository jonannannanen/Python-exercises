# Write a program that asks a fisher the length of 
# a zander in centimeters. If the zander does not 
# fulfill the size limit, the program instructs 
# to release the fish back into the lake and notifies 
# the user of how many centimeters below the size limit 
# the caught fish was. A zander must be 42 centimeters 
# or longer to meet the size limit.

length = int(input("The length of a zander in cm: "))

erotus = 42 - length

if length >= 42:
    print("Your catch meets the requirements.")
else:
    print("Requirements not met.")
    print(f"Missing amount: {erotus:.2f}")