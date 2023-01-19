# 2.	Write a Python program for removing i-th character from a string?
def remove_ith_char(i, string):
    return string[:i] + string[i+1:]

string = "Hello World!"
i = 6

print("Original String: ",string)
print("String after removing the i-th character: ",remove_ith_char(i, string))
