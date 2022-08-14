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

exercise = 'src.stopwatch'
classname = "Stopwatch"

def f(attr: list):
    return ",".join(attr)

@points('8.stopwatch')
class StopwatchTest(unittest.TestCase):
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
            from src.stopwatch import Stopwatch
        except:
            self.fail("Your program should contain a class called Stopwatch")

        def test2_constructor(self):
            try:
                from src.stopwatch import Stopwatch
                clock = Stopwatch()
            except Exception as e:
                self.fail('Calling constructor Stopwatch()' +
                    f' threw an error: {e}')

    def test3_test_str(self):
        try:
            from src.stopwatch import Stopwatch
            clock = Stopwatch()

            corr = "00:00"
            val = str(clock)

            self.assertEqual(corr, val, f"Method __str__ should return a string {corr}\nObject was initialized as\n" + 
                f"Stopwatch().\nNow method returns {val}.")

        except Exception as e:
            self.fail('Calling method __str__ ' +
                f'threw an error: {e}\nwhen object was initalized as Stopwatch()')

    def test5_tick_exists(self):

        try:
            from src.stopwatch import Stopwatch
            code = """
clock = Stopwatch()                
clock.tick()
"""

            clock = Stopwatch()
            clock.tick()  

        except Exception as e:
            self.assertTrue(False, f'Executing code\n{code}\nthrew an error\n{e}\nCheck that method tick(self) is defined.')

    def test6_test_tick(self):
            try:
                from src.stopwatch import Stopwatch
                clock = Stopwatch()
                clock.tick()

                code = """
clock = Stopwatch()                
clock.tick()                
""" 
                corr = "00:01"
                val = str(clock)

                self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwafter executing code\n{code}\nNow method returns\n{val}")

                clock.tick()
                clock.tick()

                code += "clock.tick()\nclock.tick()\n"   

                corr = "00:03"
                val = str(clock)

                self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwafter executing code\n{code}\nNow method returns\n{val}")

                clock = Stopwatch()
                for i in range(60):
                    clock.tick()
                
                code = """
clock = Stopwatch()
for i in range(60):
    clock.tick()         
""" 

                corr = "01:00"
                val = str(clock)

                self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwafter executing code\n{code}\nNow method returns\n{val}")
                
                clock.tick()

                code += "clock.tick()\nclock.tick()\n"   

                corr = "01:01"
                val = str(clock)

                self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwafter executing code\n{code}\nNow method returns\n{val}")
                
                clock = Stopwatch()
                for i in range(60*59+59):
                    clock.tick()
                
                code = """
clock = Stopwatch()
# advance hour minus one second
for i in range(60*59+59):
    clock.tick()         
""" 

                corr = "59:59"
                val = str(clock)

                self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwafter executing code\n{code}\nNow method returns\n{val}")
                
                code += "clock.tick()\n"   

                clock.tick()
                corr = "00:00"
                val = str(clock)

                self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwafter executing code\n{code}\nNow method returns\n{val}")
                

            except Exception as e:
                self.fail('Calling method tick()' +
                f' threw an error: {e}\nwhen the following code was executed\n{code}')

if __name__ == '__main__':
    unittest.main()
