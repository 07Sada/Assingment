# Question 1:
"""
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70

"""

def divisible_by_5_and_7(n):
    for i in range(n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

n = int(input("Enter a number: "))

result = [x for x in divisible_by_5_and_7(n)]

print(','.join(map(str, result)))
