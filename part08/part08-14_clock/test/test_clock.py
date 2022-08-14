import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date, datetime, timedelta

exercise = 'src.clock'
classname = "Clock"

def f(attr: list):
    return ",".join(attr)

@points('8.clock')
class ClockTest(unittest.TestCase):
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

    
    def test1_class_exists(self):
        try:
            from src.clock import Clock
        except:
            self.fail("Your program should contain a class called Clock")

    def test2_constructor(self):
        try:
            from src.clock import Clock
            clock = Clock(12,0,0)
            self.assertTrue(True, "")
        except Exception as e:
            self.fail('Calling constructor Clock(12,0,0)' +
                f' threw an error: {e}')

    def test3_test_str(self):
        test_cases = ((23,30,0), (10,10,10), (15,10,5), (23,5,15), (4,24,28), (3,4,5))
        for test_case in test_cases:
            try:
                from src.clock import Clock
                h,m,s = test_case
                clock = Clock(h,m,s)

                corr = (datetime(2000,1,1,h,m,s)).strftime("%H:%M:%S")
                val = str(clock)

                self.assertEqual(corr, val, f"Method __str__ should return string {corr}\nwhen object was created as\n" + 
                    f"Clock({h}:{m}:{s}).\nNow method returns {val}.")

            except Exception as e:
                self.fail('Calling method __str__ ' +
                    f' threw an error: {e}\nObject was initalized as Clock({h},{m},{s})')

    def test4_test_tick(self):
        test_cases = ((10,10,58,3),(23,59,55,6),(0,0,0,30),(23,58,30,31))
        for test_case in test_cases:
            try:
                from src.clock import Clock
                h,m,s,t = test_case
                clock = Clock(h,m,s)
                for i in range(t):
                    clock.tick()

                corr = (datetime(2000,1,1,h,m,s) + timedelta(seconds=t)).strftime("%H:%M:%S")
                val = str(clock)

                self.assertEqual(corr, val, f"Method __str__ should return string {corr}\nwhen object was created as\n" + 
                    f"Clock({h}:{m}:{s}) and method tick() was called {t} times.\nNow method returns {val}.")

            except Exception as e:
                self.fail( 'Calling method tick()' +
                    f' threw an error: {e}\nwhen object was initialized as Clock({h},{m},{s})')

    def test5_testaa_time_set(self):
        test_cases = ((10,10,58,15,15),(23,59,55,11,0),(0,0,0,12,0),(23,58,10,11,34))
        for test_case in test_cases:
            try:
                from src.clock import Clock
                h,m,s,h2,m2 = test_case
                clock = Clock(h,m,s)
                clock.set(h2,m2)

                corr = (datetime(2000,1,1,h2,m2,0)).strftime("%H:%M:00")
                val = str(clock)

                self.assertEqual(corr, val, f"Method __str__ should return string {corr}\nwhen object was created as\n" + 
                    f"Clock({h}:{m}:{s}) and afterwards method set({h2}:{m2}) was called.\nNow mtehod __str__ returns {val}.")

            except Exception as e:
                self.fail( f'Calling method set({h2},{m2})' +
                    f' threw an error: {e}\nwhen object was initialized as Clock({h},{m},{s})')

if __name__ == '__main__':
    unittest.main()
