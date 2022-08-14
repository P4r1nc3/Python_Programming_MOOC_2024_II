import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date
from src.shopping_list import ShoppingList

exercise = 'src.shopping_list'
function = "total_units"

def get_corr(l):
    return sum(l.amount(i) for i in range(1, l.number_of_items() + 1))

def gen(l: list):
    k = ShoppingList()
    for i in l:
        k.add(i[0],i[1])
    return k

def format(l: list):
    return "\n".join([f"{x[0]}: {x[1]} pcs." for x in l])

        

@points('8.shopping_list')
class ShoppingListTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_ok(self):
        ok, line = check_source(self.module)
        message = """All code testing the functions must be inside the
if __name__ == "__main__":
block. The following line must be moved:
"""
        self.assertTrue(ok, message+line)

    def test1_function_exists(self):
        try:
            from src.shopping_list import total_units
        except:
            self.fail("Your program must contain a function total_units(my_list: ShoppingList)")

    def test2_return_type(self):
        try:
            from src.shopping_list import total_units
            test_list = gen([("omena",1)])
            val = total_units(test_list)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == int, f"Function total_units should return an object of type int," +  
                f" now it returns {val} which is of type {taip}\nwhen it's called with a list with single item")
        except Exception as e:
            self.fail(f"Function threw an error when it was called with a list with single item:\n{e}")


    def test3_test_values(self):
        d = date
        test_cases = ([("apple",5),("orange",5)], [("apple",4),("orange",5),("banana",6)],
                      [("mouse", 2), ("hamster",8), ("gerbil", 6)], [("car",24),("moped",40),("motorcycle",10),("truck",5)], 
                      [("rose",100),("daffodil",90),("sunflower",80),("lilly",70),("daisy",60)])

        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
                reload_module(self.module)
                total_units = load(exercise, function, 'en')

                lista = gen(test_case)
               
                val = total_units(lista)
                corr = get_corr(lista)

                self.assertEqual(val, corr, f"Function should return {corr}\nbut instead it returns {val}\nwhen there are these products in the list: \n{format(test_case)}")
    

if __name__ == '__main__':
    unittest.main()
