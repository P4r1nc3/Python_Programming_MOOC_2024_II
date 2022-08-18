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

exercise = 'src.most_common_words'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('11.most_common_words')
class MostCommonWordsTest(unittest.TestCase):
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
            from src.most_common_words import most_common_words
        except Exception as e:
            self.fail(f'Your program should contain function named most_common_words.')

    def test_2_type_of_return_value(self):
        try:
            from src.most_common_words import most_common_words
            val = most_common_words("comprehensions.txt", 3)
        except Exception as e:
            self.assertTrue(False, f"Function threw an error when it was called as follows:" + 
                f'\nmost_common_words("comprehensions.txt", 3)\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == dict, f"Function most_common_words is expected to return a value, which is of type dict," +  
            f" now it returns a value {val} which is of type {taip}\n when it is called as follows\n" +  
            'most_common_words("comprehensions.txt", 3))')


    def test_3_test_file_1(self):
        fname = "comprehensions.txt"
        from src.most_common_words import most_common_words
        limit = 3
        val = most_common_words(fname, limit)
        corr = {'comprehension': 4, 'is': 3, 'and': 3, 'for': 3, 'list': 4, 'in': 3}

        self.assertEqual(val, corr, f'Function should return a dict\n' + 
            f'{corr}\nwhen reading file {fname} and the limit {limit}.\n' + 
            f'Now function returns a dictionary\n{val}')

    def test_4_test_file_2(self):
        fname = "programming.txt"
        from src.most_common_words import most_common_words
        limit = 6
        val = most_common_words(fname, limit)
        corr = {'and': 7, 'of': 6, 'programming': 9}

        self.assertEqual(val, corr, f'Function should return a dict\n' + 
            f'{corr}\nwhen reading file {fname} and the limit {limit}.\n' + 
            f'Now function returns a dictionary\n{val}')

    def test_5_test_file_3(self):
        fname = "comprehensions.txt"
        from src.most_common_words import most_common_words
        limit = 4
        val = most_common_words(fname, limit)
        corr = {'comprehension': 4, 'list': 4}

        self.assertEqual(val, corr, f'Function should return a dict\n' + 
            f'{corr}\nwhen reading file {fname} and the limit {limit}.\n' + 
            f'Now function returns a dictionary\n{val}')

    def test_6_test_file_4(self):
        fname = "programming.txt"
        from src.most_common_words import most_common_words
        limit = 4
        val = most_common_words(fname, limit)
        corr = {'is': 5, 'and': 7, 'the': 5, 'of': 6, 'in': 4, 'programming': 9, 'languages': 5}
        
        self.assertEqual(val, corr, f'Function should return a dict\n' + 
            f'{corr}\nwhen reading file {fname} and the limit {limit}.\n' + 
            f'Now function returns a dictionary\n{val}')

if __name__ == '__main__':
    unittest.main()
