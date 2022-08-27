# Task 1

# Write a Python program to detect the number of local variables declared in a function.
def func_return():
    new = 1
    a = 2
    b = 3
    c = 4


print('number of variables in functiob', func_return.__code__.co_nlocals)
#co_nlocals - returns the number of local variables used by the function to get the desired result
#__code__ - it represents the code object for the function

# Task 2

# Write a Python program to access a function inside a function (Tips: use function, which returns another function)
def func_tu(a, b):
    def func23(a1, b1):
        return int(a) * int(b) * int(a1) * int(b1)

    return func23


functy = func_tu(2, 2)
print(functy(1, 2))


# Task 3

# Write a function called `choose_func` which takes a list of nums and 2 callback functions. If all nums inside the list are positive, execute the first function on that list and return the result of it. Otherwise, return the result of the second one


def choose_func(nums: list, func1, func2):
    pass


# Assertions

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1, func2):
    if all(i > 0 for i in nums):
        return func1(nums)
    else:
        return func2(nums)


print(choose_func(nums2, square_nums, remove_negatives))
