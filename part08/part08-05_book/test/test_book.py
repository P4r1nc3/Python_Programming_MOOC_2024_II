import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date

exercise = 'src.book'
classname = "Book"

def f(attr: list):
    return ",".join(attr)


@points('8.book')
class BookTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_ok(self):
        ok, line = check_source(self.module)
        message = """All code testing the functions must be inside the
if __name__ == "__main__":
block. The following line must be moved:
"""
        self.assertTrue(ok, message+line)

    def test1_class_exists(self):
        try:
            from src.book import Book
        except:
            self.fail("Your program must contain a class Book")

    def test2_constructor(self):
        try:
            from src.book import Book
            val = Book("Python 1", "Peter Python", "Non-fiction", 2010)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(True, "")
        except Exception as e:
            self.fail('Calling class constructor with Book("Python 1", "Peter Python", "Non-fiction", 2010)' +
                f' threw an error: {e}')

    
    def test3_test_attributes(self):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
            reload_module(self.module)
            from src.book import Book

            attributes = ("name", "author", "genre", "year")

            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(Book("Python 1", "Peter Python", "Non-fiction", 2010))

                self.assertTrue(ref.has_attribute(attr), f"Object should have an attribute {attr}," +  
                    f'\nnow attributes are\n{f(ref.list_attributes(True))}\nwhen constructor was called with arguments ' + 
                    f'Book("Python 1", "Peter Python", "Non-fiction", 2010)')
    
    def test4_test_attribute_types(self):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
            reload_module(self.module)
            from src.book import Book

            attributes = (("name", str), ("author", str), ("genre", str), ("year", int))

            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(Book("Python 1", "Peter Python", "Non-fiction", 2010))
                name,taip = attr

                taip_name = str(taip).replace("<class '", "").replace("'>", "")
                taip2 = str(type(ref.get_attribute(name))).replace("<class '","").replace("'>","")

                self.assertTrue(type(ref.get_attribute(name)) == taip, f"The type of ttribute {name} should be {taip_name}, now it is {taip2}")

    def test5_test_attribute_values(self):
         test_cases = [("Seven Brothers", "Aleksis Kivi", "Novel", 1870), 
                       ("The Egyptian", "Mika Waltari", "Novel", 1945),
                       ("The Cyberiad", "Stanislaw Lem", "Sci-fi", 1965), 
                       ("A Brief History of Time", "Stephen Hawking", "Science", 1988)]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
                reload_module(self.module)
                from src.book import Book

                book = Book(test_case[0], test_case[1], test_case[2], test_case[3])
                
                attributes = ("name", "author", "genre", "year")
                ref = reflect.Reflect()
                ref.set_object(book)

                for i in range(len(attributes)):
                    value = ref.get_attribute(attributes[i])
                    self.assertEqual(value, test_case[i], 
                        f'The value of attribute {attributes[i]} should be {test_case[i]}, now it is {value},\nwhen arguments are \n{test_case}')


if __name__ == '__main__':
    unittest.main()
