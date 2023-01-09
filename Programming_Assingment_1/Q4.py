# 4.Write a Python program to swap two variables?

# Taking input from user
a = input("Enter the value for first variable: ")
b = input("Enter the value for second variable: ")

print(f"""Befor swap  
        value of a: {a}
        value of b: {b}\n""")

# swapping the two variables
a, b = b, a

print("*"*50)

print(f"""After swap 
        value of a: {a}
        value of b: {b}""")
