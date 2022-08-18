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

exercise = 'src.add_numbers_to_list'

@points('11.add_numbers_to_list')
class AddNumbersToListTest(unittest.TestCase):
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
            from src.add_numbers_to_list import add_numbers_to_list
        except Exception as e:
            self.fail(f'Your program should contain function named add_numbers_to_list.')

    def test_2_type_of_return_value(self):
        try:
            from src.add_numbers_to_list import add_numbers_to_list
            val = add_numbers_to_list([1,2,3,4])
        except Exception as e:
            self.assertTrue(False, f"Function threw an error when it was called as follows:" + 
                f'\nadd_numbers_to_list([1,2,3,4])\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(val == None, f"Function add_numbers_to_list should not return anything," +  
            f" now it returns a value {val} which is of type {taip}\n when it is called as follows\n" +  
            'add_numbers_to_list([1,2,3,4])')
        

    def test_3_is_recursive(self):
        from src.add_numbers_to_list import add_numbers_to_list
        self.assertTrue(reflect.test_recursion(add_numbers_to_list, [1,2]), 
            f'"Function add_numbers_to_list should call itself recursively.\n' + 
            f'Now calling add_numbers_to_list([1,2]) does not lead to new calls of function add_numbers_to_list.')

    def test_4_test_with_values_1(self):
        test_case = [1,2,3]
        val= test_case[:]
        corr = [1,2,3,4,5]

        from src.add_numbers_to_list import add_numbers_to_list
        add_numbers_to_list(val)

        self.assertEqual(val, corr, f'Content of the list should be \n{corr}\n' + 
            f'when function is called with the parameter\n{test_case}\nnow content of the list is\n' + 
            f'{val}')

    def test_5_test_with_values_2(self):
        test_case = [1,3,5,7,9,11]
        val= test_case[:]
        corr = [1,3,5,7,9,11,12,13,14,15]

        from src.add_numbers_to_list import add_numbers_to_list
        add_numbers_to_list(val)

        self.assertEqual(val, corr, f'Content of the list should be \n{corr}\n' + 
            f'when function is called with the parameter\n{test_case}\nnow content of the list is\n' + 
            f'{val}')

    def test_6_test_with_values_3(self):
        test_case = [10,20,30,40,50,60,70,80,90,100,110]
        val= test_case[:]
        corr = [10,20,30,40,50,60,70,80,90,100,110,111,112,113,114]

        from src.add_numbers_to_list import add_numbers_to_list
        add_numbers_to_list(val)

        self.assertEqual(val, corr, f'Content of the list should be \n{corr}\n' + 
            f'when function is called with the parameter\n{test_case}\nnow content of the list is\n' + 
            f'{val}')

    def test_7_test_with_values_4(self):
        test_case = [1,2,3,4,5]
        val= test_case[:]
        corr = [1,2,3,4,5]

        from src.add_numbers_to_list import add_numbers_to_list
        add_numbers_to_list(val)

        self.assertEqual(val, corr, f'Content of the list should be \n{corr}\n' + 
            f'when function is called with the parameter\n{test_case}\nnow content of the list is\n' + 
            f'{val}')
    
if __name__ == '__main__':
    unittest.main()
