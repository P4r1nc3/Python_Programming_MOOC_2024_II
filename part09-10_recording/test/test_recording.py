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

exercise = 'src.recording'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('9.recording')
class RecordingTest(unittest.TestCase):
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

    def test_1_class_exists(self):
        try:
            from src.recording import Recording
            r = Recording(1)
        except Exception as e:
            self.fail(f'Calling constructor Recording(1) threw an error \n{e}\n' + 
            'Make sure, that class is defined.')

    def test_2_methods_exists(self):
        from src.recording import Recording
        r = Recording(1)
        try:
             val = r.length
             taip = str(type(val)).replace("<class '","").replace("'>","")
             self.assertTrue(type(val) == int, f'The getter method length should return an integer. ' +
                f'Now it returns a value {val} which is of type {taip}.')
        except Exception as e:
            self.fail(f"Program\nr = Recording(1)\nvalue = r.length\n threw an error \n{e}")

        try:
             r.length = 3
        except Exception as e:
            self.fail(f"Program\nr = Recording(1)\nr.length = 3\n threw an error \n{e}")

    def test3_test_attributes(self):
        from src.recording import Recording
        r = Recording(1)
        ref = reflect.Reflect()
        ref.set_object(r)

        att = ref.list_public_members()

        self.assertTrue(ref.has_attribute("length"), f'Class Recording should have public getter method length')

        att.remove("length")

        self.assertEqual(len(att), 0, f'Class Recording should not have other public members than  ' +
            f'getter and setter method for length. Now it also have following public members:\n'+ f(att))
    
    def test4_test_allowed(self):
        from src.recording import Recording
        test_cases = [(1,10), (5,50), (100,10)]
        for test_case in test_cases:
            r = Recording(test_case[0])
            self.assertEqual(r.length, test_case[0], f'The length should be {test_case[0]} when object is initialized as follows:\n' +
                f'Recording({test_case[0]})\nNyt length kuitenkin on {r.length}')

            r.length = test_case[1]
            self.assertEqual(r.length, test_case[1], f'The length should be {test_case[1]} after executing following rows:\n' +
                f'r = Recording({test_case[0]})\nr.length = {test_case[1]}\n' + 
                f'Now, however, length is {r.length}')

    def test5_test_forbidden(self):
        from src.recording import Recording

        for i in [-1,-5,-1000]:
            try:
                r = Recording(i)
                self.fail(f'Class is expected to raise ValueError-exception, when it is initialized as follows:\nRecording({i})')
            except Exception as ve:
                if type(ve) is not ValueError:
                    taip = str(type(ve)).replace("<class '","").replace("'>","")
                    self.fail(f'Class is expected to raise ValueError-exception, when it is initialized as follows:\nRecording({i})\n')

        for i in [-1,-5,-1000]:
            try:
                r = Recording(1)
                r.length = i
                self.fail(f'Class is expected to raise ValueError-exception, when setter method is called with value {i}')
            except Exception as ve:
                if type(ve) is not ValueError:
                    taip = str(type(ve)).replace("<class '","").replace("'>","")
                    self.fail(f'Class is expected to raise ValueError-exception, when setter method is called with value {i}\n')
    
if __name__ == '__main__':
    unittest.main()
