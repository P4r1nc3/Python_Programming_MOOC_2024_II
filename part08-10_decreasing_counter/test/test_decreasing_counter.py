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

exercise = 'src.decreasing_counter'
classname = "DecreasingCounter"

def f(attr: list):
    return ",".join(attr)



class DecreasingCounterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_ok(self):
        ok, line = check_source(self.module)
        message = """All code testing the functions must be inside the
if __name__ == "__main__":
block. The following line must be moved:
"""
        self.assertTrue(ok, message+line)

    @points('8.decreasing_counter_part1')
    def test1_class_exists(self):
        try:
            from src.decreasing_counter import DecreasingCounter
        except:
            self.fail("Your program should have a class called DecreasingCounter")

    @points('8.decreasing_counter_part1')
    def test2_constructor(self):
        try:
            from src.decreasing_counter import DecreasingCounter
            val = DecreasingCounter(1)
            self.assertTrue(True, "")
        except Exception as e:
            self.fail('Calling constructor with DecreasingCounter(1)' +
                f' threw an error: {e}')

    @points('8.decreasing_counter_part1')
    def test3_test_decrease(self):
        test_cases = ((5,1), (9,4), (100,10), (1,1))
        for test_case in test_cases:
            try:
                from src.decreasing_counter import DecreasingCounter
                counter = DecreasingCounter(test_case[0])
                for i in range(test_case[1]):
                    counter.decrease()
                corr = test_case[0] - test_case[1]

                self.assertEqual(counter.value, corr, f"The value of counter should be{corr}, when it was initialized with\n" +
                    f"DecreasingCounter({test_case[0]})\nja and the method decrease was called {test_case[1]} times.\n" +
                    f"Now the value of counter is {counter.value}.")
            except Exception as e:
                self.fail(f"Calling method decrease threw an error:\n{e}" +
                    f"\nwhen the object was initialized with DecreasingCounter{(test_case[0])}")

    @points('8.decreasing_counter_part2')
    def test4_test_negative(self):
        test_cases = ((1,2), (3,6), (100,101), (1,10))
        for test_case in test_cases:
            try:
                from src.decreasing_counter import DecreasingCounter
                counter = DecreasingCounter(test_case[0])
                for i in range(test_case[1]):
                    counter.decrease()
                corr = 0

                self.assertEqual(counter.value, corr, f"The value of counter should be{corr}, when it was initialized with\n" +
                    f"DecreasingCounter({test_case[0]})\nja and the method decrease was called {test_case[1]} times.\n" +
                    f"Now the value of counter is {counter.value}. The value should not be negative!")
            except Exception as e:
                self.fail(f"Calling method decrease threw an error:\n{e}" +
                    f"\nwhen the object was initialized with DecreasingCounter{(test_case[0])}")

    @points('8.decreasing_counter_part3')
    def test5_test_set_to_zero(self):
        test_cases = ((1,0), (3,0), (100,10))
        for test_case in test_cases:
            try:
                from src.decreasing_counter import DecreasingCounter
                counter = DecreasingCounter(test_case[0])
                for i in range(test_case[1]):
                    counter.decrease()
                counter.set_to_zero()
                corr = 0

                self.assertEqual(counter.value, corr, f"The value of counter should be{corr}, when it was initialized with\n" +
                    f"DecreasingCounter({test_case[0]})\nja and the method decrease was called {test_case[1]} times.\n" +
                    f"and after this method set_to_zero() was called.\n" + 
                    f"Now value is {counter.value}.")
            except Exception as e:
                self.fail(f"Error occurred:\n{e}"
                    f"when an object was initialized as DecreasingCounter{(test_case[0])}" +
                    "\nand method decrease was called {test_case[1]} times,\n" +
                    f"and finally method set_to_zero() was called.")

    @points('8.decreasing_counter_part4')
    def test6_test_reset(self):
        test_cases = ((2,1), (3,3), (100,20), (5,10))
        for test_case in test_cases:
            try:
                from src.decreasing_counter import DecreasingCounter
                counter = DecreasingCounter(test_case[0])
                for i in range(test_case[1]):
                    counter.decrease()
                counter.reset_original_value()
                corr = test_case[0]

                self.assertEqual(counter.value, corr, f"The value of counter should be{corr}, when it was initialized with\n" +
                    f"DecreasingCounter({test_case[0]})\nja and the method decrease was called {test_case[1]} times.\n" +
                    f"and after this method reset_original_value() was called.\n" + 
                    f"Now value is {counter.value}.")
            except Exception as e:
                self.fail(f"Error occurred:\n{e}"
                    f"when an object was initialized as DecreasingCounter{(test_case[0])}" +
                    "\nand method decrease was called {test_case[1]} times,\n" +
                    f"and finally method reset_original_value() was called.")

    

if __name__ == '__main__':
    unittest.main()
