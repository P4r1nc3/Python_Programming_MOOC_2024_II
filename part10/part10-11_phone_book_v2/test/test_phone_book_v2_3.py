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

exercise = 'src.phone_book_v2'

def f(attr: list):
    return ",".join(attr)

def s(l: list):
    return "\n".join(l)

@points('10.phonebook_part2_3')
class PhoneBook2_Part2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'en')

    def test_1_works_number_found(self):
        input_values = ["1", "Erkki", "02-123456", "2",  "Erkki", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with input\n{s(input_values)}")
                
            output = get_stdout()
            expected = "02-123456"
            self.assertTrue(expected in output, f"Program output should contain\n{expected}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   
            expected = "address unknown"
            self.assertTrue(expected in output, f"Program output should contain\n{expected}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   

    def test_2_works_add_address(self):
        input_values = ["3", "Erkki", "Linnankatu 10", "2",  "Erkki", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with input\n{s(input_values)}")
                
            output = get_stdout()
            expected = "number unknown"
            self.assertTrue(expected in output, f"Program output should contain\n{expected}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   
            expected = "Linnankatu 10"
            self.assertTrue(expected in output, f"Program output should contain\n{expected}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   
 
    def test_2_works_if_addressa_and_number(self):
        input_values = ["3", "Emilia", "Mannerheimintie 100", "1", "Emilia", "044-121212","2", "Emilia", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with input\n{s(input_values)}")
                
            output = get_stdout()
            expected = "044-121212"
            self.assertTrue(expected in output, f"Program output should contain\n{expected}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   
            expected = "Mannerheimintie 100"
            self.assertTrue(expected in output, f"Program output should contain\n{expected}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   
            expected = "number unknown"
            self.assertFalse(expected in output, f"The output of your program should not contain\n{expected}\nwith input\n{s(input_values)}\nOutput was\n{output}")   
            expected = "address unknown"
            self.assertFalse(expected in output, f"The output of your program should not contain\n{expected}\nwith input\n{s(input_values)}\nOutput was\n{output}")


    def test_4_works_with_unknown(self):
        input_values = ["2",  "Erkki", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with input\n{s(input_values)}")
                
            output = get_stdout()
            expected = "number unknown"
            self.assertTrue(expected in output, f"Program output should contain\n{expected}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   
            expected = "address unknown"
            self.assertTrue(expected in output, f"Program output should contain\n{expected}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   

if __name__ == '__main__':
    unittest.main()
