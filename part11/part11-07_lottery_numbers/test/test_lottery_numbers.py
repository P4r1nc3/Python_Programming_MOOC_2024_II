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

exercise = 'src.lottery_numbers'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)


class LotteryNumberstTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected.")]):
           cls.module = load_module(exercise, 'en')

    @points('11.lottery_numbers_part1')
    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)
    
    @points('11.lottery_numbers_part1')
    def test_class_exists(self):
        try:
            from src.lottery_numbers import LotteryNumbers
        except Exception as e:
            self.fail(f'Make sure, that class LotteryNumbers exists!')

    @points('11.lottery_numbers_part1')  
    def test_2_creation_of_object(self):
        try:
            from src.lottery_numbers import LotteryNumbers
            a = LotteryNumbers(1,[1,2,3,4,5,6,7])
        except Exception as e:
            self.fail(f'Calling constructor LotteryNumbers(1,[1,2,3,4,5,6,7]) threw an error \n{e}\n' + 
            'Make sure, that object can be initialized by calling constructor.')
    
    @points('11.lottery_numbers_part1')
    def test_3a_method_number_of_hits(self):
        try:
            from src.lottery_numbers import LotteryNumbers
            row = LotteryNumbers(1,[1,2,3,4,5,6,7])
            n = row.number_of_hits([1,2,3,4,5,6,7])
        except Exception as e:
            self.fail(f'Method number_of_hits threw an error, when it was called as follows:\n' + 
                f'row = LotteryNumbers(1,[1,2,3,4,5,6,7])\n' + 
                f'n = row.number_of_hits([1,2,3,4,5,6,7])\n' + 
                f'The error was:\n{e}')

    @points('11.lottery_numbers_part1')
    def test_3b_number_of_hits_type_of_return_value(self):
        try:
            from src.lottery_numbers import LotteryNumbers
            row = LotteryNumbers(1,[1,2,3,4,5,6,7])
            val = row.number_of_hits([1,2,3,4,5,6,7])
        except Exception as e:
            self.fail(f'Method number_of_hits threw an error, when it was called as follows:\n' + 
                f'row = LotteryNumbers(1,[1,2,3,4,5,6,7])\n' + 
                f'n = row.number_of_hits([1,2,3,4,5,6,7])\n' + 
                f'The error was:\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == int, f"Method number_of_hits is expected to return a value which is of type integer," +  
            f" now it returns a value {val} which is of type {taip}\n when it was called as follows:\n" +  
            f'row = LotteryNumbers(1,[1,2,3,4,5,6,7])\n' + 
            f'n = row.number_of_hits([1,2,3,4,5,6,7])\n')
        
    @points('11.lottery_numbers_part1')
    def test_4_length_of_method_number_of_hits(self):
        from src.lottery_numbers import LotteryNumbers
        lines = source_rows(LotteryNumbers.number_of_hits)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Method number_of_hits must have at most ' + 
            f' {max_lines} rows in this exercise.\n' +
            f'The method now has a total of {lines} rows (excluding empty rows and comments.')

    @points('11.lottery_numbers_part1')
    def test_5a_test_number_of_hits_with_values_1(self):
        test_case = [1,2,5,6,9,10,11]
        correct = [1,3,5,7,9,11,13]
        corr = 4
        from src.lottery_numbers import LotteryNumbers
        row = LotteryNumbers(1, correct)
        val = row.number_of_hits(test_case)

        self.assertEqual(val, corr, f'Method number_of_hits is expected to return {corr}\n' + 
            f'when it is called as follows:\n' +
            f'row = LotteryNumbers({correct})\n' + 
            f'n = row.number_of_hits({test_case})\n' 
            f'now method returns {val}')

    @points('11.lottery_numbers_part1')
    def test_5b_test_number_of_hits_with_values_2(self):
        test_case = [5,10,15,20,25,30,35]
        correct = [6,7,10,11,12,13,15]
        corr = 2
        from src.lottery_numbers import LotteryNumbers
        row = LotteryNumbers(1, correct)
        val = row.number_of_hits(test_case)

        self.assertEqual(val, corr, f'Method number_of_hits is expected to return {corr}\n' + 
            f'when it is called as follows:\n' +
            f'row = LotteryNumbers({correct})\n' + 
            f'n = row.number_of_hits({test_case})\n' 
            f'now method returns {val}')

    @points('11.lottery_numbers_part2')
    def test_6_method_hits_in_place(self):
        try:
            from src.lottery_numbers import LotteryNumbers
            row = LotteryNumbers(1,[1,2,3,4,5,6,7])
            n = row.hits_in_place([1,2,3,4,5,6,7])
        except Exception as e:
            self.fail(f'Method hits_in_place( threw an error, when it was called as follows:\n' + 
                f'row = LotteryNumbers(1,[1,2,3,4,5,6,7])\n' + 
                f'n = row.hits_in_place(([1,2,3,4,5,6,7])\n' + 
                f'The error was:\n{e}')

    @points('11.lottery_numbers_part2')
    def test_7_hits_in_place_type_of_return_value(self):
        try:
            from src.lottery_numbers import LotteryNumbers
            row = LotteryNumbers(1,[1,2,3,4,5,6,7])
            val = row.hits_in_place([1,2,3,4,5,6,7])
        except Exception as e:
            self.fail(f'Method hits_in_place threw an error, when it was called as follows:\n' + 
                f'row = LotteryNumbers(1,[1,2,3,4,5,6,7])\n' + 
                f'n = row.hits_in_place([1,2,3,4,5,6,7])\n' + 
                f'The error was:\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Method hits_in_place is expected to return a value, which is of type list," +  
            f" now it returns a value {val} which is of type {taip}\n when it was called as follows:\n" +  
            f'row = LotteryNumbers(1,[1,2,3,4,5,6,7])\n' + 
            f'n = row.hits_in_place([1,2,3,4,5,6,7])\n')
        
    @points('11.lottery_numbers_part2')
    def test_8_length_of_method_hits_in_place(self):
        from src.lottery_numbers import LotteryNumbers
        lines = source_rows(LotteryNumbers.hits_in_place)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Method hits_in_place must have at most'+ 
            f' {max_lines} rows in this exercise.\n' +
            f'The method now has a total of {lines} rows (excluding empty rows and comments).')

    @points('11.lottery_numbers_part2')
    def test_9a_test_hits_in_place_with_values_1(self):
        test_case = [1,2,5,6,9,10,11]
        correct = [1,3,5,7,9,11,13]
        corr = [1,-1,5,-1,9,-1,11]
        from src.lottery_numbers import LotteryNumbers
        row = LotteryNumbers(1, correct)
        val = row.hits_in_place(test_case[:])

        self.assertEqual(val, corr, f'Method hits_in_place is expected to return\n{corr}\n' + 
            f'when it is called as follows:\n' +
            f'row = LotteryNumbers({correct})\n' + 
            f'n = row.hits_in_place({test_case})\n' 
            f'now method returns\n{val}')

    @points('11.lottery_numbers_part2')
    def test_9b_test_hits_in_place_with_values_2(self):
        test_case = [4,6,8,10,30,32,34]
        correct = [5,6,7,8,32,33,34]
        corr = [-1,6,8,-1,-1,32,34]
        from src.lottery_numbers import LotteryNumbers
        row = LotteryNumbers(1, correct)
        val = row.hits_in_place(test_case[:])

        self.assertEqual(val, corr, f'Method hits_in_place is expected to return\n{corr}\n' + 
            f'when it is called as follows:\n' +
            f'row = LotteryNumbers({correct})\n' + 
            f'n = row.hits_in_place({test_case})\n' 
            f'now method returns\n{val}')
    
if __name__ == '__main__':
    unittest.main()
