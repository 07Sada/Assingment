# 5.	Write a Python program to find uncommon words from two Strings?

def find_uncommon_words(string1, string2):
    words1 = set(string1.split())
    words2 = set(string2.split())
    uncommon_words = words1.symmetric_difference(words2)
    return uncommon_words

string1 = "Hello World! How are you today?"
string2 = "Hello World! How have you been?"

print(find_uncommon_words(string1, string2))
