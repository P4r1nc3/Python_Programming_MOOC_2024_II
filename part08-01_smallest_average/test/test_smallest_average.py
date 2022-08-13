import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.smallest_average'
function = "smallest_average"

def hlo(t: tuple):
    return {"name": "Anna", "result1": t[0], "result2": t[1], "result3": t[2]}

def par(t1: tuple, t2: tuple, t3: tuple):
    s = "("
    for t in (t1,t2,t3):
        s += "{" + ",".join([f'"result{x}": {t[x-1]}' for x in range(1,4)]) + "}" + ", "
    return s[:-2] + ")"
        

@points('8.smallest_average')
class SmallestAverageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input wasn't expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_ok(self):
        ok, line = check_source(self.module)
        message = """All code testing the functions must be inside the
if __name__ == "__main__":
block. The following line must be moved:
"""
        self.assertTrue(ok, message+line)

    def test1_function_exists(self):
        try:
            from src.smallest_average import smallest_average
        except:
            self.fail("Your program must contain a function smallest_average(p1: dict, p2: dict, p3: dict)")

    def test2_return_type(self):
        try:
            from src.smallest_average import smallest_average
            val = smallest_average(hlo((1,1,1)), hlo((2,2,2)), hlo((3,3,3)))
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == dict, f"Function smallest_average should return a value of type dictg," +  
                f" now it returns {val} which is of type {taip}\nwhen called with parameters {par((1,1,1),(2,2,2),(3,3,3))}")
        except:
            self.fail(f"Function threw an error when called with parameter values {par((1,1,1),(2,2,2),(3,3,3))}")


    def test3_test_values(self):
        test_cases = [((1,1,1),(2,2,2),(3,3,3)), ((9,9,9),(7,7,7),(8,8,8)), ((3,3,3),(5,5,5), (1,1,1)), 
                      ((5,3,1),(6,4,2),(2,2,2)), ((9,3,8),(9,4,9),(9,6,8)), ((6,0,0), (5,0,0), (3,3,3)),
                      ((6,4,4),(5,7,7),(4,8,8)), ((4,3,4),(4,2,4),(4,3,4)), ((6,2,2), (5,2,2), (5,2,3))]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Input was not excpected")]):
                reload_module(self.module)
                smallest_average = load(exercise, function, 'en')

                h1 = hlo(test_case[0])
                h2 = hlo(test_case[1])
                h3 = hlo(test_case[2])

                results = [sum(test_case[0]),sum(test_case[1]),sum(test_case[2])]
                results.sort()
                if results[0] == results[1]:
                    self.fail("Error in tests: smallest average is not unique")

                val = smallest_average(h1, h2, h3)

                t1 = hlo(test_case[0])
                t2 = hlo(test_case[1])
                t3 = hlo(test_case[2])
                corr = min((t1,t2,t3), key=lambda x: ((x["result1"]+x["result2"]+x["result3"]) / 3))

                self.assertEqual(val, corr, f"Function should return \n{corr}\nbut it returns \n{val}\nwhen parameters are\n{par(test_case[0], test_case[1], test_case[2])}")

    

if __name__ == '__main__':
    unittest.main()
