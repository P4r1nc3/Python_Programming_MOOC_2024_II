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

exercise = 'src.car'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('9.car')
class CarTest(unittest.TestCase):
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
            from src.car import Car
            c = Car()
        except Exception as e:
            self.fail(f'Calling constructor Car() threw an error \n{e}\n' + 
            'Make sure, that class is defined.')

    def test_2_methods_exists(self):
        from src.car import Car
        c = Car()
        try:
             c.drive(10)
        except Exception as e:
            self.fail(f"Method call drive(10) threw an error \n{e}")

        try:
            c.fill_up()
        except Exception as e:
            self.fail(f"Method call fill_up() threw an error \n{e}")

    def test3_test_attributes(self):
        from src.car import Car
        c = Car()
        ref = reflect.Reflect()
        ref.set_object(c)

        att = ref.list_public_members()
        if "drive" in att: att.remove("drive")
        if "fill_up" in att: att.remove("fill_up")

        self.assertEqual(len(att), 0, f'Class Car should not have other public members than ' +
            f'methods drive and fill_up. Now it also have following public members:\n'+ f(att))

    def test4_test_str(self):
        from src.car import Car
        c = Car()
        try:
            output = str(c)
        except Exception as e:
            self.fail(f"Callling Car's __str__-method throws an error {e}.")

        self.assertTrue("0 km" in output and "0 litres" in output, f'Car\'s __str__-method should return ' +
            f'a string "Car: odometer reading 0 km, petrol remaining 0 litres", now it returns\n{output}')
        

    def test5_test_fill_up(self):
        from src.car import Car
        c = Car()

        c.fill_up()
        output = str(c)

        self.assertTrue("60 litres" in output, f"After fill up, car's amount of petrol in the tank should be 60 litres, now " +
            f"__str__-method returns\n{output}")

    def test6_test_drive_and_fill_up(self):
        from src.car import Car
        c = Car()
        c.fill_up()

        test_cases = [10, 20, 10, 20, 5]
        petrol = 60
        km = 0
        tests = ""
        for test_case in test_cases:
            c.drive(test_case)
            if test_case <= petrol:
                petrol -= test_case
                km += test_case
            tests += f"\ndrive({test_case})"

            output = str(c)

            self.assertTrue(str(petrol) + " litres" in output and str(km) + " km" in output, f'The printout of the car should report ' +
                f'amount of petrol in the tank to be {petrol} litres and odometer reading {km} km when after initialing the the object ' +
                f'following methods have been called:\n{tests}' +
                f'\nNow the printout is\n{output}')

        c.fill_up()
        tests += "\nfill_up()"
        test_cases = [10, 30, 20]
        petrol = 60
        for test_case in test_cases:
            c.drive(test_case)
            if test_case <= petrol:
                petrol -= test_case
                km += test_case
            tests += f"\ndrive({test_case})"

            output = str(c)

            self.assertTrue(str(petrol) + " litres" in output and str(km) + " km" in output, f'The printout of the car should report ' +
                f'amount of petrol in the tank to be {petrol} litres and odometer reading {km} km when after initialing the the object ' +
                f'following methods have been called:\n{tests}' +
                f'\nNow the printout is\n{output}')

if __name__ == '__main__':
    unittest.main()