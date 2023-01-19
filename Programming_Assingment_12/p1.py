# 1.	Write a Python program to Extract Unique values dictionary values?

def unique_values(dictionary):
    return set(dictionary.values())

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2}
print(unique_values(my_dict))
