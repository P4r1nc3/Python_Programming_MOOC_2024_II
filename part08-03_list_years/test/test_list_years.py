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

exercise = 'src.list_years'
function = "list_years"

def get_corr(m):
    return sorted([x.year for x in m])
        

@points('8.list_years')
class ListYearsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input wasn't expected")]):
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
            from src.list_years import list_years
        except:
            self.fail("Your program must contain a function list_years(years: list)")

    def test2_return_type(self):
        try:
            from src.list_years import list_years
            val = list_years([date(1900,1,1)])
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == list, f"Function list_years should return a value of type list," +  
                f"now it returns {val} which is of type {taip}\n when it's called with arguments \n[date(1900,1,1)]")
        except Exception as e:
            self.fail(f"Function threw an error when called with arguments [date(1900,1,1)]")


    def test3_test_values(self):
        d = date
        test_cases = ([d(1900,1,1), d(1950,2,3), d(1979,6,6)], [d(2010,5,11),d(2009,11,1),d(2004,3,3),d(2000,1,23)],
                      [d(1976,8,8), d(1984,12,24), d(1979,2,4), d(1980,9,3)], [d(1763,2,7),d(1454,11,11),d(1133,2,23),d(1755,4,22)])
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Input wasn't expected")]):
                reload_module(self.module)
                list_years = load(exercise, function, 'en')

                test_case_2 = test_case[:]
               
                val = list_years(test_case)
                
                corr = get_corr(test_case_2)

                self.assertEqual(val, corr, f"Function should return \n{corr}\nbut it returns \n{val}\nwhen argument is\n{test_case_2}")
                self.assertEqual(test_case, test_case_2, f"Function should not change the list\nList is now \n{test_case}, \nbut it should be \n{test_case_2}")

    

if __name__ == '__main__':
    unittest.main()
