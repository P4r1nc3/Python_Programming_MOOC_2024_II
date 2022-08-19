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

exercise = 'src.ratings'

def source_rows(function: callable):
    src = inspect.getsource(function)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('12.ratings')
class RatingsTest(unittest.TestCase):
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
            from src.ratings import sort_by_ratings
        except Exception as e:
            self.fail(f'Your program should have a function called sort_by_ratings.')

    def test_2_return_type(self):
        try:
            from src.ratings import sort_by_ratings
            val = sort_by_ratings([{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, 
                { "name": "Friends", "rating" : 8.9, "seasons":10 }])
        except Exception as e:
            self.fail(f"Function threw an error when it was called as:\n"  + 
            'sort_by_ratings([{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 }]):\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Function sort_by_ratings should return a value of type list list," +  
            f" now it returns {val} which is of type {taip}\n when called as\n" +  
            'sort_by_ratings([{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 }])')
        

    def test_3_test_with_values1(self):
        from src.ratings import sort_by_ratings
    
        tdata = [("Dexter",8.8, 9), ("Simpsons",8.6,30), ("Friends",8.9,10), ("Oz",8.7,6)]
        test_case = [{"name":tc[0], "rating":tc[1], "seasons":tc[2]} for tc in tdata]
        test_case_2 = test_case[:]
        corr = sorted(test_case, key=lambda t:t["rating"], reverse=True)
        val = sort_by_ratings(test_case)

        self.assertEqual(val, corr, f'Function should return list\n{corr}\n' + 
            f'when called with parameter\n{test_case}\nNow the function returns\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Function cannot change the original list!\n" + 
            f'The list was\n{test_case_2}\nbut after the function call it is\n{test_case}.')

    def test_4_test_with_values1(self):
        from src.ratings import sort_by_ratings
    
        tdata = [("The Wire",9.3, 5), ("Game of Thrones",9.2,8), ("Band of Brothers",9.5,1), ("Sopranos",9.4,6), ("Sherlock",9.1,4)]
        test_case = [{"name":tc[0], "rating":tc[1], "seasons":tc[2]} for tc in tdata]
        test_case_2 = test_case[:]
        corr = sorted(test_case, key=lambda t:t["rating"], reverse=True)
        val = sort_by_ratings(test_case)

        self.assertEqual(val, corr, f'Function should return list\n{corr}\n' + 
            f'when called with parameter\n{test_case}\nNow the function returns\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Function cannot change the original list!\n" + 
            f'The list was\n{test_case_2}\nbut after the function call it is\n{test_case}.')

 
    
if __name__ == '__main__':
    unittest.main()
