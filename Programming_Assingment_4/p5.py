# 5.	Write a Python Program to Find Armstrong Number in an Interval?
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

for num in range(start, end + 1):
    # Compute the sum of the cubes of the digits
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    # Check if the number is an Armstrong number
    if num == sum:
        print(num)
