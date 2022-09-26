import re
from functools import wraps
import random
import sys


# Task1
# Create a class method named `validate`,
# which should be called from the `__init__`
# method to validate parameter email, passed to the constructor.
# The logic inside the `validate` method could be to check if the passed email
# parameter is a valid email string
class check_amail:
    def __init__(self, email):
        self.__email = email

    @property
    def validate(self):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, self.__email):
            return "Valid email"
        else:
            return "Invalid email"


s = check_amail('oleksandr@gmail.ua')
print(s.validate)


# task 2
# Implement 2 classes, the first one is the Boss and the second one is the Worker.

# Worker has a property 'boss', and its value must be an instance of Boss.

# You can reassign this value, but you should check whether the new
# value is Boss. Each Boss has a list of his own workers.
# You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class to workers list directly
# via access to attribute, use getters and setters instead!

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.__workers = []

    @property
    def workers(self):
        return self.__workers

    @workers.setter
    def workers(self, worker):
        if isinstance(worker, Worker):
            self.__workers.append(worker)

    def add_worker(self, worker):
        self.workers.append(worker)
        worker.boss = self

    def __str__(self):
        return f"{self.name}"


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, boss):
        if isinstance(boss, Boss):
            self.__boss = boss
            boss.workers.append(self)

    def __str__(self):
        return f"{self.name}"
boss = Boss(1,"Boss",'Company')
worker1= Worker(1,"rainold",'Company',boss)
worker2= Worker(1,"Raad",'Company',boss)
print(boss.workers[0])
print(worker1.boss)
# Task3
# Write a class TypeDecorators which
# has several methods for converting results of functions to a specified type (if it's possible):
class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if func(*args, **kwargs).isdigit():
                return int(func(*args, **kwargs))
            else:
                return "its not a int"

        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return str(func(*args, **kwargs))

        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if func(*args, **kwargs).lower() == 'false':
                return 'false'
            else:
                return bool(func(*args, **kwargs))

        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if func(*args, **kwargs).isdigit():
                return float(func(*args, **kwargs))
            else:
                return "its not a float"

        return wrapper

@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


print(do_nothing('25'))
print(do_something('True'))