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

exercise = 'src.fastest_car'
function = "fastest_car"

def f(attr: list):
    return ",".join(attr)


@points('9.fastest_car')
class FastestCarTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_0b_constructor(self):
        try:
            from src.fastest_car import Car
            Lada = Car("Lada", 110)
        except Exception as e:
            self.fail(f'Calling constructor Lada = Car("Lada", 110) threw an error \n{e}')


    def test1_function_exists(self):
        try:
            from src.fastest_car import fastest_car
        except:
            self.assertTrue(False, "Your code should contain function " + 
                "named fastest_car(cars: list)")

    def test2_type_of_return_value(self):
        from src.fastest_car import fastest_car, Car
        val = fastest_car([Car("Mercedes-Benz",200), Car("Lada",100)])
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == str, f"Function fastest_car must return a value of type string (str)," +
            f' now it returns a value {val} which is of type {taip}\n when calling the function with the following parameter values\n [Car("Mercedes-Benz",200), Car("Lada",100)])')


    def test3_test_lists(self):
        test_cases = [[("Mercedes-Benz",200),("Volvo",180)], [("Opel", 175), ("Mazda", 185)], [("Lada", 170), ("Mercedes-Benz", 155), ("Volvo", 175)],
                      [("Ferrari", 300), ("Bugatti", 350), ("Lamborghini", 330)],
                      [("Trabant", 100), ("Lada", 110), ("Skoda", 105), ("Mosse", 95)]]
        for test_case in test_cases:
            speed, amount = -1, 0
            for x in test_case:
                if x[1] > speed:
                    speed = x[1]
                    amount = 1
                elif x[1] == speed:
                    amount += 1
            self.assertEqual(amount, 1, "Error while testing: fastest car is not unambiguous")
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                fastest_car = load(exercise, function, 'en')
                from src.fastest_car import Car

                testlist = [Car(x[0], x[1]) for x in test_case]
                val = fastest_car(testlist)
                corr = max(testlist, key = lambda x : x.top_speed).make

                self.assertEqual(val, corr, f'The function should return {corr}, but it returns {val} when the test list is \n{testlist}')
                
if __name__ == '__main__':
    unittest.main()
