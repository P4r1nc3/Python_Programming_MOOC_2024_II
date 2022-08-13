import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.books_of_genre'
function = "books_of_genre"


@points('8.books_of_genre')
class BooksOfGenreTest(unittest.TestCase):
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
            from src.books_of_genre import books_of_genre
        except:
            self.fail("Your program should have a function books_of_genre(books: list, genre: str)")

    def test1b_class_exists(self):
        try:
            from src.books_of_genre import Book
        except:
            self.fail("Your program should contain the definition of class Book!")

    def test2_return_type(self):
        try:
            from src.books_of_genre import books_of_genre
            from src.books_of_genre import Book
            
            val = books_of_genre([Book("Python","P. Python", "non-fiction", 2000), Book("Java", "J.Java", "non-fiction", 2001)], "non-fiction")
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == list, f"Function books_of_genre should return a list," +  
                f" now it returns {val} which is of type {taip}\n when it's called with arguments\n" + 
                'books_of_genre([Book("Python","P. Python", "non-fiction", 2000), Book("Java", "J.Java", "non-fiction", 2001)])')
        except Exception as e:
            self.fail(f"Function threw an error when called with arguments\n" +
                f'books_of_genre([Book("Python","P. Python", "non-fiction", 2000), Book("Java", "J.Java", "non-fiction", 2001)])\n{e}')


    def test3_test_list1(self):
        test_case = [("Seven Brothers", "Aleksis Kivi", "Novel", 1870), 
                       ("The Egyptian", "Mika Waltari", "Novel", 1945),
                       ("The Cyberiad", "Stanislaw Lem", "Sci-fi", 1965), 
                       ("A Brief History of Time", "Stephen Hawking", "Science", 1988)]
        genre = "Novel"
        
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
            reload_module(self.module)
            books_of_genre = load(exercise, function, 'en')
            from src.books_of_genre import Book

            book_list = [Book(x[0],x[1],x[2],x[3]) for x in test_case]
            corr = sorted([x for x in book_list if x.genre == genre], key = lambda x: x.name)
            val = sorted(books_of_genre(book_list, genre), key = lambda x: x.name)
            
            self.assertEqual(corr, val, f"Function should return values\n{corr}\nNow it returns\n{val}\n...when arguments were\n{test_case}")

    def test4_test_list2(self):
        test_case = [("Seven Brothers", "Aleksis Kivi", "Novel", 1870), 
                       ("The Egyptian", "Mika Waltari", "Novel", 1945),
                       ("The Cyberiad", "Stanislaw Lem", "Sci-fi", 1965), 
                       ("A Brief History of Time", "Stephen Hawking", "Science", 1988), 
                       ("2001: a Space Odyssey", "Arthur C. Clarke", "Sci-fi", 1968)]
        genre = "Sci-fi"
        
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
            reload_module(self.module)
            books_of_genre = load(exercise, function, 'en')
            from src.books_of_genre import Book

            book_list = [Book(x[0],x[1],x[2],x[3]) for x in test_case]
            corr = sorted([x for x in book_list if x.genre == genre], key = lambda x: x.name)
            val = sorted(books_of_genre(book_list, genre), key = lambda x: x.name)
            
            self.assertEqual(corr, val, f"Function should return values\n{corr}\nNow it returns\n{val}\n...when arguments were\n{test_case}")

                
    

if __name__ == '__main__':
    unittest.main()
