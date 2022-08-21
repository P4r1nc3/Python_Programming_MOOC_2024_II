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

exercise = 'src.prime_numbers'

def source_rows(function: callable):
    src = inspect.getsource(function)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('12.prime_numbers')
class PrimeNumbersTest(unittest.TestCase):
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
            from src.prime_numbers import prime_numbers
        except Exception as e:
            self.fail(f'Your program should have a function called prime_numbers.')

    def test_2_return_type(self):
        try:
            from src.prime_numbers import prime_numbers
            val = prime_numbers()
        except Exception as e:
            self.fail(f"Function threw an error when called like this\n"  + 
            'prime_numbers()\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) is types.GeneratorType, f"Function prime_numbers should return a generator," +  
            f" now it returns {val} which is of type {taip}\n when it is called as\n" +  
            'prime_numbers()')
        

    def test_3_test_with_values1(self):
        from src.prime_numbers import prime_numbers
    
        test_cases = (1,3,4,7,9,12)
        al = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]
        for test_case in test_cases:
            corr = al[:test_case]
            gen = prime_numbers()
            val = [next(gen) for i in range(test_case)]

            self.assertEqual(val, corr, f'Generator should return values\n{corr}\n' + 
                f'when it is initialized as:\ngen = prime_numbers()\n' +
                f'and the function next(gen) is called {test_case} times\n' +
                f'Now it returns\n' + 
                f'{val}')

    
if __name__ == '__main__':
    unittest.main()
