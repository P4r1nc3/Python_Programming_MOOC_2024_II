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

exercise = 'src.baby_centre'

def f(attr: list):
    return ",".join(attr)


class BabyCentreTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected.")]):
           cls.module = load_module(exercise, 'en')

    @points('9.baby_centre_part1')
    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    @points('9.baby_centre_part1')
    def test_1_classes_exists(self):
        try:
            from src.baby_centre import Person
            h = Person("Peter", 19, 175, 73)
        except Exception as e:
            self.fail(f'Calling constructor Person("Peter", 19, 175, 73) threw an error \n{e}\n' +
                'Have you changed the implementation of the class Person?')
        try:
            from src.baby_centre import BabyCentre
            k = BabyCentre()
        except Exception as e:
            self.fail(f'Calling constructor BabyCentre() threw an error \n{e}\n' +
                'Does the class BabyCentre exists?')

    @points('9.baby_centre_part1')
    def test_2_weigh_works(self):
        test_cases = [("Peter", 19, 175, 73), ("Pia", 10, 143, 35), ("Carl", 44, 185, 96), 
            ("Eric", 37, 180, 78), ("Lisa", 17, 176, 68)]
        for test_case in test_cases:
            from src.baby_centre import Person, BabyCentre
            centre = BabyCentre()
            p = Person(test_case[0], test_case[1], test_case[2], test_case[3])
            val = centre.weigh(p)
        
            corr = test_case[3]

            self.assertEqual(val, corr, f'Method weigh() returned a value {val}.\nWhen the correct value would have been {corr}, ' +
                f'when the object was initialized as follows:\nPerson{test_case}')
            

    @points('9.baby_centre_part2')    
    def test_3_feed_works(self):
        test_cases = [("Peter", 19, 175, 73, 1), ("Pia", 10, 143, 35, 3), ("Carl", 44, 185, 96, 5), 
            ("Eric", 37, 180, 78, 4), ("Lisa", 17, 176, 68, 2)]
        for test_case in test_cases:
            from src.baby_centre import Person, BabyCentre
            centre = BabyCentre()
            p = Person(test_case[0], test_case[1], test_case[2], test_case[3])
            for i in range(test_case[4]):
                centre.feed(p)
            
            val = centre.weigh(p)
            corr = test_case[3] + test_case[4]

            self.assertEqual(val, corr, f'Weight of the person is now {val}.\n, but it should be {corr}, ' +
                f'when the object was initialized as follows:\nPerson{test_case[:-1]}\n' +
                f'and the method feed() was called {test_case[4]} times.')
    
    @points('9.baby_centre_part3')
    def test_4_counting_the_weigh_ins(self):
        test_cases = [("Peter", 19, 175, 73, 1), ("Pia", 10, 143, 35, 3), ("Carl", 44, 185, 96, 5), 
            ("Eric", 37, 180, 78, 4), ("Lisa", 17, 176, 68, 2)]
        for i in range(1, len(test_cases)):
            from src.baby_centre import Person, BabyCentre
            centre = BabyCentre()
            for test_case in test_cases[:i]:
                p = Person(test_case[0], test_case[1], test_case[2], test_case[3])
                centre.weigh(p)
            corr = i
            val = centre.weigh_ins()
            
            self.assertEqual(val, corr, f'Method weigh_ins() returned a value {val}.\n, when the correct value would have been {corr}, ' +
                    f'when the method weigh() was called {i} times')
                
if __name__ == '__main__':
    unittest.main()