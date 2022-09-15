# task1
# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student,
# and another one called Teacher.
# Try to find as many methods and attributes
# as you can which belong to different classes,
# and keep in mind which are common and which are not.
# For example, the name should be a Person attribute,
# while salary should only be available to the teacher.
class Person:
    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex

    def __repr__(self):
        return f'{self.__name},{self.__age},{self.__sex}'


class Teacher(Person):
    def __init__(self, name, age, sex, subject):
        super().__init__(name, age, sex)
        self.__subject = subject

    def mark(self, student, subject, mark):
        student.get_mark(subject, mark)


class Student(Person):
    def __init__(self, name, age, sex, grade):
        super().__init__(name, age, sex)
        self.__grade = grade
        self.__dict = {}

    def get_mark(self, subject, mark):
        self.__dict[f'{subject}'] = mark
        return self.__dict

    def please_i_whant_marks(self):
        return self.__dict


class School:
    def __init__(self):
        self.__number_0f_students = []
        self.__number_0f_techers = {}

    def append_student(self, student):
        self.__number_0f_students.append(student)

    def append_techers(self, techer, subject):
        self.__number_0f_techers[f'{subject}'] = techer


school = School()
Sashs = Student('sasha', '44', 'm', '1')
Coldemar = Teacher('Cold', '12', 'm', 'math')
school.append_techers(Coldemar, 'math')
school.append_student(Sashs)
Coldemar.mark(Sashs, 'math', 7)
print(Sashs.please_i_whant_marks())


# Task 2
# Implement a class Mathematician which is a helper class for doing math operations on listscla
class Mathematican():
    def square_nums(self, list=[]):
        return [i ** 2 for i in list]

    def remove_positives(self, list=[]):
        return [i for i in list if i >= 0]

    def filter_leaps(self, list=[]):
        return [i for i in list if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0)]


m = Mathematican()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))


# The class doesn't take any attributes and only has methods:
# task 3
# Write a class Product that has three attributes:
class Product:
    def __init__(self, type1, name, price):
        self.type1 = type1
        self.name = name
        self.price = price

    def __call__(self):
        return self.type1, self.name, self.price


class ProductStore:
    def __init__(self):
        self.storage = []
        self.money = 0

    def add(self, product, amount):
        if [product.type1, product.name] not in [[i["product"].name, i["product"].type1] for i in self.storage]:
            self.storage.append({"product": product,
                                 "amount": amount,
                                 "discount": 1})
            return
        else:
            for i in self.storage:
                if i['product'].name == product.name and i['product'].type == product.type:
                    i['amount'] += amount
                    return

    def get_all_products(self):
        info = []
        for i in self.storage:
            name, type1, price = i["product"]()
            info.append({"name": name,
                         "type": type1,
                         "price": price,
                         "amount": i["amount"],
                         "discount": i["discount"]})
        return info

    def set_discount(self, name_of_product, discount, type_of_product="name"):
        if type_of_product == "name":
            for i in self.storage:
                if i["product"].name == name_of_product:
                    i["discount"] = discount / 100
        elif type_of_product == "type":
            for i in self.storage:
                if i["product"].type == name_of_product:
                    i["discount"] = discount / 100

    def sell_product(self, productname, amount):
        for i in self.storage:
            if i["product"].name == productname:
                i["amount"] -= amount
                self.money += i["product"].price * amount * i["discount"]

    def get_income(self):
        return self.money

    def get_product_info(self, product_name):
        for i in self.storage:
            if i["product"].name == product_name:
                result = (i["product"].name, i["amount"], i['discount'])
        return result


product = Product('sport', 'ball', 1000)

product1 = Product('food', 'eggs', 10)

store = ProductStore()
store.add(product, 1)
store.add(product1, 1000)
store.set_discount('eggs', 10)
store.sell_product('eggs', 100)
print(store.get_product_info('eggs'))
print(store.get_income())
print(store.get_all_products())



# type
# name
# price
# Then create a class ProductStore,
# which will have some Products and will operate with
# all products in the store. All methods, in case they
# can’t perform its action, should raise ValueError with
# appropriate error information.

# Tips: Use aggregation/composition concepts while implementing the ProductStore class.
# You can also implement additional classes to operate on a certain type of product, etc.
# Task 4
# Create your custom exception named `CustomException`,
# you can inherit from base Exception class, but extend
# its functionality to log every error message to a file named
# `logs.txt`. Tips: Use __init__ method to extend functionality
# for saving messages to file


class CustomException(Exception):
    def __init__(self, msg):
        with open('somefile.txt', 'a') as the_file:
            the_file.write(f'{CustomException}, s {msg}')


try:
    CustomException('exception')
    raise CustomException('exderfer')
except CustomException:
    with open('somefile.txt', 'r') as the_file:
        print(the_file.read())
#task with star
"""
html = HTML(Head -> class, Body -> class)
body = Body(Div -> class)
HTML -> те що збирає теги(класи) до купи

"""


class Tag:
    def __init__(self, tag_name, content=[], tag_name_class={}):
        self.tag_name = tag_name
        self.content = content
        self.tag_name_class = tag_name_class

    def __str__(self):
        content = ''
        if type(self.content) == list:
            content = '\n'
            for i in self.content:
                content += str(i) + '\n'
        else:
            content = self.content
        content = str(content).replace('\n', '\n\t')
        if len(self.tag_name_class) == 0:
            return f"<{self.tag_name}>\n\t{content}\n</{self.tag_name}>"
        if len(self.tag_name_class) > 0 or len((self.tag_name_class)) < 0:
            return f"<{self.tag_name} {list(self.tag_name_class.keys())[0]} = \"{list(self.tag_name_class.values())[0]}\">\n\t{content}\n</{self.tag_name}>"

    # def generate(self):
    #     if type(self.content) == Tag:
    #         smth = self.content.generate()
    #     else:
    #         smth = self.content
    #     return f"<{self.tag_name}>{smth}</{self.tag_name}>"


class Html(Tag):
    def __init__(self, content):
        super().__init__("html", content)

    def __str__(self):
        return f"<!DOCTYPE html>\n{self.content}"


class Tag_Tag(Tag):
    def __init__(self, name_of_tag, content, tag_name_class={}):
        super().__init__(name_of_tag, content, tag_name_class)


if __name__ == "__main__":
    tag = Html(Tag_Tag('html', [
        Tag_Tag('div', ["first",Tag_Tag('p', 'Paragraph')], {'class': 'jss5 jss6'}),Tag_Tag('h1','Hello world')]))
    print(tag)
