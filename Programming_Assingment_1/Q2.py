# 2.Write a Python program to do arithmetical operations addition and division.?

# taking input from user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# creating function to add the numbers
def addition(a, b):
    return a+b 

# creating division function 
def division(a, b):
    return a/b 

print(f"The result of addition is:{addition(a, b)}")
print(f"The result of division is:{division(a, b)}")