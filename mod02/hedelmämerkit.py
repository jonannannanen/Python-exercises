# ask user for amount of fruit in kg
# calculate the price of each fruit based on price per kg
# calculate and display each fruit separately as well as the total

# fruit prices in kg

banana_price_kilograms = 2.85
apple_price_kilograms = 3.15
orange_price_kilograms = 4.05

amount_of_bananas = float(input("Give the amount of bananas: "))
amount_of_apples = float(input("Give the amount of apples: "))
amount_of_oranges = float(input("Give the amount of oranges: "))

price_of_bananas = amount_of_bananas*banana_price_kilograms
price_of_apples = amount_of_apples*apple_price_kilograms
price_of_oranges = amount_of_oranges*orange_price_kilograms

total_price = price_of_bananas + price_of_apples + price_of_oranges

print(f"Banana total: {price_of_bananas:.2f}")
print(f"Apple total: {price_of_apples:.2f}")
print(f"Orange total: {price_of_oranges:.2f}")
