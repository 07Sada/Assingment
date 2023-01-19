# Question 1:
"""Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n."""

class DivisibleBySeven:
    def __init__(self,n):
        self.n = n

    def iterate_divisible_by_seven(self):
        for i in range(self.n+1):
            if i % 7 == 0:
                yield i 

# create an instance of the DivisibleBySeven class with n=35
divisible_by_seven = DivisibleBySeven(35)

# use the generator 
for num in divisible_by_seven.iterate_divisible_by_seven():
    print(num)