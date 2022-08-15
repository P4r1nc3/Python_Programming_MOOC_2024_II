import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date, datetime, timedelta

exercise = 'src.code'

def f(attr: list):
    return ",".join(attr)

@points('8.item_suitcase_hold_part1')
class ItemTest(unittest.TestCase):
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

    def test1_item_exists(self):
        try:
            from src.code import Item
        except:
            self.assertTrue(False, "Your program should contain class named Item")

    def test2_item_constructor(self):
        try:
            from src.code import Item
            item = Item("ABC Book", 2)
        except Exception as e:
            self.assertTrue(False, 'Calling constructor of the class Item as follows Item("ABC Book", 2)' +
                f' threw an error: {e}\nMake sure, that the constructor is defined properly.')

    def test3_item_str(self):
        test_cases = [("ABC Book", 2), ("Hammer", 8), ("Bottle", 1)]
        for test_case in test_cases:
            from src.code import Item
            item = Item(test_case[0], test_case[1])

            corr = f'{test_case[0]} ({test_case[1]} kg)'
            val = str(item)

            self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwhen object is initialized as follows\n" + 
                f'Item("{test_case[0]}", {test_case[1]})\nNow method returns a string\n{val}')

    def test4_attributes_hidden(self):
        from src.code import Item
        code = """
item = Item("ABC Book", 2)
print(item.weight)
"""

        ok = False
        item = Item("ABC Book", 2)
        try:
            v = item.weight
        except Exception as e:
            ok = True
        
        if not ok:
            self.assertFalse(type(v) ==  type(2), f'Executing the following code\n{code}\n should not print out the weight of the item. The weight of the item should be encapsulated')
        
        code = """
item = Item("ABC Book", 2)
print(item.name)
"""

        ok = False
        item = Item("ABC Book", 2)
        try:
            v = item.name
        except Exception as e:
            ok = True
        
        if not ok:
            self.assertFalse(type(v) == type("LOL"), f'Executing the following code\n{code}\n should not print out the name of the item. The name of the product should be encapsulated')
         
    def test5_item_weight(self):
        try:
            from src.code import Item
            code = """
item = Item("ABC Book", 2)
item.weight()
"""

            item = Item("ABC Book", 2)
            p = item.weight()

        except Exception as e:
            self.assertTrue(False, f'Executing the following code\n{code}\n threw an error\n{e}\nIs the method weight(self) defined?')
                
        self.assertTrue(p == 2, f'When executing the following code\n{code}\n, method should return 2, but the return value was {p}')

    @points('8.item_suitcase_hold_part1')
    def test6_item_name(self):
        try:
            from src.code import Item
            code = """
item = Item("ABC Book", 2)
item.name()
"""

            item = Item("ABC Book", 2)
            p = item.name()

        except Exception as e:
            self.assertTrue(False, f'Executing the following code\n{code}\n threw an error\n{e}\nIs the method name(self) defined?')
                
        self.assertTrue(p == "ABC Book", f'When executing the following code\n{code}\n, method should return ABC Book, but the return value was {p}')

    def test7_item_weight_2(self):
        try:
            from src.code import Item
            code = """
item = Item("ABC Book", 5)
item.weight()
"""

            item = Item("ABC Book", 5)
            p = item.weight()

        except Exception as e:
            self.assertTrue(False, f'Executing the following code\n{code}\n threw an error\n{e}\nIs the method weight(self) defined?')
                
        self.assertTrue(p == 5, f'When executing the following code\n{code}\n, method should return 5, but the return value was {p}')

    @points('8.item_suitcase_hold_part1')
    def test7_item_name_2(self):
        try:
            from src.code import Item
            code = """
item = Item("Drilling machine", 2)
item.name()
"""

            item = Item("Drilling machine", 2)
            p = item.name()

        except Exception as e:
            self.assertTrue(False, f'Executing the following code\n{code}\n threw an error\n{e}\nIs the method name(self) defined?')
                
        self.assertTrue(p == "Drilling machine", f'When executing the following code\n{code}\n, method should return Drilling machine, but the return value was {p}')


if __name__ == '__main__':
    unittest.main()

