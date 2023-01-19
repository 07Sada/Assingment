# 4.	Write a Python to check if a given string is binary string or not?

def is_binary_string(string):
    for char in string:
        if char != '0' and char != '1':
            return False
    return True

string = "010101"
result = is_binary_string(string)
if result:
    print("The given string is a binary string.")
else:
    print("The given string is not a binary string.")
