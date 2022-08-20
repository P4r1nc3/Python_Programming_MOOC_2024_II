import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re
import types
from random import choice, randint, shuffle

exercise = 'src.even_numbers'

def source_rows(function: callable):
    src = inspect.getsource(function)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('12.even_numbers')
class EvenNumbersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_ok(self):
        ok, line = check_source(self.module)
        message = """Code testing the functions must be located after the
if __name__ == "__main__":
block. The following line must be moved:
"""
        self.assertTrue(ok, message+line)
    
    def test_1_function_exists(self):
        try:
            from src.even_numbers import even_numbers
        except Exception as e:
            self.fail(f'Program should contain a function called even_numbers.')

    def test_2_return_type(self):
        try:
            from src.even_numbers import even_numbers
            val = even_numbers(2,4)
        except Exception as e:
            self.fail(f"Function threw an error when it was called like this:\n"  + 
            'even_numbers(2,4)\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) is types.GeneratorType, f"Function even numbers should return a generator," +  
            f" now it returns a value {val} which is of type {taip}\n when it is called with parameter\n" +  
            'even_numbers(2,4)')
        

    def test_3_test_with_values(self):
        from src.even_numbers import even_numbers
    
        test_cases = [(2,6), (4,11), (7,12), (20,22), (1,19)]
        for test_case in test_cases:
            func = f"even_numbers {test_case}"
            corr = [x for x in range(test_case[0] 
                if test_case[0] % 2 == 0 else test_case [0] + 1, 
                test_case[1] + 1 if test_case[1] % 2 == 0 else test_case[1], 2)]
            gen = even_numbers(test_case[0], test_case[1])
            val = [x for x in gen]

            self.assertEqual(val, corr, f'Generator should return values\n{corr}\n' + 
                f'when it was initialized like this:\n{func}\nnow it returns values\n' + 
                f'{val}')

    
if __name__ == '__main__':
    unittest.main()
