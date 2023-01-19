# Question 5:
"""Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!"."""

import zlib

# original string
original_string = "hello world!hello world!hello world!hello world!"

# compress the string
compressed_string = zlib.compress(original_string.encode())

# decompress the string
decompressed_string = zlib.decompress(compressed_string).decode()

# print the original, compressed and decompressed strings
print("Original string:", original_string)
print("Compressed string:", compressed_string)
print("Decompressed string:", decompressed_string)
