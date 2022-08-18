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

exercise = 'src.products_in_shopping_list'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('11.products_in_shopping_list')
class ProductsInShoppingListTest(unittest.TestCase):
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
            from src.products_in_shopping_list import products_in_shopping_list
        except Exception as e:
            self.fail(f'Your program should contain function named products_in_shopping_list.')

    def test_2_paluuarvon_type_of_return_value(self):
        try:
            from src.products_in_shopping_list import products_in_shopping_list
            val = products_in_shopping_list([("apple",2)],1)
        except Exception as e:
            self.assertTrue(False, f"Function threw an error when it was called as follows:" + 
                f'\nproducts_in_shopping_list([("apple",2)],1)\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Function products_in_shopping_list is expected to return a value which is of type list," +  
            f" now it returns a value {val} which is of type {taip}\n when it is called as follows\n" +  
            'products_in_shopping_list([("apple",2)],1)')
        

    def test_3_length_of_function(self):
        from src.products_in_shopping_list import products_in_shopping_list
        lines = source_rows(products_in_shopping_list)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Function products_in_shopping_list must have at most' + 
            f' {max_lines} rows in this exercise.\n' +
            f'The function now has a total of {lines} rows (excluding empty rows and comments).')

    def test_4_test_with_values_1(self):
        test_case = [("Apple",10),("Orange",6),("Banana",8),("Pineapple",4),("Plum",9)]
        corr = ["Apple","Banana","Plum"]
        limit = 7
        from src.products_in_shopping_list import products_in_shopping_list
        val = products_in_shopping_list(test_case, limit)

        self.assertEqual(val, corr, f'The function is expected to return the following list:\n{corr}\n' +
            f'when it is called as follows:\n' + 
            f'products_in_shopping_list({test_case}, {limit})\n' +
            f'now function returns\n' + 
            f'{val}')

    def test_5_test_with_values_2(self):
        test_case = [("Chewing gum",5),("Chokolate",4),("Lollipop",5),("Chips",4)]
        corr = ["Chewing gum","Lollipop"]
        limit = 5
        from src.products_in_shopping_list import products_in_shopping_list
        val = products_in_shopping_list(test_case, limit)

        self.assertEqual(val, corr, f'The function is expected to return the following list:\n{corr}\n' +
            f'when it is called as follows:\n' + 
            f'products_in_shopping_list({test_case}, {limit})\n' +
            f'now function returns\n' + 
            f'{val}')

    def test_6_test_with_values_3(self):
        test_case = [("Notebook",12),("Pencil",14),("Sharpener",9),("Ruler",7)]
        corr = ["Pencil"]
        limit = 13
        from src.products_in_shopping_list import products_in_shopping_list
        val = products_in_shopping_list(test_case, limit)

        self.assertEqual(val, corr, f'The function is expected to return the following list:\n{corr}\n' +
            f'when it is called as follows:\n' + 
            f'products_in_shopping_list({test_case}, {limit})\n' +
            f'now function returns\n' + 
            f'{val}')

 
if __name__ == '__main__':
    unittest.main()
