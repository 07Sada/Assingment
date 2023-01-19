# 1.	Write a Python program to find words which are greater than given length k?
def find_words_greater_than_k(k, string):
  words = string.split()
  result = []
  for word in words:
    if len(word) > k:
      result.append(word)
  return result

k = 5
string = "This is a sample sentence to find words greater than a given length"
print(find_words_greater_than_k(k, string))
