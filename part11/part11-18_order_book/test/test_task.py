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

exercise = 'src.order_book'

def f(attr: list):
    return ",".join(attr)

def s(l: list):
    return "\n".join(l)

@points('11.order_book_part1')
class TaskTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test1_task_exists(self):
        try:
            from src.order_book import Task
        except:
            self.assertTrue(False, "Your program should contain class named Task")

    def test2_constructor(self):
        try:
            from src.order_book import Task
            t = Task("code hello world", "Eric", 3)
        except Exception as e:
            self.assertTrue(False, 'Calling constructor of class Task with values Task("code hello world", "Eric", 3)' +
                f' threw an error: {e}\nMake sure, that constructor is defined properly')
        
        try:
            code = """
t = Task("code hello world", "Eric", 3)
t.programmer
"""
            result = t.programmer
        except Exception as e:
            self.fail(f"Executing the following code {code} threw an error {e}")
        expected = "Eric" 
        self.assertTrue(result == expected, f"When executing the following code {code}\nexpected result is {expected} but result was {result}")

        try:
            code = """
t = Task("code hello world", "Eric", 3)
t.description
"""
            result = t.description 
        except Exception as e:
            self.fail(f"Executing the following code {code} threw an error {e}")
        expected = "code hello world"
        self.assertTrue(result == expected, f"When executing the following code {code}\nexpected result is {expected} but result was {result}")

        try:
            code = """
t = Task("code hello world", "Eric", 3)
t.workload
"""
            result = t.workload 
        except Exception as e:
            self.fail(f"Executing the following code {code} threw an error {e}")
        expected = 3
        self.assertTrue(result == expected, f"When executing the following code {code}\nexpected result is {expected} but result was {result}")

        try:
            code = """
t = Task("code hello world", "Eric", 3)
t.id
"""
            result = t.id 
        except Exception as e:
            self.fail(f"Executing the following code {code} threw an error {e}")

    def test3_id(self):
        try:
            from src.order_book import Task
            t1 = Task("code hello world", "Eric", 3)
            t2 = Task("code facebook", "Eric", 4)
            t3 = Task("program mobile app", "Eric", 5)
        except Exception as e:
            self.assertTrue(False, 'Calling constructor of class Task with values Task("code hello world", "Eric", 3)' +
                f' threw an error: {e}\nMake sure, that constructor is defined properly')
        
        try:
            code = """
t1 = Task("code hello world", "Eric", 3)
t2 = Task("code facebook", "Eric", 4)
t3 = Task("program mobile app", "Eric", 5)
"""
            id1 = t1.id
            id2 = t2.id
            id3 = t3.id
        except Exception as e:
            self.fail(f"Executing the following code {code} threw an error {e}")
        expected = "Eric" 
        self.assertTrue(id1 != id2, f"After executing the following code {code}all id-fields should have distinct values. Now values are {id1}, {id2} and {id2}")
        self.assertTrue(id1 != id3, f"After executing the following code {code}all id-fields should have distinct values. Now values are {id1}, {id2} and {id2}")
        self.assertTrue(id2 != id3, f"After executing the following code {code}all id-fields should have distinct values. Now values are {id1}, {id2} and {id2}")

    def test_4_method_is_finished(self):
        from src.order_book import Task
        code = """
t = Task("code hello world", "Eric", 3)
t.is_finished() 
"""
        t = Task("code hello world", "Eric", 3)
        try:
            val = t.is_finished()
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method defined?')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == type(True), f"When executing the following code{code}type of return value should be boolean, now return value is of type {taip}")
        self.assertFalse(val, f"When executing the following code{code}return value should be False, now it is {val}")

    def test_5_method_mark_finished(self):
        from src.order_book import Task
        code = """
t = Task("code hello world", "Eric", 3)
t.mark_finished() 
"""
        t = Task("code hello world", "Eric", 3)
        try:
            t.mark_finished() 
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method defined?')

        code = """
t = Task("code hello world", "Eric", 3)
t.mark_finished()
t.is_finished() 
"""

        val = t.is_finished()
        self.assertTrue(val, f"When executing the following code{code}return value should be False, now it is {val}")

    def test_6_str(self):
        from src.order_book import Task
        code = """
t = Task("code hello world", "Andy", 3)
print(t)
"""
        t = Task("code hello world", "Andy", 3)
        try:
            f"{t}"
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method defined?')

        expected = f"{t.id}: code hello world (3 hours), programmer Andy NOT FINISHED" 
        oli = f"{t}"
        self.assertTrue(expected == oli, f"String representation of the object is incorrect. When executing the following code{code}\nexpected print out is\n{expected}\nbut string representation was\n{oli}")

        code = """
t = Task("code hello world", "Andy", 3)
t.mark_finished()
print(t)
"""
        t.mark_finished() 
        expected = f"{t.id}: code hello world (3 hours), programmer Andy FINISHED" 
        oli = f"{t}"
        self.assertTrue(expected == oli, f"String representation of the object is incorrect. When executing the following code{code}\nexpected print out is\n{expected}\nbut string representation was\n{oli}")

if __name__ == '__main__':
    unittest.main()