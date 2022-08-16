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

exercise = 'src.pets'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('9.pets')
class PetsTest(unittest.TestCase):
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

    def test_1_classes_exists(self):
        try:
            from src.pets import Pet
            l = Pet("Rex","dog")
        except Exception as e:
            self.fail(f'Calling constructor Pet("Rex","dog") threw an error \n{e}\n' + 
            'Do not change the class Pet!')

        try:
            from src.pets import Person
            h = Person("Bill", l)
        except Exception as e:
            self.fail(f'Calling constructor Person("Bill",pet("Rex","dog")) threw an error \n{e}\n')

    def test2_str_works(self):
        test_cases = [("Peter","Buddy","little dog"), ("Bill","Cupcake", "golden hamster"),
                      ("Lisa","Jack Sparrow","witty goldfish"), ("Jake", "Spike", "cursing hedghog")]
        for test_case in test_cases:
            from src.pets import Pet,Person
            lem = Pet(test_case[1], test_case[2])
            hen = Person(test_case[0], lem)
            val = str(hen)

            corr = f"{test_case[0]}, whose pal is {test_case[1]}, a {test_case[2]}"

            for mjono in test_case:
                self.assertTrue(mjono in val, f'The string returned by __str__ method is expected to include {mjono}\n' +
                    f'"when object is initialized as follows:\n' +
                    f'Person("{test_case[0]}", Pet("{test_case[1]}", "{test_case[2]}"))')

            self.assertEqual(val, corr, f"Method __str__ should return\n{corr}\n" +
                f"now it returns\n{val}\n" +
                f'when object is initialized as follows:\n' +
                f'Person("{test_case[0]}", Pet("{test_case[1]}", "{test_case[2]}"))' +
                "\nMake sure, that also commas and spaces are in right places!")
                
if __name__ == '__main__':
    unittest.main()