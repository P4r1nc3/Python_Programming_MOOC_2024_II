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

exercise = 'src.filter_forbidden'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('11.filter_forbidden')
class FilterForbiddenTest(unittest.TestCase):
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
            from src.filter_forbidden import filter_forbidden
        except Exception as e:
            self.fail(f'Your program should contain function named filter_forbidden.')

    def test_2_type_of_return_value(self):
        try:
            from src.filter_forbidden import filter_forbidden
            val = filter_forbidden("abc","a")
        except Exception as e:
            self.assertTrue(False, f"Function threw an error when it was called as follows:" + 
                f'\nfilter_forbidden("abc","a")\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == str, f"Function filter_forbidden is expected to return a value which is of type str," +  
            f" now it returns a value {val} which is of type {taip}\n when it is called as follows\n" +  
            'filter_forbidden("abc","a")')
        

    def test_3_length_of_function(self):
        from src.filter_forbidden import filter_forbidden
        lines = source_rows(filter_forbidden)
        max_lines = 3
        self.assertTrue(lines <= max_lines, f'Function filter_forbidden must have at most'+ 
            f' {max_lines} rows in this exercise.\n' +
            f'The function now has a total of {lines} rows (excluding empty rows and comments).')

    def test_4_test_with_values_1(self):
        test_case = ("abcdefg", "bde")
        corr = "acfg"
        from src.filter_forbidden import filter_forbidden
        val = filter_forbidden(test_case[0], test_case[1])

        self.assertEqual(val, corr, f'The function is expected to return the following string\n{corr}\n' + 
            f'when it is called with the parameters {test_case}\nnow the function returns\n' + 
            f'{val}')

    
    def test_5_test_with_values_2(self):
        test_case = ("sheila sells seashells, she sells seashells by the seashore.", "sh")
        corr = "eila ell eaell, e ell eaell by te eaore."
        from src.filter_forbidden import filter_forbidden
        val = filter_forbidden(test_case[0], test_case[1])

        self.assertEqual(val, corr, f'The function is expected to return the following string\n{corr}\n' + 
            f'when it is called with the parameters {test_case}\nnow the function returns\n' + 
            f'{val}')

    def test_6_test_with_values_3(self):
        test_case = ("Sizzling sausages in a silver copper pan. Save six thin sausages for Saturday.", "zgiltpx")
        corr = "Sn sausaes n a sver coer an. Save s hn sausaes for Saurday."
        from src.filter_forbidden import filter_forbidden
        val = filter_forbidden(test_case[0], test_case[1])

        self.assertEqual(val, corr, f'The function is expected to return the following string\n{corr}\n' + 
            f'when it is called with the parameters {test_case}\nnow the function returns\n' + 
            f'{val}')
    
if __name__ == '__main__':
    unittest.main()
