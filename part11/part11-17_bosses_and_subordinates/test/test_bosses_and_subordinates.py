import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re

exercise = 'src.bosses_and_subordinates'

@points('11.bosses_and_subordinates')
class BossesAndSubordinatesTest(unittest.TestCase):
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
            from src.bosses_and_subordinates import count_subordinates
        except Exception as e:
            self.fail(f'Your program should contain function named count_subordinates.')

    def test_2_type_of_return_value(self):
        try:
            from src.bosses_and_subordinates import count_subordinates, Employee
            val = count_subordinates(Employee("Joe"))
        except Exception as e:
            self.assertTrue(False, f"Function threw an error when it was called as follows:" + 
                f'\ncount_subordinates(Employee(\"Joe\"))\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == int, f"Function count_subordinates should return a value, which is of type int," +  
            f" now it returns a value {val} which is of type {taip}\n when it is called as follows:\n" +  
            'count_subordinates(Employee(\"Joe\"))')

    def test_3_function(self):
        from src.bosses_and_subordinates import count_subordinates, Employee

        t1 = Employee("Sally")
        t2 = Employee("Matthew")
        t3 = Employee("Eric")
        t4 = Employee("Andy")
        t5 = Employee("Emily")
        t6 = Employee("James")
        t7 = Employee("John")
        t8 = Employee("Tina")
        t9 = Employee("Theodore")
        t10 = Employee("Arthur")
        t11 = Employee("Jack")
        t12 = Employee("Lea")
        t1.add_subordinate(t3)
        t1.add_subordinate(t4)
        t1.add_subordinate(t7)
        t3.add_subordinate(t8)
        t3.add_subordinate(t9)
        t3.add_subordinate(t10)
        t3.add_subordinate(t12)
        t9.add_subordinate(t2)
        t2.add_subordinate(t5)
        t2.add_subordinate(t11)
        t5.add_subordinate(t6)

        tests = [(t1,11),(t2,3),(t3,8),(t4,0),(t5,1),(t6,0),(t7,0),(t8,0),(t9,4),(t10,0),(t11,0),(t12,0)]
        for test in tests:
            result = count_subordinates(test[0])
            self.assertEqual(result, test[1], f"Employee {test[0].name} should have {test[1]} subordinates, but function returns {result} subordinates "+
                                               "(you can look the staff structure from the tests")

if __name__ == '__main__':
    unittest.main()
