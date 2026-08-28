# Write a program that draws two random
# combinations of numbers for a combination lock:
# a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.
import random

lock1 = f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
lock2 = f"{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}"

print(f"Lock 1 combination: {lock1}")
print(f"Lock 2 combination: {lock2}")
