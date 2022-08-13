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

exercise = 'src.number_stats'

def f(attr: list):
    return ",".join(attr)

class NumbesrStatsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0","-1"]):
           cls.module = load_module(exercise, 'en')

    def test0a_main_ok(self):
        with open("src/number_stats.py") as t:
            if "if __name__" in t.read():
                self.fail('Main program cannot be written inside if __name__ == "__main__": block')

    @points('8.number_stats_part1')
    def test1_class_exists(self):
        with patch('builtins.input', side_effect=["0","-1"]):
            try:
                from src.number_stats import NumberStats
            except:
                self.fail("Your program should have a class called NumberStats")

    @points('8.number_stats_part1')
    def test2_constructor(self):
        with patch('builtins.input', side_effect=["0","-1"]):
            try:
                from src.number_stats import NumberStats
                val = NumberStats()
            except Exception as e:
                self.fail('Calling constructor NumberStats() ' +
                    f' threw an error: {e}')

    @points('8.number_stats_part1')
    def test2b_test_methods(self):
        from src.number_stats import NumberStats
        stats = NumberStats()
        try:
            stats.add_number(1)
        except Exception as e:
            self.fail(f"Calling method add_number(1) threw an error {e}, " +
                "Check that the method is included in the class!")
        try:
            stats.count_numbers()
        except Exception as e:
            self.fail(f"Calling method count_numbers() threw an error {e}, " +
                "Check that the method is included in the class!")
        

    @points('8.number_stats_part1')
    def test3_test_count_numbers(self):
        test_cases = ([1], (2,3,4,2), (9,8,7,5,3,2,4,1), (3,3), (5,5,5,5,4,4,4,4,3,3,3,3,4,4,4,4))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=["0","-1"]):    
                try:
                    from src.number_stats import NumberStats
                    number_stats = NumberStats()
                    for number in test_case:
                        number_stats.add_number(number)
                    corr = len(test_case)
                except Exception as e:
                    self.fail(f"Using class threw an error:\n{e}" +
                        "\nObject was initialized with\n" +
                        f"NumberStats()\nand method add_number called with values {test_case}")

                self.assertEqual(number_stats.count_numbers(), corr, f"The number count should be {corr}, when object was initialized with\n" +
                    f"NumberStats()\nand method add_number was called with {test_case}.\n" +
                    f"Now count_numbers returns {number_stats.count_numbers()}.")
                

    @points('8.number_stats_part2')
    def test3_test_get_sum(self):
        from src.number_stats import NumberStats
        number_stats = NumberStats()
        number_stats.add_number(1)
        try:
            number_stats.get_sum()
        except Exception as e:
            self.fail(f"Method call get_sum() threw an error {e}, " +
                "Please check that method is defined in the class!")
       
        test_cases = ([1], (2,3), (5,4,3,4,5), (3,3), (5,5,5,5,4,4,4,4,3,3,3,3,4,4,4,4))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=["0","-1"]):
                number_stats = NumberStats()
                for number in test_case:
                    number_stats.add_number(number)
                corr = sum(test_case)
                val = number_stats.get_sum()

                self.assertEqual(val, corr, f"The sum on numbers should be {corr}, when object was initialized as\n" +
                    f"NumberStats()\nand method add_number was called with values {test_case}.\n" +
                    f"Now get_sum() returns {val}.")

                # Check that count didn't break here
                self.assertEqual(number_stats.count_numbers(), len(test_case), f"Count should be {len(test_case)}, when object was initialized as\n" +
                    f"NumberStats()\nand method add_number was called with {test_case}.\n" +
                        f"Now count_numbers returns {number_stats.count_numbers()}.")

    @points('8.number_stats_part2')
    def test3_test_empty_average(self):
        try:
            from src.number_stats import NumberStats
            number_stats = NumberStats()
            number_stats.average()
        except ZeroDivisionError:
            self.assertTrue(False, "Make sure, that you do not divide by zero, when calling method average() with no numbers added.")
        except Exception as e:
                self.assertTrue(False, f"Calling method average() with no numbers added threw an error:\n{e}")

    @points('8.number_stats_part2')
    def test3_test_average(self):
        from src.number_stats import NumberStats
        number_stats = NumberStats()
        try:
            number_stats.average()
        except Exception as e:
            self.fail(f"Calling method average() threw an error {e}, " +
                "Check that the method is defined in class!")
        
        test_cases = ([1,1], (2,3), (1,2,3,4), (3,3), (5,5,5,5,4,4,4,4))
        for test_case in test_cases:
            number_stats = NumberStats()
            with patch('builtins.input', side_effect=["0","-1"]):            
                for number in test_case:
                    number_stats.add_number(number)
                corr = sum(test_case) / len(test_case)
                val = number_stats.average()

                self.assertEqual(val, corr, f"The average of numbers should be {corr}, when object was initialized with\n" +
                    f"NumberStats()\nand method add_number was called with {test_case}.\n" +
                    f"Now average() returns {val}.")
                
  
    @points('8.number_stats_part3')
    def test3_test_input_get_sum_and_avg(self):
        test_cases = ([1,-1], (2,3,-1), (5,4,3,4,5,-1), (3,3,-1), (5,5,5,5,4,4,4,4,3,3,3,3,4,4,4,4,-1))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=list([str(x) for x in test_case])):
                reload_module(self.module)

                output = get_stdout()

                get_sum = sum([x for x in test_case if x != -1])
                ka = get_sum / (len(test_case) - 1)

                corr1 = f"Sum of numbers: {get_sum}"
                corr2 = f"Mean of numbers: {ka}"

                self.assertTrue(corr1 in output, f"Output should contain line\n{corr1}\nwhen input is \n{test_case}.\nNow output is \n{output}")
                self.assertTrue(corr2 in output, f"Output should contain line\n{corr2}\nwhen input is \n{test_case}.\nNow output is \n{output}")
                
    @points('8.number_stats_part4')
    def test3_testaa_input_even_odd(self):
        test_cases = ([1,2,-1], (1,2,3,2,3,2,-1), (5,4,3,4,5,-1), (10,9,8,7,6,5,4,3,2,1,-1))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=list([str(x) for x in test_case])):
                reload_module(self.module)

                output = get_stdout()

                even = sum([x for x in test_case if x % 2 == 0])
                odd = sum([x for x in test_case if x % 2 != 0 and x != -1])

                corr1 = f"Sum of even numbers: {even}"
                corr2 = f"Sum of odd numbers: {odd}"

                self.assertTrue(corr1 in output, f"Output should contain line\n{corr1}\nwhen input is \n{test_case}.\nNow output is \n{output}")
                self.assertTrue(corr2 in output, f"Output should contain line\n{corr1}\nwhen input is \n{test_case}.\nNow output is \n{output}")

   

if __name__ == '__main__':
    unittest.main()
