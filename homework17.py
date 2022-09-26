# Task1
# Create a base class named Animal
# with a method called talk and then create two subclasses:
# Dog and Cat, and make their own implementation of the method
# talk be different. For instance, Dog’s can be to print ‘woof woof’,
# while Cat’s can be to print ‘meow’.

# Also, create a simple generic function,
# which takes as input instance of a Cat or Dog classes
# and performs talk method on input parameter.
class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError('must be subclass')


class Cat(Animal):
    def talk(self):
        print('meow')


class Dog(Animal):
    def talk(self):
        print("woof woof")


animals = [Cat('doge'), Dog('shrek'), Dog('sereta'), Cat('pobutui')]
for animal in animals:
    animal.talk()


# task2
# Library
# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
class Author:
    def __init__(self, name, country, birthday, books=[]):
        self.__name = name
        self.__country = country
        self.__birthday = birthday
        self.__books = books

    def add_book(self, name_of_book):
        self.__books.append(name_of_book)

    def __repr__(self):
        return self.__name, self.__country, self.__birthday, self.__books

    def __str__(self):
        return self.__name


class Book(Author):
    def __init__(self, name, year, author):
        self.__name = name
        self.__year = year
        self.__author = author

    def add_book(self):
        if self.__name in self.__author.__repr__[3]:
            pass
        else:
            self.__author.add_book()

    def __repr__(self):
        return self.__name, self.__year, self.__author

    def __str__(self):
        return self.__name


class Library:
    def __init__(self, name, books=[], authors=[]):
        self.__listik_by_author = []
        self.__listik_by_year = []
        self.__name = name
        self.__books = books
        self.__authors = authors

    def new_book(self, name):
        self.__books.append(name)

    def info_about_book(self, name_of_book):
        for i in self.__books:
            if i.__str__().lower() == name_of_book.lower():
                return i.__repr__()

    def group_by_author(self, author_name):
        for i in self.__books:
            if i.__repr__()[2].lower() == author_name.lower():
                self.__listik_by_author.append(str(i))
        return self.__listik_by_author

    def group_by_year(self, what_year):
        for i in self.__books:
            if i.__repr__()[1].lower() == what_year.lower():
                self.__listik_by_year.append(str(i))
        return self.__listik_by_year

    def __repr__(self):
        return self.__name, self.__books, self.__authors

    def __str__(self):
        return self.__name


aut1 = Author('Jo Jo', 'Britain', '12 13 1234', ['History of stands', 'Ancient people', 'Legend of immortality'])
aut2 = Author('Monkey King', 'Earth', '12 13 0001',
              ['Ancient Gods', 'The greatest king is Monkey king', 'Monkey stronger then lion'])
book_jo1 = Book('History of stands', '1267', 'Jo Jo')
book_jo2 = Book('Ancient people', '1277', 'Jo Jo')
book_jo3 = Book('Legend of immortality', '1800', 'Jo Jo')
book_mon1 = Book('Ancient Gods', '12', 'Monkey King')
book_mon2 = Book('The greatest king is Monkey king', '100', 'Monkey King')
book_mon3 = Book('Monkey stronger then lion', '88', 'Monkey King')
library_1 = Library('Greatest Library', [book_mon1, book_mon2, book_mon3, book_jo1, book_jo2],
                    ['Jo Jo', 'Monkey King'])
print(library_1.info_about_book('Ancient Gods'))
print(library_1.group_by_author('Monkey King'))
print(library_1.group_by_year('1277'))
# task3
# Fraction
# Створіть клас Fraction,
# який буде представляти всю базову арифметичну логіку для дробів
# (+, -, /, *) з належною перевіркою й обробкою помилок.
# Потрібно додати магічні методи для математичних операцій та операції
# порівняння між об'єктами класу Fraction
import math


class Fraction:
    def __init__(self, numeretor, denominator):
        self.num = numeretor
        self.den = denominator
        if self.den == 0:
            raise ZeroDivisionError

    def __add__(self, other):
        return (self.num * other.den + self.den * other.num) / (other.den * self.den)

    def __sub__(self, other):
        return (self.num * other.den - self.den * other.num) / (other.den * self.den)

    def __eq__(self, other):
        return self.num / self.den == other.num / other.den

    def __lt__(self, other):
        return self.num / self.den < other.num / other.den

    def __gt__(self, other):
        return self.num / self.den > other.num / other.den

    def __le__(self, other):
        return self.num / self.den <= other.num / other.den

    def __ge__(self, other):
        return self.num / self.den >= other.num / other.den

    def __mul__(self, other):
        return (self.num * other.num) / (self.den * other.den)

    def __truediv__(self, other):
        return (self.num * other.den) / (self.den * other.num)

    def __str__(self):
        return f'{self.num}/{self.den}'


a = Fraction(1, 4)
b = Fraction(2, 6)
print(a + b)
