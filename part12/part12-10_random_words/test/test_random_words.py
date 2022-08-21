import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re
import types
from random import choice, randint, shuffle

exercise = 'src.random_words'

def source_rows(function: callable):
    src = inspect.getsource(function)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('12.random_words')
class RandomWordsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_ok(self):
        ok, line = check_source(self.module)
        message = """Code testing the functions must be located after the
if __name__ == "__main__":
block. The following line must be moved:
"""
        self.assertTrue(ok, message+line)
    
    def test_1_function_exists(self):
        try:
            from src.random_words import word_generator
        except Exception as e:
            self.fail(f'Program should have a function called word_generator.')

    def test_2_return_type(self):
        try:
            from src.random_words import word_generator
            val = word_generator("abc",2,1)
        except Exception as e:
            self.fail(f"Function threw an error when it was called like this:\n"  + 
            'word_generator("abc",2,1)\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) is types.GeneratorType, f"Function word generator should return a generator," +  
            f" now it returns {val} which is of type {taip}\nwhen it is called as\n" +  
            'word_generator("abc",2,1)')
        

    def test_3_test_word_count(self):
        from src.random_words import word_generator
    
        test_cases = [("abc",2,3), ("ABCabcDEF",5,10), ("XYZ123456", 4, 7)]
        for test_case in test_cases:
            func = f"random_words{test_case}"
            corr = test_case[2]
            gen = word_generator(test_case[0], test_case[1], test_case[2])
            val = [i for i in gen]

            self.assertEqual(len(val), corr, f'Generator should return {corr} values\n' + 
                f'when it is initialized like this:\ngen = {func}\n' +
                f'now it returns values\n' + 
                f'{val}')

    def test_4_test_different_words(self):
        from src.random_words import word_generator
    
        test_cases = [("abcdefghijklmnopqrstuvwxyz",3,2), ("ABCabcDEFdefGHIghi",5,3), ("XYZ123456xyz789", 4, 4)]
        for test_case in test_cases:
            func = f"random_words{test_case}"
            gen = word_generator(test_case[0], test_case[1], test_case[2])
            val = [i for i in gen]
            corr = len(set(val)) != 1

            self.assertTrue(corr, f'Generator should return {corr} different values\n' + 
                f'when it is initialized like this:\ngen = {func}\n' +
                f'now it returns values\n' + 
                f'{val}')

    def test_5_test_right_letters(self):
        from src.random_words import word_generator
    
        test_cases = [("abcdefg",3,2), ("ABCabcDEFdef",5,3), ("XYZ1234", 4, 4)]
        for test_case in test_cases:
            func = f"random_words{test_case}"
            gen = word_generator(test_case[0], test_case[1], test_case[2])
            val = [i for i in gen]
            c = [[x for x in s if x not in test_case[0]] for s in val]
            corr = reduce(lambda x,y : True and len(y) == 0, c)

            self.assertTrue(corr, f'Words returned by generator should ' + 
                f'only contain letters from a string {test_case[0]}\n' +
                f'when it is initialized like this:\ngen = {func}\n' +
                f'now it returns values\n' + 
                f'{val}')



    
if __name__ == '__main__':
    unittest.main()
