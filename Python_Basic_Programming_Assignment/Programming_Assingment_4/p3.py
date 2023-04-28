# 3.	Write a Python Program to Print the Fibonacci sequence?
num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Initialize the first two terms
a, b = 0, 1

# Print the first two terms
print(a)
print(b)

for i in range(2, num_terms):
    # Compute the next term
    c = a + b
    
    # Print the term
    print(c)
    
    # Update the variables for the next iteration
    a, b = b, c
