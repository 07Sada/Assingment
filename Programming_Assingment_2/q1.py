# 1.	Write a Python program to convert kilometers to miles?


# Taking the input from user
km = float(input("Enter the distance in Km: "))

# converting Km to mi
# formula to convert kilometers to miles
# miles  = kilometer * 0.621371
mi = km * 0.621371

print(f"{km} Km is {round(mi,2)} miles")
