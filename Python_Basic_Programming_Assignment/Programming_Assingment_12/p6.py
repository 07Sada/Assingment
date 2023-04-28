# 6.	Write a Python program to check order of character in string using OrderedDict()?
from collections import OrderedDict

def check_order(string):
    return list(OrderedDict.fromkeys(string).keys()) == list(string) #returns True if they are identical and False otherwise.

string = "abcdefg"
print(check_order(string))

