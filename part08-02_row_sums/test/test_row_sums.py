import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.row_sums'
function = "row_sums"

def get_corr(m):
    return [r + [sum(r)] for r in m]
        

@points('8.row_sums')
class RowSumsTest(unittest.TestCase):
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

    def test1_function_exists(self):
        try:
            from src.row_sums import row_sums
        except:
            self.fail("Your program must contain a function row_sums(matrix: list)")

    def test2_return_type(self):
        try:
            from src.row_sums import row_sums
            val = row_sums([[1,1],[2,2]])
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(val == None, f"Function row_sums should not return a value," +  
                f" \nnow it returns a value {val} which is of type {taip}\n when it's called with arguments \n[[1,1],[2,2]]")
        except Exception as e:
            self.fail(f"Function threw an error when called with arguments [[1,1],[2,2]]:\n{e}")


    def test3_test_values(self):
        test_cases = ([[1,1],[2,2]], [[2]*3,[4]*3,[6]*3], [[1,2,3,4],[2,3,4,5],[3,4,5,6]], [[5,6],[4,1],[10,20],[6,9],[11,22]],
                      [[1,3,5,7,9],[2,4,6,8,10],[-1,-3,-5,-7,-9]])
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
                reload_module(self.module)
                row_sums = load(exercise, function, 'en')

                test_case_2 = [m[:] for m in test_case[:]]
                row_sums(test_case)
                
                corr = get_corr(test_case_2)

                self.assertEqual(test_case, corr, f"After executing the function, the matrix should be\n{corr}\nbut it is \n{test_case}\nwhen arguments are\n{test_case_2}")

    

if __name__ == '__main__':
    unittest.main()
