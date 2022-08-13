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

exercise = 'src.first_and_last_name'

def f(attr: list):
    return ",".join(attr)

@points('8.first_and_last_name')
class FirstAndLastNameTest(unittest.TestCase):
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
            from src.first_and_last_name import Person
        except:
            self.fail("Your program should contain a class called Person")


    def test2_constructor(self):
        try:
            from src.first_and_last_name import Person
            val = Person("Peter Python")
            self.assertTrue(True, "")
        except Exception as e:
            self.assertTrue(False, 'Calling the constructor as Person("Peter Python")' +
                f' threw an error: {e}')

    def test3_test_first_name(self):
        test_cases = ("Peter Python", "Paula Pascal", "James Java", "Henry Haskell", "Benjamin Basic", "Carlos Csharp")
        for test_case in test_cases:
            try:
                from src.first_and_last_name import Person
                person = Person(test_case)
                val = person.return_first_name()
                corr = test_case.split(" ")[0]

                self.assertEqual(val, corr, f"Method return_first_name should return {corr}, when person was initalized asa\n" +
                    f"Person('{test_case}')\nNow method returns\n{val}")
                    
            except Exception as e:
                self.fail(f"There was an error when calling method return_first_name:\n{e}" +
                    f"The object was initalized as Person{(test_case)}")

    def test4_test_last_name(self):
        test_cases = ("Peter Python", "Paula Pascal", "James Java", "Henry Haskell", "Benjamin Basic", "Carlos Csharp")
        for test_case in test_cases:
            try:
                from src.first_and_last_name import Person
                person = Person(test_case)
                val = person.return_last_name()
                corr = test_case.split(" ")[-1]

                self.assertEqual(val, corr, f"Mtehod return_last_name should return {corr}, when the object was initalized as\n" +
                    f"Person('{test_case}')\nNow the method returns\n{val}")
                    
            except Exception as e:
                self.fail(f"There was an error when calling method return_last_name:\n{e}" +
                    f"The object was initalized as Person{(test_case)}")

    def test5_test_attributes(self):
        try:
            from src.first_and_last_name import Person
            person = Person("James Jamerson")
            en = person.return_first_name()
            sn = person.return_last_name()

            
        except Exception as e:
            self.fail(f"There was an error:\n{e}" +
                    f"when object was initalized as Person('James Jamerson')\n" + 
                    "and methods return_first_name() and return_last_name() were called")

        ref = reflect.Reflect(person)
        ref.set_object(person)
        att_list = ref.attributes_only()
        

        self.assertTrue(len(att_list) == 1, f"Class Person should have only one attribute, now there are {len(att_list)}\n" + 
            f"Please check, that you are not using self keyword when creating a local variable!\n" + 
            f"Here are the attributes now:\n{att_list}")



    

if __name__ == '__main__':
    unittest.main()
