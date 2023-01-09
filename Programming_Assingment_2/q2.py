# 2.	Write a Python program to convert Celsius to Fahrenheit?

# Taking the input from user
cel = float(input("Enter the temperature in celsius: "))

# converting Celsius to Fahrenheit
fah = (cel * 1.8) + 32

print(f"{cel} celsius is {round(fah,2)} Fahrenheit")