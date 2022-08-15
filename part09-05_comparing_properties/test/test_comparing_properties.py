import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date

exercise = 'src.comparing_properties'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 


class ComparingPropertiesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected.")]):
           cls.module = load_module(exercise, 'en')

    @points('9.comparing_properties_part1')
    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    @points('9.comparing_properties_part1')
    def test_1_class_exists(self):
        try:
            from src.comparing_properties import RealProperty
            h = RealProperty(1,1,1)
        except Exception as e:
            self.fail(f'Calling constructor RealProperty(1,1,1) threw an error \n{e}\n' + 
            'Do not change the constructor of the class!')        

    @points('9.comparing_properties_part1')
    def test_2_is_it_bigger(self):
        from src.comparing_properties import RealProperty
        a1 = RealProperty(1,1,1)
        a2 = RealProperty(2,2,2)
        a1.bigger(a2)

        test_cases = [((1,24,2500), (2,48,3200)), ((2,43,4200), (1,52,3900)), 
                      ((3,67,3000), (3,69,3000)), ((4,100,5000), (4,99,5010))]
        for test_case in test_cases:
            d1,d2 = test_case
            a1 = RealProperty(d1[0],d1[1],d1[2])
            a2 = RealProperty(d2[0],d2[1],d2[2])

            val = a1.bigger(a2)
            corr = d1[1] > d2[1]

            self.assertEqual(val, corr, f'Method call RealProperty1.bigger(RealProperty2) should ' +
                f'return {corr}, when objects are initialized as follows:\n' +
                f'RealProperty1 = RealProperty({d1[0]},{d1[1]},{d1[2]})\n' + 
                f'RealProperty2 = RealProperty({d2[0]},{d2[1]},{d2[2]})\n' +
                f'Now method did return {val}.')
    
    @points('9.comparing_properties_part2')
    def test_3_price_difference(self):
        from src.comparing_properties import RealProperty
        a1 = RealProperty(1,1,1)
        a2 = RealProperty(2,2,2)
        a1.price_difference(a2)

        test_cases = [((1,24,2500), (2,48,3200)), ((2,43,4200), (1,32,3900)), 
                      ((3,67,3000), (3,69,3000)), ((4,100,5000), (4,99,5000))]
        for test_case in test_cases:
            d1,d2 = test_case
            a1 = RealProperty(d1[0],d1[1],d1[2])
            a2 = RealProperty(d2[0],d2[1],d2[2])

            val = a1.price_difference(a2)
            corr = abs((d1[1] * d1[2]) - (d2[1] * d2[2]))

            self.assertEqual(val, corr, f'Method call RealProperty1.price_difference(RealProperty2) should ' +
                f'return {corr}, when objects are initialized as follows:\n' +
                f'RealProperty1 = RealProperty({d1[0]},{d1[1]},{d1[2]})\n' + 
                f'RealProperty2 = RealProperty({d2[0]},{d2[1]},{d2[2]})\n' +
                f'Now method did return {val}.')

    @points('9.comparing_properties_part3')
    def test_4_is_it_more_expensive(self):
        from src.comparing_properties import RealProperty
        a1 = RealProperty(1,1,1)
        a2 = RealProperty(2,2,2)
        a1.more_expensive(a2)

        test_cases = [((1,24,2500), (2,48,3200)), ((2,43,4200), (1,32,3900)), 
                      ((3,67,3000), (3,69,3000)), ((4,100,5000), (4,99,5000))]
        for test_case in test_cases:
            d1,d2 = test_case
            a1 = RealProperty(d1[0],d1[1],d1[2])
            a2 = RealProperty(d2[0],d2[1],d2[2])

            val = a1.more_expensive(a2)
            corr = (d1[1] * d1[2]) > (d2[1] * d2[2])

            self.assertEqual(val, corr, f'Method call RealProperty1.more_expensive(RealProperty2) should ' +
                f'return {corr}, when objects are initialized as follows:\n' +
                f'RealProperty1 = RealProperty({d1[0]},{d1[1]},{d1[2]})\n' +
                f'RealProperty2 = RealProperty({d2[0]},{d2[1]},{d2[2]})\n' +
                f'Now method did return {val}.')

if __name__ == '__main__':
    unittest.main()
