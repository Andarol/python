import numpy as np


# Task1 із уроку 11 (Робота з файлами та менеджери контексту, JSON).
def write_file():
    file = open("myfile.txt", "w")
    file.write("hello file world!")


def open_file(name):
    file = open(name, "r")
    return file.read()


write_file()
print(open_file("myfile.txt"))


# Додаткове завдання:
# Task1
# Створити функцію, яка перетворює рядок в
# число без використання стандартних функцій.
# Спробуйте зробити без гугління.
def digit(string):
    line = []
    for digit in string.split():
        if digit.isdigit():
            line.append(float(digit))

    return line


print(digit("123 sdrsr 1241234 sfdasfda"))


# Task2
# Створити функцію, яка приймає на вхід список
# та число n. Вхідний список потрібно розбити на n
# максимально рівномірних підсписків. Додатково можна зробити
# аргумент, який дозволить перевернути кожен із підсписків.
def lists_split(list1, n, list_type):
    list_with = []
    if list_type.lower() == "reverse":
        list1.reverse()
        list_split = np.array_split(list1, n)
        for arr in list_split:
            list_with.append(list(arr))
        return list_with

    else:
        list_split = np.array_split(list1, n)
        for arr in list_split:
            list_with.append(list(arr))
        return list_with


lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

print(lists_split(lists, 13, "reverse"))
