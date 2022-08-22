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

exercise = 'src.regular_expressions'

def source_rows(function: callable):
    src = inspect.getsource(function)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)


class RegularExpressionsTest(unittest.TestCase):
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
    
    @points('12.regular_expressions_part1')
    def test_2a_function_exists(self):
        try:
            from src.regular_expressions import is_dotw
        except Exception as e:
            self.fail(f'Your program should contain a function is_dotw.')

    @points('12.regular_expressions_part1')
    def test_2b_return_type(self):
        try:
            from src.regular_expressions import is_dotw
            val = is_dotw("Mon")
        except Exception as e:
            self.fail(f"Function threw an error when it was called like this:\n"  + 
            'is_dotw("Mon")\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == bool, f"Function is_dotw should return a value of type bool," +  
            f" now it returns{val} which is of type {taip}\n when it was called as\n" +  
            'is_dotw("Mon")')
        
    @points('12.regular_expressions_part1')
    def test_2c_test_with_values(self):
        from src.regular_expressions import is_dotw
        test_cases = "Mon Tue Wed Thu Fri Sat Sun noM euT ab lauantai Mnonday Mo Tu Po My".split()
        for test_case in test_cases:
            corr = test_case in "Mon Tue Wed Thu Fri Sat Sun".split()
            val = is_dotw(test_case)

            self.assertEqual(val, corr, f'Function is_dotw should return {corr}\n' + 
                f'when it was called as\n{test_case}\nNow the function returns\n' + 
                f'{val}')

    @points('12.regular_expressions_part2')
    def test_3a_function_exists(self):
        try:
            from src.regular_expressions import all_vowels
        except Exception as e:
            self.fail(f'Your program should contain a function all_vowels.')

    @points('12.regular_expressions_part2')
    def test_3b_return_type(self):
        try:
            from src.regular_expressions import all_vowels
            val = all_vowels("aa")
        except Exception as e:
            self.fail(f"Function all_vowels threw an error when it was called as:\n"  + 
            'all_vowels("aa")\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == bool, f"Function all_vowels should return a value of type bool," +  
            f" now it returns{val} which is of type {taip}\n when it was called as\n" +  
            'all_vowels("aa")')
        
    @points('12.regular_expressions_part2')
    def test_3c_test_with_values(self):
        from src.regular_expressions import all_vowels
        test_cases = "aaa eee iii oo uu yy aeee ioioi aioioä oyoyuaå aab aec ooooaeoip aaaaabo".split()
        for test_case in test_cases:
            corr = len([x for x in test_case if x not in "aeiouy"]) == 0
            val = all_vowels(test_case)

            self.assertEqual(val, corr, f'Function all_vowels should return {corr}\n' + 
                f'when it was called as\n{test_case}\nNow the function returns\n' + 
                f'{val}')

    @points('12.regular_expressions_part3')
    def test_4a_function_exists(self):
        try:
            from src.regular_expressions import time_of_day
        except Exception as e:
            self.fail(f'Your program should contain a function time_of_day.')

    @points('12.regular_expressions_part3')
    def test_4b_return_type(self):
        try:
            from src.regular_expressions import time_of_day
            val = time_of_day("11:11:11")
        except Exception as e:
            self.fail(f"Function time_of_day threw an error when it was called as:\n"  + 
            'time_of_day("11:11:11")\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == bool, f"Function time_of_day should return a value of type bool," +  
            f" now it returns{val} which is of type {taip}\n when it was called as\n" +  
            'time_of_day("11:11:11")')
        
    @points('12.regular_expressions_part3')
    def test_4c_test_with_values(self):
        from src.regular_expressions import time_of_day
        test_cases = ("12:12:12 16:34:56 23:55:59 19:00:00 20:10:30 " + 
            "ab:20:20 23:15:xx 19:zz:04 " + 
            "25:13:01 39:23:20 11:66:03 17:34:87").split()
        cor = (True,True,True,True,True,False,False,False,False,False,False,False)
        for test_case,corr in zip(test_cases,cor):
            val = time_of_day(test_case)

            self.assertEqual(val, corr, f'Function time_of_day should return {corr}\n' + 
                f'when it was called as\n{test_case}\nNow the function returns\n' + 
                f'{val}')

    
if __name__ == '__main__':
    unittest.main()
