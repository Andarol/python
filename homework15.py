# Task 1

# Make a class called Person.
# Make the __init__() method take firstname,
# lastname, and age as parameters and add them
# as attributes. Make another method called talk()
# which makes prints a greeting from the person containing,
# for example like this: “Hello, my name is Carl Johnson and
# I’m 26 years old”.

class Person():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


def talk(name, lastname, age):
    talk1 = Person(name, lastname, age)
    return f"Hello, my name is {talk1.firstname} {talk1.lastname} and I’m {talk1.age} years old"


print(talk('oleks', 'gero', '23'))


# Task 2

# Doggy age

# Create a class Dog with class attribute
# `age_factor` equals to 7.
# Make __init__() which takes values for
# a dog’s age. Then create a method `human_age`
# which returns the dog’s age in human equivalent.
class Dog():
    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * 7


doberman = Dog(9)
print(doberman.age)
print(doberman.human_age())


# task3
# Create a simple prototype of a TV controller in Python.
# It’ll use the following commands:
class TVController():
    count1 = 0

    def __init__(self, channels):
        self.channels = channels

    def first_channel(self):
        TVController.count1 = 0
        print(self.channels[TVController.count1])
        return TVController.count1

    def last_channel(self):
        TVController.count1 = len(self.channels) - 1
        print(self.channels[TVController.count1])
        return TVController.count1

    def next_channel(self):
        if TVController.count1 == len(self.channels) - 1:
            TVController.count1 = 0
        else:
            TVController.count1 += 1
        print(self.channels[TVController.count1])
        return TVController.count1

    def previous_channel(self):
        TVController.count1 -= 1
        print(self.channels[TVController.count1])
        return TVController.count1

    def current_channel(self):
        print(self.channels[TVController.count1])
        return TVController.count1

    def is_exist(self, n):
        self.n = n
        if type(n)==int:
            if int(n) == len(self.channels):
                return 'yes'
            else:
                return 'no'
        else:
            for i in self.channels:
                if i == n:
                    return 'yes'
                else:
                    return 'no'
    def turn_channel(self,n):
        n = n-1
        TVController.count1 = n
        print(self.channels[n])
        return TVController.count1

CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = TVController(CHANNELS)

controller.first_channel()
controller.last_channel()

controller.turn_channel(1)

controller.next_channel()

controller.previous_channel()

controller.current_channel()

print(controller.is_exist(4))

print(controller.is_exist("BBC"))
