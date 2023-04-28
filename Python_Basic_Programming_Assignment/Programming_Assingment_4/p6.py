# 6.	Write a Python Program to Find the Sum of Natural Numbers?
num = int(input("Enter a number: "))

# Initialize the sum to 0
sum = 0

# Add up all the natural numbers from 1 to num
for i in range(1, num + 1):
    sum += i

print("The sum of the natural numbers up to", num, "is", sum)
