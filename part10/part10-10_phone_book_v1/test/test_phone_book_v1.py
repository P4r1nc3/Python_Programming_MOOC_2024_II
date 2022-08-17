import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date, datetime, timedelta

exercise = 'src.phone_book_v1'

def f(attr: list):
    return ",".join(attr)

def s(l: list):
    return "\n".join(l)

def clear_file():
    with open("luettelo.txt", "w"):
        pass

@points('10.phone_book_osa1')
class PhoneBookTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'en')

    def test_1_stops(self):
        clear_file()
        syote = ["0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"check that your program works with input\n{s(syote)}")  

    def test_2_search_works_after_add(self):
        clear_file()
        syote = ["1", "Erkki", "02-123456", "2",  "Erkki", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that you program works with input\n{s(syote)}")
                
            output = get_stdout()
            self.assertFalse(len(output)==0,f'Your code does not output anything with input\n{s(syote)}\nIn this program, no code should be included inside the if __name__ == "__main__" block')

            expected = "02-123456"
            self.assertTrue(expected in output, f"The output of  the program should be\n{expected}\nwith input\n{s(syote)}\nOutput was\n{output}")   

    def test_3_by_number_1(self):
        clear_file()
        syote = ["1", "Erkki", "02-123456", "3",  "02-123456", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that you program works with input\n{s(syote)}")
                
            output = get_stdout()
            expected = "Erkki"
            self.assertTrue(expected in output, f"The output of  the program should be\n{expected}\nwith input\n{s(syote)}\nOutput was\n{output}")   

    def test_3_by_number_2(self):
        clear_file()
        syote = ["1", "Emilia", "09-123456", "3",  "09-123456", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that you program works with input\n{s(syote)}")
                
            output = get_stdout()
            expected = "Emilia"
            self.assertTrue(expected in output, f"The output of  the program should be\n{expected}\nwith input\n{s(syote)}\nOutput was\n{output}")   
    
    def test_3_by_number_3(self):
        clear_file()
        syote = ["1", "Emilia", "045-333444", "1", "Emilia", "09-123456", "3",  "09-123456", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that you program works with input\n{s(syote)}")
                
            output = get_stdout()
            expected = "Emilia"
            self.assertTrue(expected in output, f"The output of  the program should be\n{expected}\nwith input\n{s(syote)}\nOutput was\n{output}")   
            expected = "unknown number"
            self.assertFalse(expected in output, f"The output should not contain line\n{expected}\nwith input\n{s(syote)}\nOutput was\n{output}") 

    def test_3_by_number_3(self):
        clear_file()
        syote = ["1", "Emilia", "045-333444", "1", "Erkki", "02-123456", "3",  "040-332211", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that you program works with input\n{s(syote)}")
                
            output = get_stdout()
            expected = "unknown number"
            self.assertTrue(expected in output, f"The output of  the program should be\n{expected}\nwith input\n{s(syote)}\nOutput was\n{output}")   
            expected = "Erkki"
            self.assertFalse(expected in output, f"The output should not contain line\n{expected}\nwith input\n{s(syote)}\nOutput was\n{output}") 

if __name__ == '__main__':
    unittest.main()