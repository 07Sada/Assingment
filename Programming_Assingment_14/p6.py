# Question 6:
"""Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list."""

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
        # x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1


# test the function
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
if result != -1:
    print(f'{x} is present at index {str(result)}.')
else:
    print(f'{x} is not present in array.')