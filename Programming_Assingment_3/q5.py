# 5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
for num in range(1, 10001):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
