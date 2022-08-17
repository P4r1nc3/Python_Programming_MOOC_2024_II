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

@points('10.phonebook_part_2_2')
class PhoneBook2_Part2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'en')

    def test_1_stops(self):
        syote = ["0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with input\n{s(syote)}")
                
            output = get_stdout()

    def test_2_works_with_number_input(self):
        syote = ["1", "Erkki", "02-123456", "2",  "Erkki", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with input\n{s(syote)}")
                
            output = get_stdout()
            expected = "02-123456"
            self.assertTrue(expected in output, f"The output of your program should be\n{expected}\nwith input\n{s(syote)}\nNow the output was\n{output}")   

    def test_3_works_many_numbers(self):
        syote = ["1", "Emilia", "09-123456", "1", "Emilia", "040-999999", "2", "Emilia", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with input\n{s(syote)}")
                
            output = get_stdout()
            expected = "09-123456"
            self.assertTrue(expected in output, f"The output of your program should be\n{expected}\nwith input\n{s(syote)}\nNow the output was\n{output}")   
            expected = "040-999999"
            self.assertTrue(expected in output, f"The output of your program should be\n{expected}\nwith input\n{s(syote)}\nNow the output was\n{output}")   

    def test_4_works_no_number_1(self):
        syote = ["2", "Pekka", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with input\n{s(syote)}")
                
            output = get_stdout()
            expected = "number unknown"
            self.assertTrue(expected in output, f"The output of your program should be\n{expected}\nwith input\n{s(syote)}\nNow the output was\n{output}")   

    def test_5_works_no_number_2(self):
        syote = ["1", "Emilia", "09-123456", "1", "Emilia", "040-999999", "2", "Pekka", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with input\n{s(syote)}")
                
            output = get_stdout()
            expected = "number unknown"
            self.assertTrue(expected in output, f"The output of your program should be\n{expected}\nwith input\n{s(syote)}\nNow the output was\n{output}")   

            expected = "09-123456"
            self.assertFalse(expected in output, f"The output of your program should NOT contain\n{expected}\nwith input\n{s(syote)}\nNow the output was\n{output}")   
            expected = "040-999999"
            self.assertFalse(expected in output, f"The output of your program should NOT contain\n{expected}\nwith input\n{s(syote)}\nNow the output was\n{output}")   

    def test_6_person_in_use(self):
        src_file = os.path.join('src', 'phone_book_v2.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "class PhoneBook"  in line and not ("STUB: class PhoneBook:" in line):
                    p = True
                elif p and "class " in line:
                    p = False 
                elif p:
                    lines.append(line)

        required = [
            "Person("
        ]

        for v in required:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"Class PhoneBook must use Person class objects to save person information!")   
       
        forbidden = [
            ".append("
        ]

        for v in forbidden:
            on = False
            for line in lines:
                if v in line:         
                    self.fail(f"Class PhoneBook must use Person class objects to save person information! Next line does not belong to the code\n{line}")   

if __name__ == '__main__':
    unittest.main()

