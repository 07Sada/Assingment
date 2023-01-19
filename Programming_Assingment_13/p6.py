# Question 6:
""" 
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

1. At least 1 letter between [a-z]

2. At least 1 number between [0-9]

1. At least 1 letter between [A-Z]

3. At least 1 character from [$#@]

4. Minimum length of transaction password: 6

5. Maximum length of transaction password: 12

Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345

Then, the output of the program should be:

ABd1234@1

"""
import re

# input passwords
passwords = input("Enter a list of passwords separated by commas: ")

# split the input string into a list of passwords
password_list = passwords.split(",")

# initialize a list to store valid passwords
valid_passwords = []

# check each password for validity
for password in password_list:
    if len(password) >= 6 and len(password) <= 12:
        if re.search("[a-z]", password) and re.search("[0-9]", password) and re.search("[A-Z]", password) and re.search("[$#@]", password):
            valid_passwords.append(password)

# join the valid passwords with a comma
valid_passwords = ",".join(valid_passwords)

# print the valid passwords
print(valid_passwords)
