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

exercise = 'src.lengths_of_strings'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('11.lengths_of_strings')
class LengthsOfStringsTest(unittest.TestCase):
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
            from src.lengths_of_strings import lengths
        except Exception as e:
            self.fail(f'Your function should contain function named lengths.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.lengths_of_strings import lengths
            val = lengths(["a"])
        except Exception as e:
            self.assertTrue(False, f"Function antoi thew an error when it was called as follows:" + 
                f'\nlengths(["a"])\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == dict, f"Function lengths is expected to return a value, which is of type dict," +  
            f" now it returns a value {val} whicxh is of type {taip}\n when it is called as follows\n" +  
            'lengths(["a"])')
        

    def test_3_length_of_function(self):
        from src.lengths_of_strings import lengths
        lines = source_rows(lengths)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Function lengths must have at most'+ 
            f' {max_lines} rows in this exercise.\n' +
            f'The function now has a total of {lines} rows (excluding empty rows and comments)')

    def test_4_test_with_values_1(self):
        test_case = ["first","second","third"]
        corr = {"first": 5, "second": 6, "third": 5}
        from src.lengths_of_strings import lengths
        val = lengths(test_case)

        self.assertEqual(val, corr, f'Function is expected to return a dictionary\n{corr}\n' + 
            f'when it is called with the parameters\n{test_case}\now function returns\n' + 
            f'{val}')

    def test_5_test_with_values_2(self):
        test_case = ["dog","cat","guinea pig","hamster","gerbil","goldfish"]
        corr = {"dog":3, "cat":3, "guinea pig":10, "hamster":7, "gerbil":6, "goldfish":8}
        from src.lengths_of_strings import lengths
        val = lengths(test_case)

        self.assertEqual(val, corr, f'Function is expected to return a dictionary\n{corr}\n' + 
            f'when it is called with the parameters\n{test_case}\now function returns\n' + 
            f'{val}')

    def test_6_test_with_values_3(self):
        test_case = ["commodore", "atari", "amstrad", "msx", "spectrum"]
        corr = {'commodore': 9, 'atari': 5, 'amstrad': 7, 'msx': 3, 'spectrum': 8}
        from src.lengths_of_strings import lengths
        val = lengths(test_case)

        self.assertEqual(val, corr, f'Function is expected to return a dictionary\n{corr}\n' + 
            f'when it is called with the parameters\n{test_case}\now function returns\n' + 
            f'{val}')

    




    

   

    








    
if __name__ == '__main__':
    unittest.main()
