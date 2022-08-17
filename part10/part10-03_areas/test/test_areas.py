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

exercise = 'src.areas'

def f(attr: list):
    return "\n".join([str(x) for x in attr])

class AreatTest(unittest.TestCase):
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

    @points('10.areas')
    def test_0b_class_square_exists(self):
        try:
            from src.areas import Rectangle
            a = Rectangle(1,2)
        except Exception as e:
            self.fail(f'Calling constructor Rectangle(1,2) threw an error \n{e}\n' + 
            'Check that you have not changed the class Rectangle!')

    @points('10.areas')
    def test_1_class_square_exists(self):
        try:
            from src.areas import Square
            a = Square(1)
        except Exception as e:
            self.fail(f'Calling constructor Square(1) threw an error \n{e}\n' + 
            'Check that the class is defined.')

    @points('10.areas')
    def test_2_square_perinta(self):
        from src.areas import Rectangle, Square
        a = Square(1)
        self.assertTrue(isinstance(a, Rectangle), f"Class Square should " +
            'inherit class Rectangle!')

    @points('10.areas')
    def test_3_square_no_new_attributes(self):
        from src.areas import Rectangle, Square
        a = Square(1)
        b = Rectangle(1,2)
        ref = reflect.Reflect()
        ref.set_object(a)
        attr = ref.list_attributes(True)
        self.assertTrue(len(attr) == 3, f"You should not define new " +
            "attributes for class Square!")

    @points('10.areas')
    def test_4_square_str(self):
        from src.areas import Rectangle, Square
        test_cases = (1,2,4,6,8)
        for test_case in test_cases:
            square = Square(test_case)
            val = str(square)
            corr = f"square {test_case}x{test_case}"
            self.assertEqual(corr, val, f'Method __str__ should return ' + 
                f'\n{corr}\nNow it returns\n{val}\nwhen object was ' + 
                f'initialized as:\nSquare({test_case})')

    @points('10.areas')
    def test_5_square_area(self):
        from src.areas import Rectangle, Square
        test_cases = (1,2,4,6,8)
        for test_case in test_cases:
            square = Square(test_case)
            val = square.area()
            corr = test_case ** 2
            self.assertEqual(corr, val, f'Method area should return ' + 
                f'\n{corr}\nNow it returns\n{val}\nwhen object was ' + 
                f'initialized as:\nSquare({test_case})')

if __name__ == '__main__':
    unittest.main()
