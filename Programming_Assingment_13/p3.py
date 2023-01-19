# Question 3:
""" Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world

Then, the output should be:

bag,hello,without,world
"""
 
words = input("Enter a list of words separated by commas: ")

# splitting input string into list of words
word_list = words.split(",")

# sort the list of words
word_list.sort()

# join the words in the list with commas
sorted_words = ",".join(word_list)

# print the sorted, comma-separated words
print(sorted_words)