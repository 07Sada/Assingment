# 5.	Write a Python program to insertion at the beginning in OrderedDict?
from collections import OrderedDict

my_dict = OrderedDict()
my_dict[1] = 'a'
my_dict[2] = 'b'
my_dict[3] = 'c'

my_dict.move_to_end(1, last=False)
print(my_dict)
