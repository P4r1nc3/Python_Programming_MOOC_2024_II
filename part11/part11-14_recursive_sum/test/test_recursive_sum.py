import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re

exercise = 'src.recursive_sum'

@points('11.recursive_sum')
class RecursiveSumTest(unittest.TestCase):
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
    
    def test_1_function_exists(self):
        try:
            from src.recursive_sum import recursive_sum
        except Exception as e:
            self.fail(f'Your program should contain function named recursive_sum.')

    def test_2_type_of_return_value(self):
        try:
            from src.recursive_sum import recursive_sum
            val = recursive_sum(1)
        except Exception as e:
            self.assertTrue(False, f"Function threw an error when it was called as follows:" + 
                f'\nrecursive_sum(1)\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == int, f"Function recursive_sum is expected to return value, which is of type int," +  
            f" now it returns a value {val} which is of type {taip}\n when it is called as follows\n" +  
            'recursive_sum(1)')
        

    def test_3_is_recursive(self):
        from src.recursive_sum import recursive_sum
        self.assertTrue(reflect.test_recursion(recursive_sum, 2), 
            f'"Function recursive_sum should call itself recursively.\n' + 
            f'Now calling recursive_sum(2) does not lead to new calls of function recursive_sum.')

    def test_4_test_with_values(self):
        from src.recursive_sum import recursive_sum
        test_cases = [2,4,6,8,7,5,3]
        for test_case in test_cases:
            val = recursive_sum(test_case)
            corr = sum(list(range(test_case + 1)))

            self.assertEqual(val, corr, f'Function should return value\n{corr}\n' + 
            f'when it is called with the parameter\n{test_case}\nnow function returns\n' + 
            f'{val}')

if __name__ == '__main__':
    unittest.main()
