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

exercise = 'src.remaining_stock'

def source_rows(function: callable):
    src = inspect.getsource(function)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('12.remaining_stock')
class RemainingStockTest(unittest.TestCase):
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
            from src.remaining_stock import sort_by_remaining_stock
        except Exception as e:
            self.fail(f'The program should have a function called sort_by_remaining_stock.')

    def test_2_return_type(self):
        try:
            from src.remaining_stock import sort_by_remaining_stock
            val = sort_by_remaining_stock([("apple",1,1),("pineapple",2,2)])
        except Exception as e:
            self.fail(f"Function threw an error when called as\n"  + 
            f'sort_by_remaining_stock([("apple",1,1),("pineapple",2,2)]):\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Function sort_by_remaining_stock should return a value of type list," +  
            f" now it returns {val} which is of type {taip}\n when called as\n" +  
            'sort_by_remaining_stock([("apple",1,1),("pineapple",2,2)])')
        

    def test_3_test_with_values1(self):
        from src.remaining_stock import sort_by_remaining_stock
        test_case = [("apple",5,3), ("orange",10,2), ("pineapple",8,6), ("pear",11,5)]
        test_case_2 = test_case[:]
        corr = [("orange",10,2), ("apple",5,3), ("pear",11,5), ("pineapple",8,6)]
        val = sort_by_remaining_stock(test_case)

        self.assertEqual(val, corr, f'Function should return a list\n{corr}\n' + 
            f'when called as\n{test_case}\nnow the function returns\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Function cannot change the original list!\n" + 
            f'The list was\n{test_case_2}\nbut after the function call it is\n{test_case}.')

    def test_4_testaa_arvoilla2(self):
        from src.remaining_stock import sort_by_remaining_stock
        test_case = [("auto",5,13), ("mopo",10,12), ("vene",11,4), ("rullalauta",11,9), ("skootteri",11,10)]
        test_case_2 = test_case[:]
        corr = [("vene",11,4), ("rullalauta",11,9), ("skootteri",11,10), ("mopo",10,12), ("auto",5,13)]
        val = sort_by_remaining_stock(test_case)

        self.assertEqual(val, corr, f'Function should return a list\n{corr}\n' + 
            f'when called as\n{test_case}\nnow the function returns\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Function cannot change the original list!\n" + 
            f'The list was\n{test_case_2}\nbut after the function call it is\n{test_case}.')
    
if __name__ == '__main__':
    unittest.main()
