# 4.	Write a Python program to solve quadratic equation?
# ax^2 + bx + c = 0

import math

def solve_quadratic(a, b, c):
    # calculate the discriminant
    discriminant = b**2 - 4*a*c

    # calculate the roots of the quadratic equation
    if discriminant > 0:
        # real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        # Real root
        root = -b / (2*a)
        return (root,)
    else:
        # Complex roots
        real = -b / (2*a)
        imag = math.sqrt(-discriminant) / (2*a)
        return (real + imag*1j, real - imag*1j)


print(solve_quadratic(1, 4, 3))