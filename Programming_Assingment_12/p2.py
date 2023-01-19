# 2.	Write a Python program to find the sum of all items in a dictionary?
def sum_items(dictionary):
    return sum(dictionary.values())

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(sum_items(my_dict))
