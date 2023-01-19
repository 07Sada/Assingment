# Question 4:
"""
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again

Then, the output should be:

again and hello makes perfect practice world
"""

words = input("Enter a sequence of words separated by whitespace: ")

# splitting input string into list of words
word_list = words.split()

# remove duplicate words
word_list = list(set(word_list))

# sort the list of words
word_list.sort()

# join the words in the list with ' '
sorted_words = " ".join(word_list)

# print the sorted, alphanumerically words
print(sorted_words)
