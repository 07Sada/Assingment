# 7.	Write a Python Program to check if a string contains any special character?
import re

def has_special_char(string):
    return bool(re.search(r'[^a-zA-Z0-9\s]', string))

string = "Hello World! How are you today?"
result = has_special_char(string)
if result:
    print("The given string contains special characters.")
else:
    print("The given string does not contain special characters.")
