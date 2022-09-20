# task1
# Create your own implementation
# of a built-in function enumerate,
# named `with_index`, which takes two parameters
# : `iterable` and `start`, default is 0. Tips:
# see the documentation for the enumerate function
def with_index(list_to_iterate, start=0):
    for i in list_to_iterate:
        yield start, i
        start += 1


arr = [1, 2, 3, 4, 5, 6]
for i in with_index(arr, 10):
    print(i)


# task2
# Create your own implementation of a built-in
# function range, named in_range(), which takes
# three parameters: `start`, `end`, and optional step.
# Tips: See the documentation for `range` function
def in_range(start, end, step=1):
    n = start
    iters = -1
    if start < 0 and end > 0:
        number_of_iterations = (abs(start) + abs(end)) // step
    else:
        number_of_iterations = (abs(start) - abs(end)) // step

    while iters != number_of_iterations:
        yield n
        n += step
        iters += 1


for i in in_range(-20, -5,2):
    print(i,'in_range')


# task 3
# Create your own implementation of an iterable,
# which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.
class MyIterable:
    def __init__(self, *args):
        self.list_ = list(args)
        self.max = len(args)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n == self.max:
            raise StopIteration

        result = self.list_[self.n]
        self.n += 1
        return result

    def __getitem__(self, index):
        return self.list_[index]


for i in MyIterable(1, 2, 3, 4, 5, 6, 7, 8, 9):
    print(i)
