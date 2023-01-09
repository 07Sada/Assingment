# 5.	Write a Python program to generate a random number ?

# importing random module
import random

# lower bound and upper bound entry
a = int(input("Enter the lower bound value: "))
b = int(input("Enter the upper bound value: "))

# Generating random integer between upper bound and lower bound
random_int = random.randint(a, b)

print(random_int)