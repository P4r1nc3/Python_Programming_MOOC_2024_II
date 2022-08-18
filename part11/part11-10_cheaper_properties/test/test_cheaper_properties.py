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

exercise = 'src.cheaper_properties'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

def f(tuples: list):
    return "\n".join(f'{real_property[0].description}, {real_property[0].square_meters} square meters, price per sqm {real_property[0].price_per_sqm}, price difference {real_property[1]}' for real_property in tuples)

def f2(real_properties: list):
    return "\n".join(f'{real_property.description}, {real_property.square_meters} square meters, price per sqm {real_property.price_per_sqm}' for real_property in real_properties)

@points('11.cheaper_properties')
class CheaperPropertiesTest(unittest.TestCase):
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
            from src.cheaper_properties import cheaper_properties
        except Exception as e:
            self.fail(f'Your program should contain function named cheaper_properties.')

    def test_1b_class_exists(self):
        try:
            from src.cheaper_properties import RealProperty
        except Exception as e:
            self.fail(f'Class RealProperty is not found - make sure, that you have not changed definition of the class RealProperty')

    def test_2_type_of_return_value_1(self):
        try:
            from src.cheaper_properties import cheaper_properties, RealProperty
            val = cheaper_properties([RealProperty(1,1,1,"a")], RealProperty(1,1,2,"b"))
        except Exception as e:
            self.assertTrue(False, f"Function cheaper_properties threw an error when it was called as follows:" + 
                f'\ncheaper_properties([RealProperty(1,1,1,"a")], RealProperty(1,1,2,"b"))\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Function cheaper_properties is expected to return a value which is of type list," +  
            f" now it returnsa value {val} which is of type {taip}\n  when it is called like this:\n" +  
            'cheaper_properties([RealProperty(1,1,1,"a")], RealProperty(1,1,2,"b"))')

    def test_2b_type_of_return_value_2(self):
        from src.cheaper_properties import cheaper_properties, RealProperty
        val = cheaper_properties([RealProperty(1,1,1,"a")], RealProperty(1,1,2,"b"))
        
        self.assertTrue(len(val) > 0, f"Function cheaper_properties returned an empty list when it was called as follows:" + 
            f'\ncheaper_properties([RealProperty(1,1,1,"a")], RealProperty(1,1,2,"b"))')
        
        taip = str(type(val[0])).replace("<class '","").replace("'>","")
        self.assertTrue(type(val[0]) == tuple, f"Function cheaper_properties is expected to return items of type tuple," +  
            f" now it returnsa value {val[0]} which is of type {taip}\n  when it is called like this:\n" +  
            'cheaper_properties([RealProperty(1,1,1,"a")], RealProperty(1,1,2,"b"))')

        taip = str(type(val[0][0])).replace("<class '","").replace("'>","")
        self.assertTrue(type(val[0][0]) == RealProperty, f"Function cheaper_properties is expected to return a list which contains tuples, " + 
            f"whose first item is of type RealProperty.\n" +  
            f"Now it returned a value {val[0][0]} which is of type {taip}\n  when it is called like this:\n" +  
            'cheaper_properties([RealProperty(1,1,1,"a")], RealProperty(1,1,2,"b"))')
        

    def test_3_length_of_function(self):
        from src.cheaper_properties import cheaper_properties
        lines = source_rows(cheaper_properties)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Function cheaper_propertiesmust have at most'+ 
            f' {max_lines} rows in this exercise.\n' +
            f'The function now has a total of {lines} rows (excluding empty rows and comments).')

    def test_4_test_with_values_1(self):
        from src.cheaper_properties import cheaper_properties, RealProperty
        a1 = RealProperty(1, 16, 5500, "Central studio")
        a2 = RealProperty(2, 38, 4200, "Two bedrooms downtown")
        a3 = RealProperty(3, 78, 2500, "Three bedrooms in the suburbs")
        a4 = RealProperty(6, 215, 500, "Farm in the middle of nowhere")
        a5 = RealProperty(4, 105, 1700, "Loft in a small town")
        a6 = RealProperty(25, 1200, 2500, "Countryside mansion")
        test_case = [a1, a2, a3, a4, a5, a6]

        limit = a3

        val = cheaper_properties(test_case, limit)
        corr = [(a1, 107000), (a2, 35400), (a4, 87500), (a5, 16500)]

        self.assertEqual(val, corr, f'Function is expected to return following properties\n{f(corr)}\n' + 
            f'when following properties were given as paramaters:\n' + 
            f'{f2(test_case)}\n' +
            f'and property compared to was\n' +
            f'{limit}\n'
            f'now function returns following properties\n' + 
            f'{f(val)}')

    def test_5_test_with_values_2(self):
        from src.cheaper_properties import cheaper_properties, RealProperty
        a1 = RealProperty(1, 16, 5500, "Central studio")
        a2 = RealProperty(2, 38, 4200, "Two bedrooms downtown")
        a3 = RealProperty(3, 78, 2500, "Three bedrooms in the suburbs")
        a4 = RealProperty(6, 215, 500, "Farm in the middle of nowhere")
        a5 = RealProperty(4, 105, 1700, "Loft in a small town")
        a6 = RealProperty(25, 1200, 2500, "Countryside mansion")
        test_case = [a1, a2, a3, a4, a5, a6]

        limit = a4

        val = cheaper_properties(test_case, limit)
        corr = [(a1, 107500 - 88000)]

        self.assertEqual(val, corr, f'Function is expected to return following properties\n{f(corr)}\n' + 
            f'when following properties were given as paramaters:\n' + 
            f'{f2(test_case)}\n' +
            f'and property compared to was\n' +
            f'{limit}\n'
            f'now function returns following properties\n' + 
            f'{f(val)}')

if __name__ == '__main__':
    unittest.main()
