import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.older_book'
function = "older_book"


@points('8.older_book')
class OlderBookTest(unittest.TestCase):
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

    def test1_function_exists(self):
        try:
            from src.older_book import older_book
        except:
            self.fail("Your program should contain function older_book(book1: Book, book2: Book)")

    def test1b_luokkamaarittely_olemassa(self):
        try:
            from src.older_book import Book
        except:
            self.fail("Your program should contain class Book!")

    def test2_return_type(self):
        try:
            from src.older_book import older_book
            from src.older_book import Book
            
            val = older_book(Book("Python","P. Python", "non-fiction", 2000), Book("Java", "J.Java", "non-fiction", 2001))
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(val == None, f"Function older_book should not return a value," +  
                f" now it returns a value {val} of type {taip}\nwhen it's called with arguments\n" + 
                'older_book(Book("Python","P. Python", "non-fiction", 2000), Book("Java", "J.Java", "non-fiction", 2001))')
        except Exception as e:
            self.fail(f"Function threw an error when called with argument values\n" + 
                f'older_book(Book("Python","P. Python", "non-fiction", 2000), Book("Java", "J.Java", "non-fiction", 2001))\n{e}')


    def test3_test_first_older(self):
        test_cases = ((("Seven Brothers", "Aleksis Kivi", "Novel", 1870), 
                       ("The Egyptian", "Mika Waltari", "Novel", 1945)),
                       (("The Cyberiad", "Stanislaw Lem", "Sci-fi", 1965), 
                       ("Brief History of Time", "Stephen Hawking", "Science", 1986)))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
                reload_module(self.module)
                older_book = load(exercise, function, 'en')
                from src.older_book import Book

                k1,k2 = test_case
                book1 = Book(k1[0],k1[1],k1[2],k1[3])
                book2 = Book(k2[0],k2[1],k2[2],k2[3])
                older = book1
                not_older = book2

                corr = f"{older.name} is older, it was published in {older.year}"

                older_book(book1,book2)
                
                output = get_stdout()
                output = output.replace("\n","").strip()

                self.assertTrue("older" in output and older.name in output and not_older.name not in output and 
                    str(older.year) in output and str(not_older.year) not in output, 
                    f"Program output\n{output}\nis different to model answer\n{corr}\nwhen books are\n{test_case}")

    def test4_test_second_older(self):
        test_cases =  ((("The Eigth Brother", "Alex Stone", "Novel", 1970), 
                       ("The Egyptian", "Mika Waltari", "Novel", 1945)),
                       (("The Son of Cyberiad", "Lenislaw Stam", "Sci-fi", 1995), 
                       ("Brief History of Time", "Stephen Hawking", "Science", 1986)))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
                reload_module(self.module)
                older_book = load(exercise, function, 'en')
                from src.older_book import Book

                k1,k2 = test_case
                book1 = Book(k1[0],k1[1],k1[2],k1[3])
                book2 = Book(k2[0],k2[1],k2[2],k2[3])
                older = book2
                not_older = book1

                corr = f"{older.name} is older, it was published in {older.year}"

                older_book(book1,book2)
                
                output = get_stdout()
                output = output.replace("\n","").strip()

                self.assertTrue("older" in output and older.name in output and not_older.name not in output and 
                    str(older.year) in output and str(not_older.year) not in output, 
                    f"Program output\n{output}\nis different to model answer\n{corr}\nwhen books are\n{test_case}")

    def test5_test_equally_old(self):
        test_cases =  ((("The Ninth Brother", "Alex Stone", "Novel", 1980), 
                       ("The Egyptian, part II", "Mikael Watson", "Novel", 1980)),
                       (("The Son of Cyberiad", "Lenislaw Stam", "Sci-fi", 1995), 
                       ("Even Briefer History of Time", "Hawk Stephenson", "Science", 1995)))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                older_book = load(exercise, function, 'en')
                from src.older_book import Book

                k1,k2 = test_case
                book1 = Book(k1[0],k1[1],k1[2],k1[3])
                book2 = Book(k2[0],k2[1],k2[2],k2[3])
               
                corr = f"{book1.name} and {book2.name} were published in {book1.year}"

                older_book(book1,book2)
                
                output = get_stdout()
                output = output.replace("\n","").strip()

                self.assertTrue("and" in output and book1.name in output and book2.name in output and 
                    str(book1.year) in output, 
                    f"Program output\n{output}\nis different to model answer\n{corr}\nwhen books are\n{test_case}")
                
    

if __name__ == '__main__':
    unittest.main()
