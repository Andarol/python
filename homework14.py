# Task 1

# Write a decorator that prints
# a function with arguments passed to it.
def decorator(functt):
    def wrap(name):
        return functt(name)

    return wrap


def test():
    return f'you have printed '


@decorator
def test(name):
    return f'you have printed {name}'


print(test('name'))


# Task 2

# Write a decorator that takes a list of stop
# words and replaces them with * inside the decorated function

def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


def stop_word(l=[]):
    def decorator1(func):
        def wrap(*args):
            string1 = func(*args)
            for i in string1.split():
                for x in l:
                    if i == x:
                        string1 = string1.replace(x, '*')
            return string1

        return wrap

    return decorator1


@stop_word(['pepsi', 'BMW!'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('oleks'))


# Task 3

# Write a decorator `arg_rules`
# that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks
# returns False, the function should return
# False and print the reason it failed; otherwise,
# return the result.
def arg_rules(max_length=15, type_=type, contains=[]):
    def decorator_func(func):
        def wrap(*args, **kwargs):
            if len(args) > 0:
                for i in args:
                    if len(i) > max_length or type(i) != type_ or not all(c in i for c in contains):
                        return False
                    else:
                        return func(*args, **kwargs)

        return wrap
    return  decorator_func

@arg_rules(type_=str,max_length=15,contains=['05','@'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"
print(create_slogan('oleksandrzaichko@gmail.com'))
print(create_slogan('05@SD'))
