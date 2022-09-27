import unittest
import pytest
import os.path
# Task 1

# File Context Manager class

# Create your own class, which can behave like a built-in function `open`.
# Also, you need to extend its functionality with counter and logging.
# Pay special attention to the implementation of `__exit__` method,
# which has to cover all the requirements to context managers mentioned here:


class Manager_With:
    def __init__(self, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs

    def __enter__(self):
        self.file = open(*self.__args, **self.__kwargs)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with Manager_With('new_file.txt', 'w') as f:
    f.write('life is benteshne')


# Task 2

# Writing tests for context manager

# Take your implementation of the context manager class
# from Task 1 and write tests for it. Try to cover as many
# use cases as you can, positive ones when a file exists and
# everything works as designed. And also, write tests when your
# class raises errors or you have errors in the runtime context suite.


class Test_of_manager(unittest.TestCase):
    def test_with(self):
        with Manager_With('new_file.txt', 'r') as f:
            self.assertEqual('life is benteshne', f.readline())

    def test_it_write(self):
        with Manager_With('new_file.txt', 'r') as f:
            self.assertTrue(isinstance(f.readline(), str))
#Task 3
@pytest.mark.parametrize("file_obj", ['new_file.txt'])
def test(file_obj):
    with Manager_With(file_obj, 'r') as f:
        file_name, file_extension = os.path.splitext(file_obj)
        assert file_extension == '.txt'


@pytest.mark.parametrize("file_obj", ['new_file.txt'])
def test1(file_obj):
    with Manager_With(file_obj, 'r') as f:
        assert isinstance(f.readline(), str) == True

