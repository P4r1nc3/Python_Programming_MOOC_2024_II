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

exercise = 'src.laptop_computer'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('10.laptop_computer')
class LaptopComputerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
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
            from src.laptop_computer import Computer
            a = Computer("hal", 1)
        except Exception as e:
            self.fail(f'Calling constructor Computer("hal", 1) threw an error \n{e}\n' + 
            'Are you sure you have not changed the class Computer?')

        try:
            from src.laptop_computer import LaptopComputer
            a = LaptopComputer("hal", 1, 1)
        except Exception as e:
            self.fail(f'Calling constructor LaptopComputer("hal", 1, 1) threw an error \n{e}\n' + 
            'Please check, that the class is defined!')

    def test_2_inheritance(self):
        from src.laptop_computer import Computer, LaptopComputer
        a = LaptopComputer("hal", 1, 1)
        self.assertTrue(isinstance(a, Computer), f"Class LaptopComputer should inherit " +
            'the class Computer!')

    def test_3_str_works(self):
        from src.laptop_computer import Computer, LaptopComputer
        test_cases = [("C65",1,10), ("IPM MicroMary", 128, 4), ("Zony", 1650, 4)]
        for test_case in test_cases:
            kone = LaptopComputer(test_case[0], test_case[1], test_case[2])
            val = str(kone)
            corr = f"{test_case[0]}, {test_case[1]} MHz, {test_case[2]} kg"
            self.assertEqual(val, corr, f'Method __str__ should return\n{corr}\n' + 
                f'Now method returns\n{val}\nwhen object was initalized as:\n' + 
                f'LaptopComputer("{test_case[0]}", {test_case[1]}, {test_case[2]})')

        

    
if __name__ == '__main__':
    unittest.main()
