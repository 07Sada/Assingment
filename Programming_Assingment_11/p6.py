# 6.	Write a Python to find all duplicate characters in string?
def find_duplicate_characters(string):
    duplicate_chars = []
    for char in string:
        if string.count(char) > 1:
            if char not in duplicate_chars:
                duplicate_chars.append(char)
    return duplicate_chars

string = "hello world"
print(find_duplicate_characters(string))
