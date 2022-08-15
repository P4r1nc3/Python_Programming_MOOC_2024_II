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

exercise = 'src.list_helper'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('9.list_helper')
class ListHelperTest(unittest.TestCase):
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
            from src.list_helper import ListHelper
        except Exception as e:
            self.fail(f'Class ListHelper is not found: \n{e}\n' + 
            'Make sure, that the class is not broken.')

    def test_2_methods_exists(self):
        from src.list_helper import ListHelper
        try:
            val = ListHelper.greatest_frequency([1,1,2])
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == int, f'Method ListHelper.greatest_frequency should ' +
                f'return a value, which is of type integer.\n' + 
                f'Now it returns a value {val} which is of type {taip}.\n' + 
                f'Method were called as follows: ListHelper.greatest_frequency([1,1,2])')
        except Exception as e:
            self.fail(f'Method call ListHelper.greatest_frequency([1,1,2]) threw an error\n{e}')

        try:
            val = ListHelper.doubles([1,1,2])
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == int, f'Method ListHelper.doubles should ' +
                f'return a value, which is of type integer.\n' + 
                f'Now it returns a value {val} which is of type {taip}.\n' + 
                f'Method were called as follows: ListHelper.doubles([1,1,2])')
        except Exception as e:
            self.fail(f'Method call ListHelper.doubles([1,1,2]) threw an error\n{e}')

    def test_3_greatest_frequency(self):
        from src.list_helper import ListHelper
        test_cases = [[1,1,1,2,2,3], [3,2,3,2,2,3,2,2,1,1,2], [1,5,4,5,6,7,7,5,7,7,7,], 
                      [1,2,3,1,2,3,1,2,3,4,4,4,3,4,4,3,4,4,3,2,1,4,4,4,4,4,4,4,3,2,1]]
        for test_case in test_cases:
            val = ListHelper.greatest_frequency(test_case)
            corr = max([(x,test_case.count(x)) for x in test_case], key = lambda y: y[1])[0]

            self.assertEqual(val, corr, f'Method ListHelper.greatest_frequency should ' + 
                f'return {corr}, when the list is\n{test_case}\nbut method returns {val}.')

    def test_3_doubles(self):
        from src.list_helper import ListHelper
        test_cases = [[1,1,1,2,2,3], [3,2,3,2,2,3,1,2,4,5,5,6], [1,5,4,5,6,7,7,5,7,7,7,], 
                      [9,8,7,9,8,6,6,5,5,4,3,3]]
        for test_case in test_cases:
            val = ListHelper.doubles(test_case)
            corr = len([x for x in set(test_case) if test_case.count(x) > 1])

            self.assertEqual(val, corr, f'Method ListHelper.doubles should ' + 
                f'return {corr}, when the list is\n{test_case}\nbut method returns {val}.')

if __name__ == '__main__':
    unittest.main()
