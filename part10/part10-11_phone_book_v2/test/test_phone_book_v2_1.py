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

@points('10.phonebook_part2_1')
class PhoneBook2_Osa1Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'en')

    def test1_person_exists(self):
        try:
            from src.phone_book_v2 import Person
        except:
            self.fail("Your class should contain a class Person")
        try:
            Person("Erkki")
        except Exception as e:
            self.fail('Calling constructor Person("Erkki")' +
                f' threw an error: {e}\nCheck that the constructor is defined correctly!')

    def test2_person_works(self):
        from src.phone_book_v2 import Person
        h = Person("Erkki")
        code = """
h = Person("Erkki")
h.name()
"""
        try:
            p = h.name()
        except Exception as e:
            self.fail(f'Executing\n{code}\nthrew an error\n{e}\nCheck that method name(self) is defined?')
        exp = "Erkki"
        self.assertEqual(exp, p,  f'\nWhen this code is executed:\n{code}\nmethod should return {exp}, now the return value was {p}')

        code = """
h = Person("Erkki")
h.numbers()
"""            
        try:
            p = h.numbers()
        except Exception as e:
            self.fail(f'Executing\n{code}\nthrew an error\n{e}\nCheck that method numbers(self) is defined?')
        exp = []
        self.assertEqual(exp, p,  f'\nWhen this code is executed:\n{code}\nmethod should return {exp}, now the return value was {p}')

        code = """
h = Person("Erkki")
h.add_number("040-445566")
"""        
        try:
            h.add_number("040-445566")
        except Exception as e:
            self.assertEqual(exp, p,  f'\nWhen this code is executed:\n{code}\nmethod should return {exp}, now the return value was {p}')      
        
        code = """
h = Person("Erkki")
h.add_number("040-445566")
h.numbers()
"""    
        try:
            p = h.numbers()
        except Exception as e:
            self.fail(f'Executing\n{code}\nthrew an error\n{e}\nCheck that method numbers(self) is defined?')
        exp = ["040-445566"]
        self.assertEqual(exp, p,  f'\nWhen this code is executed:\n{code}\nmethod should return {exp}, now the return value was {p}')

        code = """
h = Person("Erkki")
h.add_number("040-445566")
h.add_number("02-121212")
h.numbers()
"""    

        try:
            p = h.numbers()
        except Exception as e:
            self.fail(f'Executing\n{code}\nthrew an error\n{e}\nCheck that method numbers(self) is defined?')
        exp = ["040-445566"]
        self.assertEqual(exp, p,  f'\nWhen this code is executed:\n{code}\nmethod should return {exp}, now the return value was {p}')

        code = """
h = Person("Erkki")
h.address()
"""            
        try:
            p = h.address()
        except Exception as e:
            self.fail(f'Executing\n{code}\nthrew an error\n{e}\nCheck that method address(self) is defined?')
        exp = None
        self.assertEqual(exp, p,  f'\nWhen this code is executed:\n{code}\nmethod should return {exp}, now the return value was {p}')

        code = """
h = Person("Erkki")
h.add_address("Linnankatu 1")
"""        
        try:
            h.add_address("Linnankatu 1")
        except Exception as e:
            self.fail(f'Executing\n{code}\nthrew an error\n{e}\nCheck that method add_address(self, address: str) is defined?')        
        
        code = """
h = Person("Erkki")
h.add_address("Linnankatu 1")
h.address()
"""        
        try:
            p = h.address()
        except Exception as e:
            self.fail(f'Executing\n{code}\nthrew an error\n{e}\nCheck that method add_address(self, address: str) is defined?')        
        exp = "Linnankatu 1"
        self.assertEqual(exp, p,  f'\nWhen this code is executed:\n{code}\nmethod should return {exp}, now the return value was {p}')

if __name__ == '__main__':
    unittest.main()

