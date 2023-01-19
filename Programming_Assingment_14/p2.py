# Question 2:
""" 
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

Then, the output should be:

2:2

3.:1

3?:1

New:1

Python:5

Read:1

and:1

between:1

choosing:1

or:2

to:1

"""

import collections
import re

# input text
text = input("Enter a text: ")

# split the text into words
words = re.findall(r'\b\w+\b', text)

# create a dictionary to store the frequency of each word
word_freq = collections.defaultdict(int)

# compute the frequency of each word
for word in words:
    word_freq[word] += 1

# sort the dictionary by key
sorted_word_freq = dict(sorted(word_freq.items()))

# print the frequency of each word
for word, freq in sorted_word_freq.items():
    print(word + ":" + str(freq))
