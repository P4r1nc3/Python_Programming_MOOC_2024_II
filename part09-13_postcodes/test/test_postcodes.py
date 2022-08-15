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

exercise = 'src.postcodes'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('9.postcodes')
class PostcodeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected.")]):
           cls.module = load_module(exercise, 'en')

    
    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_1_class_exists(self):
        try:
            from src.postcodes import City
            a = City("Helsinki", 500000)
        except Exception as e:
            self.fail(f'Calling constructor City("Helsinki", 500000) threw an error \n{e}\n' + 
            'Make sure, that the class is not broken.')

    def test_2_variable_exists(self):
        from src.postcodes import City
        val = City.postcodes
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == dict, f'Class variable City.postcodes should refer to a dictionary (dict). ' +
            f'Now its value is {val} which is of type {taip}.')


    def test_3_values(self):
        from src.postcodes import City
        test_cases = [("Helsinki", "00100"), 
                    ("Turku", "20100"),
                    ("Tampere", "33100"),
                    ("Rovaniemi", "96100"),
                    ("Oulu", "90100")]
        val = City.postcodes

        for test_case in test_cases:
            if test_case[0] not in val or val[test_case[0]] != test_case[1]:
                    self.fail(f'From the dictionary City.postcodes should be found following key-value-pair:\n' + 
                        f'{test_case[0]}: {test_case[1]}')
            
   
if __name__ == '__main__':
    unittest.main()
