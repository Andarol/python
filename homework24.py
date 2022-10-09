# Task1
def to_power(x, exp: int):
    if exp > 0:
        return x * to_power(x, exp - 1)
    else:
        return 1


print(to_power(2, 3))


# task2
def is_palindrome(str_1: str):
    if len(str_1) < 1:
        return True
    else:
        if str_1[0] == str_1[-1]:
            return is_palindrome(str_1[1:-1])
        else:
            return False


print(is_palindrome('s'))
print(is_palindrome('sassas'))
print(is_palindrome('mom'))


# task3
def mult(x, n: int):
    if n > 0:
        return x + mult(x, n - 1)
    else:
        return 0


print(mult(6, 3))


# task4
def reverse(input_str: str) -> str:
    if len(input_str) <= 0:
        return ''
    else:
        temp = input_str[-1]
        input_str = input_str[:-1]
        return temp + reverse(input_str)


print(reverse('seder'))


# task5
def sum_of_digits(digit_string: str) -> int:
    if int(digit_string) == 0:
        return 0
    else:
        return int(digit_string) % 10 + sum_of_digits(str(int(digit_string) // 10))


print(sum_of_digits('5671'))
