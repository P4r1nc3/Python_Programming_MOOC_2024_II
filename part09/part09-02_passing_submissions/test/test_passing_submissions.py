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

exercise = 'src.passing_submissions'
function = "passed"

def f(attr: list):
    return ",".join(attr)


@points('9.passing_submissions')
class PassingSubmissionsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testng the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_0b_constructor(self):
        try:
            from src.passing_submissions import ExamSubmission
            submission = ExamSubmission("Paul", 10)
        except Exception as e:
            self.fail(f'Calling constructor ExamSubmission("Paul", 10) threw an error \n{e}\n' +
                'Have you changed the implementation of the ExamSubmission class?')


    def test1_function_exists(self):
        try:
            from src.passing_submissions import passed
        except:
            self.assertTrue(False, "Your program should contain function " + 
                "named passed(submissions: list, lowest_passing: int)")

    def test2_type_of_return_value(self):
        from src.passing_submissions import passed, ExamSubmission
        val = passed([ExamSubmission("Paul", 10)], 5)
        taip = str(type(val)).replace("<class '","").replace("'>","")

        self.assertTrue(type(val) == list, f"Function passed must return a value of type list," +
            f' now it returns a value {val} which is of type {taip}\n when calling the function with the following parameter values\n [ExamSubmission("Paul", 10)], 5')

    def test3_test_submissions(self):
         test_cases = [[("Arthur",10),("Matt",15), 14], [("Becky", 5), ("Paul", 3), 4], 
                       [("Paula", 20), ("Pippa", 18), ("Pia", 13), ("Paul", 15), 17], 
                       [("Larry", 24), ("Laura", 14), ("Lisa", 13), ("Lauren", 20), ("Lotta", 19), 15],
                       [("Kari", 29), ("Kake", 26), ("Keijo", 10), ("Kalle", 17), ("Kirsi", 30), ("Kiia", 22), 15],
                       [("Emilia", 10), ("Erkki", 9), 10]]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                passed = load(exercise, function, 'en')
                from src.passing_submissions import ExamSubmission

                testlist = [ExamSubmission(x[0], x[1]) for x in test_case[:-1]]
                val = sorted(passed(testlist, test_case[-1]), key = lambda x : x.examinee)    
                corr = sorted([x for x in testlist if x.points >= test_case[-1]], key = lambda x: x.examinee)

                self.assertEqual(len(val), len(corr), f"The function should return {len(corr)} items, but it returns {len(val)} items\n" +
                    f'kun syöte on\n{test_case}')
                self.assertEqual(val, corr, f'The function should return a list \n{corr},\n but it returns a list \nn{val}\n when the input is \n{test_case}')
                
if __name__ == '__main__':
    unittest.main()
