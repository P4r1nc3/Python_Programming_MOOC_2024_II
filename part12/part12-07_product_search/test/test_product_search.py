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

exercise = 'src.product_search'

def source_rows(function: callable):
    src = inspect.getsource(function)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('12.product_search')
class ProductSearchTest(unittest.TestCase):
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
            from src.product_search import search
        except Exception as e:
            self.fail(f'Program should contain a function called search.')

    def test_2_return_type(self):
        try:
            from src.product_search import search
            val = search([("Apple",1,1)], lambda x : True)
        except Exception as e:
            self.fail(f"Function threw an error when it was called like this:\n"  + 
            'search([("Apple",1,1)], lambda x : True)\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Function search should return a value of type list," +  
            f" now it returns a value {val} which is of type {taip}\n when it is called with parameter\n" +  
            'search([("Apple",1,1)], lambda x : True)')
        

    def test_3_test_with_values1(self):
        from src.product_search import search
    
        test_case = [("Apple",4.0,3), ("Orange",5.95, 5), ("Banana",2.95,10), ("Pineapple", 5.50, 3)]
        test_case_2 = test_case[:]
        func = "lambda product: product[1] >= 5"
        corr = [("Orange",5.95, 5),("Pineapple", 5.50, 3)]
        val = search(test_case, lambda t: t[1] > 5)

        self.assertEqual(val, corr, f'Function should return a list\n{corr}\n' + 
            f'when it is called with a list\n{test_case}\nand with a function\n{func}\nnow function returns\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Function cannot change the original list!\n" + 
            f'The list was\n{test_case_2}\nNow it isn\n{test_case}.')

    def test_4_test_with_values2(self):
        from src.product_search import search
    
        test_case = [("Apple",4.0,3), ("Orange",5.95, 5), ("Banana",2.95,10), ("Pineapple", 5.50, 3), 
            ("Pear",6.95,2), ("Grapefruit",3.95,4)]
        test_case_2 = test_case[:]
        func = "lambda product: product[0].startwith('P')"
        corr = [("Pineapple", 5.50, 3),("Pear",6.95,2)]
        val = search(test_case, lambda t: t[0].startswith("P"))

        self.assertEqual(val, corr, f'Function should return a list\n{corr}\n' + 
            f'when it is called with a list\n{test_case}\nand with a function\n{func}\nnow function returns\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Function cannot change the original list!\n" + 
            f'The list was\n{test_case_2}\nNow it isn\n{test_case}.')

    def test_5_test_with_values3(self):
        from src.product_search import search
    
        test_case = [("Apple",4.0,3), ("Orange",5.95, 5), ("Banana",2.95,10), ("Pineapple", 5.50, 3), 
            ("Pear",6.95,2), ("Grapefruit",3.95,4)]
        test_case_2 = test_case[:]
        func = "lambda product: product[2] < 5"
        corr = [("Apple",4.0,3), ("Pineapple", 5.50, 3), 
            ("Pear",6.95,2), ("Grapefruit",3.95,4)]
        val = search(test_case, lambda t: t[2] < 5)

        self.assertEqual(val, corr, f'Function should return a list\n{corr}\n' + 
            f'when it is called with a list\n{test_case}\nand with a function\n{func}\nnow function returns\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Function cannot change the original list!\n" + 
            f'The list was\n{test_case_2}\nNow it isn\n{test_case}.')    

 
    
if __name__ == '__main__':
    unittest.main()
