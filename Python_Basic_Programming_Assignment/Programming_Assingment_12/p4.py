# 4.	Write a Python program to convert key-values list to flat dictionary?
key_value_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
flat_dict = {key: value for key, value in key_value_list}
print(flat_dict)
