import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint, shuffle
from datetime import date

exercise = 'src.iterable_shopping_list'

def f(attr: list):
    return "\n".join([str(x) for x in attr]) 

@points('10.iterable_shopping_list')
class ShoppingListTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
           cls.module = load_module(exercise, 'en')

    
    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)
    
    def test_1_class_exists(self):
        try:
            from src.iterable_shopping_list import ShoppingList
            a = ShoppingList()
        except Exception as e:
            self.fail(f'Calling constructor ShoppingList() threw an error \n{e}\n' + 
            'Check that an object can be created!')

    def test_2_methods_exist(self):
        from src.iterable_shopping_list import ShoppingList
        ref = reflect.Reflect()
        slist = ShoppingList()
        ref.set_object(slist)

        if not ref.has_attribute("__getitem__"):    
            self.assertTrue(ref.has_attribute("__iter__"), f'Class ShoppingList ' + 
                'must have method __iter__ for iteration to work.')

            self.assertTrue(ref.has_attribute("__next__"), f'Class ShoppingList ' + 
                'must have method __next__ for iteration to work.')

    def test_3_iteration(self):
        from src.iterable_shopping_list import ShoppingList
        test_cases = [("Eggs",10), ("Milk", 2), ("Apples", 5)]
        slist = ShoppingList()
        for test_case in test_cases:
            slist.add(test_case[0], test_case[1])

        val = []
        for product in slist:
            val.append(product)

        self.assertEqual(test_cases, val, f'Iterating ShopList object should ' +
            f'return the next items in order:\n{f(test_cases)}\n' + 
            f'Now the iteration returns:\n{f(val)}')

    def test_4_iteration2(self):
        from src.iterable_shopping_list import ShoppingList
        test_cases = [("Cucumber",1), ("Tomatos", 12), 
            ("Cabbage", 2), ("Candy", 100)]
        slist = ShoppingList()
        for test_case in test_cases:
            slist.add(test_case[0], test_case[1])

        val = []
        for product in slist:
            val.append(product)

        self.assertEqual(test_cases, val, f'Iterating ShopList object should ' +
            f'return the next items in order:\n{f(test_cases)}\n' + 
            f'Now the iteration returns:\n{f(val)}')
    
if __name__ == '__main__':
    unittest.main()
