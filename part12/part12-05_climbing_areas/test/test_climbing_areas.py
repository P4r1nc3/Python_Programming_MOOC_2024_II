import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source, sanitize
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date, datetime, timedelta

exercise = 'src.climbing_areas'

def f(attr: list):
    return ",".join(attr)

def s(lista):
    return "\n".join(f'{r}' for r in lista)

class ClimbingAreasTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_ok(self):
        ok, line = check_source(self.module)
        message = """Code testing the functions must be located after the
if __name__ == "__main__":
block. The following line must be moved:
"""
        self.assertTrue(ok, message+line)

    @points('12.climbing_areas_part1')
    def test_1_function_sort_by_number_of_routes_exists(self):
        try:
            from src.climbing_areas import sort_by_number_of_routes
        except:
            self.fail("Your program should have a function called sort_by_number_of_routes(areas: list)")

    @points('12.climbing_areas_part1')
    def test_2_sort_by_number_of_routes_return_type(self):
        from src.climbing_areas import sort_by_number_of_routes
        from src.climbing_areas import ClimbingRoute, ClimbingArea

        code = """
k1 = ClimbingArea("Area 53")
k1.add_route(ClimbingRoute("Edge", 38, "6A+"))
k1.add_route(ClimbingRoute("Big cut", 36, "6B"))
k1.add_route(ClimbingRoute("The Swedish route", 42, "5+"))

k2 = ClimbingArea("Moor")
k2.add_route(ClimbingRoute("Syncro", 14, "8C+"))

k3 = ClimbingArea("Climbstation")
k3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
k3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
k3.add_route(ClimbingRoute("No grip", 12 , "6B+"))
k3.add_route(ClimbingRoute("Fruit garden", 8, "6A"))

sort_by_number_of_routes([k1, k2, k3])

"""

        try:
            k1 = ClimbingArea("Area 53")
            k1.add_route(ClimbingRoute("Edge", 38, "6A+"))
            k1.add_route(ClimbingRoute("Big cut", 36, "6B"))
            k1.add_route(ClimbingRoute("The Swedish route", 42, "5+"))

            k2 = ClimbingArea("Moor")
            k2.add_route(ClimbingRoute("Syncro", 14, "8C+"))

            k3 = ClimbingArea("Climbstation")
            k3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
            k3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
            k3.add_route(ClimbingRoute("No grip", 12 , "6B+"))
            k3.add_route(ClimbingRoute("Fruit garden", 8, "6A"))

            response = sort_by_number_of_routes([k1, k2, k3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        taip = str(type(response)).replace("<class '","").replace("'>","")
        self.assertTrue(type(response) == list, f"Function sort_by_number_of_routes(routes: list) should return a list, now the type of the return value was {taip}")
        self.assertTrue(len(response) == 3, f"When this code is executed {code} program should return a list with lenght of 3, now the length of the returned code was {len(response)}")
        taip = str(type(response[0])).replace("<class '","").replace("'>","")
        etaip = str(type(k1)).replace("<class '","").replace("'>","")
        self.assertTrue(type(response[0]) == type(k1),  f"When this code is executed {code}the items in the list should be of type {etaip} Now the type was {taip}")

    @points('12.climbing_areas_part1')
    def test_3_sort_by_number_of_routes_works_1(self):
        from src.climbing_areas import sort_by_number_of_routes
        from src.climbing_areas import ClimbingRoute, ClimbingArea

        code = """
k1 = ClimbingArea("Area 53")
k1.add_route(ClimbingRoute("Edge", 38, "6A+"))
k1.add_route(ClimbingRoute("Big cut", 36, "6B"))
k1.add_route(ClimbingRoute("The Swedish route", 42, "5+"))

k2 = ClimbingArea("Moor")
k2.add_route(ClimbingRoute("Syncro", 14, "8C+"))

k3 = ClimbingArea("Climbstation")
k3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
k3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
k3.add_route(ClimbingRoute("No grip", 12 , "6B+"))
k3.add_route(ClimbingRoute("Fruit garden", 8, "6A"))

sort_by_number_of_routes([k1, k2, k3])

"""

        try:
            k1 = ClimbingArea("Area 53")
            k1.add_route(ClimbingRoute("Edge", 38, "6A+"))
            k1.add_route(ClimbingRoute("Big cut", 36, "6B"))
            k1.add_route(ClimbingRoute("The Swedish route", 42, "5+"))

            k2 = ClimbingArea("Moor")
            k2.add_route(ClimbingRoute("Syncro", 14, "8C+"))

            k3 = ClimbingArea("Climbstation")
            k3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
            k3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
            k3.add_route(ClimbingRoute("No grip", 12 , "6B+"))
            k3.add_route(ClimbingRoute("Fruit garden", 8, "6A"))

            response = sort_by_number_of_routes([k1, k2, k3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = [k2, k1, k3]

        self.assertTrue(response == exp,  f"When this code is executed {code}the value returned should be \n{s(exp)}\nnow the function returned\n{s(response)}")

    @points('12.climbing_areas_part1')
    def test_4_sort_by_number_of_routes_works_2(self):
        from src.climbing_areas import sort_by_number_of_routes
        from src.climbing_areas import ClimbingRoute, ClimbingArea

        code = """
k1 = ClimbingArea("Area 53")
k1.add_route(ClimbingRoute("Edge", 38, "6A+"))
k1.add_route(ClimbingRoute("Big cut", 36, "6B"))
k1.add_route(ClimbingRoute("The Swedish route", 42, "5+"))

k2 = ClimbingArea("Moor")
k2.add_route(ClimbingRoute("Syncro", 14, "8C+"))
k2.add_route(ClimbingRoute("Tailor", 12, "8A"))

k3 = ClimbingArea("Climbstation")
k3.add_route(ClimbingRoute("Small steps", 12, "6A+"))

k4 = ClimbingArea("Rock of Jane")
k4.add_route(ClimbingRoute("Antipathy", 12, "7C"))
k4.add_route(ClimbingRoute("Wombat", 14, "6C"))
k4.add_route(ClimbingRoute("Haliba", 16, "6B"))
k4.add_route(ClimbingRoute("Old Fart Club", 21, "6A"))

sort_by_number_of_routes([k1, k2, k3, k4])

"""

        try:
            k1 = ClimbingArea("Area 53")
            k1.add_route(ClimbingRoute("Edge", 38, "6A+"))
            k1.add_route(ClimbingRoute("Big cut", 36, "6B"))
            k1.add_route(ClimbingRoute("The Swedish route", 42, "5+"))

            k2 = ClimbingArea("Moor")
            k2.add_route(ClimbingRoute("Syncro", 14, "8C+"))
            k2.add_route(ClimbingRoute("Tailor", 12, "8A"))

            k3 = ClimbingArea("Climbstation")
            k3.add_route(ClimbingRoute("Small steps", 12, "6A+"))

            k4 = ClimbingArea("Rock of Jane")
            k4.add_route(ClimbingRoute("Antipathy", 12, "7C"))
            k4.add_route(ClimbingRoute("Wombat", 14, "6C"))
            k4.add_route(ClimbingRoute("Haliba", 16, "6B"))
            k4.add_route(ClimbingRoute("Old Fart Club", 21, "6A"))

            response = sort_by_number_of_routes([k1, k2, k3, k4])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = [k3, k2, k1, k4]

        self.assertTrue(response == exp,  f"When this code is executed {code}the value returned should be \n{s(exp)}\nnow the function returned\n{s(response)}")

    @points('12.climbing_areas_part2')
    def test_5_function_sort_by_most_difficult_exists(self):
        try:
            from src.climbing_areas import sort_by_most_difficult
        except:
            self.assertTrue(False, "Your program should have a function sort_by_most_difficult(areas: list)")

    @points('12.climbing_areas_part2')
    def test_6_sort_by_most_difficult_return_type(self):
        from src.climbing_areas import sort_by_most_difficult
        from src.climbing_areas import ClimbingRoute, ClimbingArea

        code = """
k1 = ClimbingArea("Area 53")
k1.add_route(ClimbingRoute("Edge", 38, "6A+"))
k1.add_route(ClimbingRoute("Big cut", 36, "6B"))
k1.add_route(ClimbingRoute("The Swedish route", 42, "5+"))

k2 = ClimbingArea("Moor")
k2.add_route(ClimbingRoute("Syncro", 14, "8C+"))

k3 = ClimbingArea("Climbstation")
k3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
k3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
k3.add_route(ClimbingRoute("No grip", 12 , "6B+"))
k3.add_route(ClimbingRoute("Fruit garden", 8, "6A"))

sort_by_most_difficult([k1, k2, k3])

"""

        try:
            k1 = ClimbingArea("Area 53")
            k1.add_route(ClimbingRoute("Edge", 38, "6A+"))
            k1.add_route(ClimbingRoute("Big cut", 36, "6B"))
            k1.add_route(ClimbingRoute("The Swedish route", 42, "5+"))

            k2 = ClimbingArea("Moor")
            k2.add_route(ClimbingRoute("Syncro", 14, "8C+"))

            k3 = ClimbingArea("Climbstation")
            k3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
            k3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
            k3.add_route(ClimbingRoute("No grip", 12 , "6B+"))
            k3.add_route(ClimbingRoute("Fruit garden", 8, "6A"))

            response = sort_by_most_difficult([k1, k2, k3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        taip = str(type(response)).replace("<class '","").replace("'>","")
        self.assertTrue(type(response) == list, f"Function sort_by_most_difficult(routes: list) should return a list, now the type of the return value was {taip}")
        self.assertTrue(len(response) == 3, f"When this code is executed {code}program should return a list with lenght of 3, now the length of the returned code was {len(response)}")
        taip = str(type(response[0])).replace("<class '","").replace("'>","")
        etaip = str(type(k1)).replace("<class '","").replace("'>","")
        self.assertTrue(type(response[0]) == type(k1),  f"When this code is executed {code}the items in the list should be of type{etaip} Now the type was {taip}")

    @points('12.climbing_areas_part2')
    def test_7_sort_by_most_difficult_works_1(self):
        from src.climbing_areas import sort_by_most_difficult
        from src.climbing_areas import ClimbingRoute, ClimbingArea

        code = """
k1 = ClimbingArea("Area 53")
k1.add_route(ClimbingRoute("Edge", 38, "6A+"))
k1.add_route(ClimbingRoute("Big cut", 36, "6B"))
k1.add_route(ClimbingRoute("The Swedish route", 42, "5+"))

k2 = ClimbingArea("Moor")
k2.add_route(ClimbingRoute("Syncro", 14, "8C+"))

k3 = ClimbingArea("Climbstation")
k3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
k3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
k3.add_route(ClimbingRoute("No grip", 12 , "6B+"))
k3.add_route(ClimbingRoute("Fruit garden", 8, "6A"))

sort_by_most_difficult([k1, k2, k3])

"""

        try:
            k1 = ClimbingArea("Area 53")
            k1.add_route(ClimbingRoute("Edge", 38, "6A+"))
            k1.add_route(ClimbingRoute("Big cut", 36, "6B"))
            k1.add_route(ClimbingRoute("The Swedish route", 42, "5+"))

            k2 = ClimbingArea("Moor")
            k2.add_route(ClimbingRoute("Syncro", 14, "8C+"))

            k3 = ClimbingArea("Climbstation")
            k3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
            k3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
            k3.add_route(ClimbingRoute("No grip", 12 , "6B+"))
            k3.add_route(ClimbingRoute("Fruit garden", 8, "6A"))

            response = sort_by_most_difficult([k1, k2, k3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = [k2, k3, k1]

        self.assertTrue(response == exp,  f"When this code is executed {code}the value returned should be \n{s(exp)}\nnow the function returned\n{s(response)}")

    @points('12.climbing_areas_part2')
    def test_8_sort_by_most_difficult_works_2(self):
        from src.climbing_areas import sort_by_most_difficult
        from src.climbing_areas import ClimbingRoute, ClimbingArea

        code = """
k1 = ClimbingArea("Area 53")
k1.add_route(ClimbingRoute("Edge", 38, "6A+"))
k1.add_route(ClimbingRoute("Big cut", 36, "6B"))
k1.add_route(ClimbingRoute("The Swedish route", 42, "5+"))

k2 = ClimbingArea("Moor")
k2.add_route(ClimbingRoute("Syncro", 14, "8C+"))
k2.add_route(ClimbingRoute("Tailor", 12, "8A"))

k3 = ClimbingArea("Climbstation")
k3.add_route(ClimbingRoute("Small steps", 12, "6A+"))

k4 = ClimbingArea("Rock of Jane")
k4.add_route(ClimbingRoute("Antipathy", 12, "7C"))
k4.add_route(ClimbingRoute("Wombat", 14, "6C"))
k4.add_route(ClimbingRoute("Haliba", 16, "6B"))
k4.add_route(ClimbingRoute("Old Fart Club", 21, "6A"))

sort_by_most_difficult([k1, k2, k3, k4])

"""

        try:
            k1 = ClimbingArea("Area 53")
            k1.add_route(ClimbingRoute("Edge", 38, "6A+"))
            k1.add_route(ClimbingRoute("Big cut", 36, "6B"))
            k1.add_route(ClimbingRoute("The Swedish route", 42, "5+"))

            k2 = ClimbingArea("Moor")
            k2.add_route(ClimbingRoute("Syncro", 14, "8C+"))
            k2.add_route(ClimbingRoute("Tailor", 12, "8A"))

            k3 = ClimbingArea("Climbstation")
            k3.add_route(ClimbingRoute("Small steps", 12, "6A+"))

            k4 = ClimbingArea("Rock of Jane")
            k4.add_route(ClimbingRoute("Antipathy", 12, "7C"))
            k4.add_route(ClimbingRoute("Wombat", 14, "6C"))
            k4.add_route(ClimbingRoute("Haliba", 16, "6B"))
            k4.add_route(ClimbingRoute("Old Fart Club", 21, "6A"))

            response = sort_by_most_difficult([k1, k2, k3, k4])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = [k2, k4, k1, k3]

        self.assertTrue(response == exp,  f"When this code is executed {code}the value returned should be \n{s(exp)}\nnow the function returned\n{s(response)}")


if __name__ == '__main__':
    unittest.main()