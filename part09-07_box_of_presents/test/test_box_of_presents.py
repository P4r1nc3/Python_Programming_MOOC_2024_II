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

exercise = 'src.box_of_presents'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 


class BoxOfPresentsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected.")]):
           cls.module = load_module(exercise, 'en')

    @points('9.box_of_presents_part1')
    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    @points('9.box_of_presents_part1')
    def test_1_class_present_exists(self):
        try:
            from src.box_of_presents import Present
            l = Present("Ball", 1)
        except Exception as e:
            self.fail(f'Calling constructor Present("Ball", 1) threw an error \n{e}\n')        

    @points('9.box_of_presents_part1')
    def test_2_present_works(self):
        test_cases = [("Ball", 1), ("Toy train",2), ("Bicycle", 5), 
                      ("Guitar", 3), ("Car", 2000)]
        for test_case in test_cases:
            ref = reflect.Reflect()
            from src.box_of_presents import Present
            Present = Present(test_case[0], test_case[1])
            ref.set_object(Present)

            for att in ("name", "weight"):
                self.assertTrue(ref.has_attribute(att), f'Class Present should have ' + 
                    f'attribute named {att}')

            self.assertEqual(Present.name, test_case[0], f'Value of the attribute name should be ' +
                f'{test_case[0]}, when object is initialized as follows:\n' +
                f'Present("{test_case[0]}", {test_case[1]})')

            self.assertEqual(Present.weight, test_case[1], f'Value of the attribute weight should be ' +
                f'{test_case[1]}, when object is initialized as follows:\n' +
                f'Present("{test_case[0]}", {test_case[1]})')

    @points('9.box_of_presents_part2')
    def test_3_class_box_works(self):
        try:
            from src.box_of_presents import Box
            b = Box()
        except Exception as e:
            self.fail(f'Calling constructor Box() threw an error \n{e}\n')     

    @points('9.box_of_presents_part2')
    def test_4_methods_of_box(self):
        from src.box_of_presents import Box, Present
        l = Box()
        try:
            l.add_present(Present("Ball",1))
        except Exception as e:
            self.fail(f'Method call add_present(Present("Ball",1)) threw an error \n{e}')

        try:
            l.total_weight()
        except Exception as e:
            self.fail(f'Method call total_weight() threw an error\n{e}\n, when present was added ' +
                'by calling add_present(Present("Ball",1))')

    @points('9.box_of_presents_part2')
    def test_5_box_of_presents_toimii(self):
        test_cases = [("Ball", 1), ("Toy train",2), ("Bicycle", 5), 
                      ("Guitar", 3), ("Car", 2000)]
        corr = 0
        from src.box_of_presents import Box, Present
        box = Box()
        list_of_presents = ""
        for test_case in test_cases:
            present = Present(test_case[0], test_case[1])
            box.add_present(present)
            val = box.total_weight()
            corr += test_case[1]
            list_of_presents += f"\n{test_case[0]} (weight {test_case[1]})"

            self.assertEqual(corr, val, f'Total weight of box should be {corr}, when ' +
                f'the following presents have been added to the box: {list_of_presents}' +
                f'\nnow weight is {val}.')

if __name__ == '__main__':
    unittest.main()
