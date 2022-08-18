import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re

exercise = 'src.balanced_brackets'

@points('11.balanced_brackets')
class BalanceBracketsTest(unittest.TestCase):
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
            from src.balanced_brackets import balanced_brackets
        except Exception as e:
            self.fail(f'Your program should contain function named balanced_brackets.')

    def test_2_type_of_return_value(self):
        try:
            from src.balanced_brackets import balanced_brackets
            val = balanced_brackets("()")
        except Exception as e:
            self.assertTrue(False, f"Function threw an error when it was called as follows:" + 
                f'\nbalanced_brackets("()")\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == bool, f"Function balanced_brackets should return a value, which is of type bool," +  
            f" now it returns a value {val} which is of type {taip}\n when it is called as follows\n" +  
            'balanced_brackets("()")')
        

    def test_3_is_recursive(self):
        from src.balanced_brackets import balanced_brackets
        self.assertTrue(reflect.test_recursion(balanced_brackets, "()"), 
            f'"Function balanced_brackets should call itself recursively.\n' + 
            f'Now calling balanced_brackets("()") does not lead to new calls of function balanced_brackets.')

    def test_4_test_with_values_1(self):
        from src.balanced_brackets import balanced_brackets
        test_cases = [("()",True), ("(Hello)", True), ("square[brackets]", True), ("([double])", True), 
            ("[first and (Second)]", True), ("(x * (1 + y) / 2)", True), ("((([first] + second) * third) - fourth)", True)]
        for test_case, corr in test_cases:
            val = balanced_brackets(test_case)
            self.assertEqual(val, corr, f'Function should return a value\n{corr}\n' + 
            f'when it is called with the parameter\n{test_case}\nnow function returns\n' + 
            f'{val}')

    
    def test_5_test_with_values_2(self):
        from src.balanced_brackets import balanced_brackets
        test_cases = [("((x)", False), ("x[[]",False), ("(x)y)", False), ("x[y]z]", False), ("(z]zz", False), ("x[xx)", False), 
            ("([brackets crossed)]", False), ("[brackets(crossed])", False)]
        for test_case, corr in test_cases:
            val = balanced_brackets(test_case)
            self.assertEqual(val, corr, f'Function should return a value\n{corr}\n' + 
            f'when it is called with the parameter\n{test_case}\nnow function returns\n' + 
            f'{val}')

if __name__ == '__main__':
    unittest.main()
