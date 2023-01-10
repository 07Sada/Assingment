# 4.	Write a Python Program to Check Armstrong Number?

num = int(input("Enter a number: "))

# Compute the sum of the cubes of the digits
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# Check if the number is an Armstrong number
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
