import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re
from random import choice, randint, shuffle

exercise = 'src.remove_smaller_than'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('11.remove_smaller_than')
class RemoveSmallerThanTest(unittest.TestCase):
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
            from src.remove_smaller_than import remove_smaller_than
        except Exception as e:
            self.fail(f'Your program should contain function named remove_smaller_than.')

    def test_2_type_of_return_value(self):
        try:
            from src.remove_smaller_than import remove_smaller_than
            val = remove_smaller_than([1,3],2)
        except Exception as e:
            self.assertTrue(False, f"Function threw an error when it was called as follows:" + 
                f"\nremove_smaller_than([1,3],2):\n{e}")
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Function remove_smaller_than is expected to return a value which is of type list," +  
            f" now it returns a value {val} which is of type {taip}\n when it is called with the parameter " +
            "remove_smaller_than([1,3],2)")
        

    def test_3_length_of_function(self):
        from src.remove_smaller_than import remove_smaller_than
        lines = source_rows(remove_smaller_than)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Function remove_smaller_than must have at most'+ 
            f' {max_lines} rows in this exercise.\n' +
            f'The function now has a total of {lines} rows (excluding empty rows and comments).')

    def test_4_test_with_values_1(self):
        test_case = ([1,2,3,4,5,6,7],4)
        corr = [4,5,6,7]
        from src.remove_smaller_than import remove_smaller_than
        val = remove_smaller_than(test_case[0], test_case[1])

        self.assertEqual(val, corr, f'The function is expected to return the following list:\n{corr}\n' +
            f'when it is called with the parameter {test_case}\nnow the function returns\n' +
            f'{val}')

    def test_5_test_with_values_2(self):
        test_case = ([100,101,102,105,106,103,99,98,107],105)
        corr = [105,106,107]
        from src.remove_smaller_than import remove_smaller_than
        val = remove_smaller_than(test_case[0], test_case[1])

        self.assertEqual(val, corr, f'The function is expected to return the following list:\n{corr}\n' +
            f'when it is called with the parameter {test_case}\nnow the function returns\n' +
            f'{val}')

    def test_6_test_with_values_3(self):
        test_case = ([-5,-3,-10,-15,-16,-11,-12,-8],-12)
        corr = [-5,-3,-10,-11,-12,-8]
        from src.remove_smaller_than import remove_smaller_than
        val = remove_smaller_than(test_case[0], test_case[1])

        self.assertEqual(val, corr, f'The function is expected to return the following list:\n{corr}\n' +
            f'when it is called with the parameter {test_case}\nnow the function returns\n' +
            f'{val}')

if __name__ == '__main__':
    unittest.main()