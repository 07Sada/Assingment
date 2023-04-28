# Question 3:
""" 
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

Example:
If the following n is given as input to the program:
8
Then, the output of the program should be:
0,1,1,2,3,5,8,13

"""
def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = int(input("Enter a number greater than 2: "))
result = [x for x in fibonacci_sequence(n)]
print(','.join(map(str,result)))



