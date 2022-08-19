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

exercise = 'src.climbing_route'
classname = "ClimbingRoute"

def f(attr: list):
    return ",".join(attr)

def s(lista):
    return "\n".join(f'{r}' for r in lista)

class ClimbingRouteTest(unittest.TestCase):
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

    @points('12.climbing_route_part1')
    def test_1_function_by_length_exists(self):
        try:
            from src.climbing_route import sort_by_length
        except:
            self.fail("Your program should have a function sort_by_length(reitit: list)")

    @points('12.climbing_route_part1')
    def test_2_sort_by_length_return_type(self):
        from src.climbing_route import sort_by_length
        from src.climbing_route import ClimbingRoute

        code = """
r1 = ClimbingRoute("Edge", 38, "6A+")
r2 = ClimbingRoute("Smooth operator", 9, "7A")
r3 = ClimbingRoute("Syncro", 14, "8C+")
sort_by_length([r1, r2, r3])

"""

        try:
            r1 = ClimbingRoute("Edge", 38, "6A+")
            r2 = ClimbingRoute("Smooth operator", 9, "7A")
            r3 = ClimbingRoute("Syncro", 14, "8C+")
            reply = sort_by_length([r1, r2, r3])
        except:
            self.fail(f"Make sure that the following code can be executed\n{code}")

        taip = str(type(reply)).replace("<class '","").replace("'>","")
        self.assertTrue(type(reply) == list, f"Function sort_by_length(reitit: list) should return a list, now the type of the return value was {taip}")
        self.assertTrue(len(reply) == 3, f"When this code is executed: {code}a list with length of 3 should be returned, now the length was {len(reply)}")
        taip = str(type(reply[0])).replace("<class '","").replace("'>","")
        etaip = str(type(r1)).replace("<class '","").replace("'>","")
        self.assertTrue(type(reply[0]) == type(r1),  f"When this code is executed {code}the items in the returned list should be of type {etaip} now their type was {taip}")

    @points('12.climbing_route_part1')
    def test_3_sort_by_length_works_1(self):
        from src.climbing_route import sort_by_length
        from src.climbing_route import ClimbingRoute

        code = """
r1 = ClimbingRoute("Edge", 38, "6A+")
r2 = ClimbingRoute("Smooth operator", 9, "7A")
r3 = ClimbingRoute("Syncro", 14, "8C+")
sort_by_length([r1, r2, r3])

"""

        try:
            r1 = ClimbingRoute("Edge", 38, "6A+")
            r2 = ClimbingRoute("Smooth operator", 9, "7A")
            r3 = ClimbingRoute("Syncro", 14, "8C+")
            reply = sort_by_length([r1, r2, r3])
        except:
            self.fail(f"Make sure that the following code can be executed\n{code}")

        exp = [r1, r3, r2]

        self.assertTrue(reply == exp,  f"When this code is executed {code}the following routes should be returned \n{s(exp)}\nNow the function returned\n{s(reply)}")

    @points('12.climbing_route_part1')
    def test_4_sort_by_length_works_2(self):
        from src.climbing_route import sort_by_length
        from src.climbing_route import ClimbingRoute

        code = """
r1 = ClimbingRoute("Edge", 38, "6A+")
r2 = ClimbingRoute("Smooth operator", 9, "7A")
r3 = ClimbingRoute("Syncro", 14, "8C+")
r4 = ClimbingRoute("Big cut", 36, "6B")
r5 = ClimbingRoute("Fruit garden", 8, "6A")
r6 = ClimbingRoute("No grip", 12 , "6B+")
r7 = ClimbingRoute("Small steps", 13, "6A+")
sort_by_length([r1, r2, r3, r4, r5, r6, r7])

"""

        try:
            r1 = ClimbingRoute("Edge", 38, "6A+")
            r2 = ClimbingRoute("Smooth operator", 9, "7A")
            r3 = ClimbingRoute("Syncro", 14, "8C+")
            r4 = ClimbingRoute("Big cut", 36, "6B")
            r5 = ClimbingRoute("Fruit garden", 8, "6A")
            r6 = ClimbingRoute("No grip", 12 , "6B+")
            r7 = ClimbingRoute("Small steps", 13, "6A+")
            reply = sort_by_length([r1, r2, r3, r4, r5, r6, r7])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = [r1, r4, r3, r7, r6, r2, r5]

        self.assertTrue(reply == exp,  f"When the following code is executed{code}the following routes should be returned\n{s(exp)}\nNow the function returns\n{s(reply)}")

    @points('12.climbing_route_part2')
    def test_5_funktio_sort_by_difficulty_olemassa(self):
        try:
            from src.climbing_route import sort_by_difficulty
        except:
            self.fail("Ohjelmastasi pitäisi löytyä funktio nimeltä sort_by_difficulty(reitit: list)")

    @points('12.climbing_route_part2')
    def test_6_sort_by_difficulty_return_type(self):
        from src.climbing_route import sort_by_difficulty
        from src.climbing_route import ClimbingRoute

        climbing_route = """
r1 = ClimbingRoute("Edge", 38, "6A+")
r2 = ClimbingRoute("Smooth operator", 9, "7A")
r3 = ClimbingRoute("Syncro", 14, "8C+")
sort_by_difficulty([r1, r2, r3])

"""

        try:
            r1 = ClimbingRoute("Edge", 38, "6A+")
            r2 = ClimbingRoute("Smooth operator", 9, "7A")
            r3 = ClimbingRoute("Syncro", 14, "8C+")
            reply = sort_by_difficulty([r1, r2, r3])
        except:
            self.fail(f"Check that the following code can be executed\n{climbing_route}")

        taip = str(type(reply)).replace("<class '","").replace("'>","")
        self.assertTrue(type(reply) == list, f"Funktion sort_by_difficulty(reitit: list) tulee palauttaa lista, nyt palautettu arvo oli tyypiltään {taip}")
        self.assertTrue(len(reply) == 3, f"When the following code is executed{climbing_route}tulee palauttaa listan jonka pituus on 3, nyt palautetun listan pituus oli {len(reply)}")
        taip = str(type(reply[0])).replace("<class '","").replace("'>","")
        etaip = str(type(r1)).replace("<class '","").replace("'>","")
        self.assertTrue(type(reply[0]) == type(r1),  f"When the following code is executed{climbing_route}palautetun listan alkioiden tulee olla tyypiltään {etaip} nyt niiden tyyppi on {taip}")

    @points('12.climbing_route_part2')
    def test_7_sort_by_difficulty_works_1(self):
        from src.climbing_route import sort_by_difficulty
        from src.climbing_route import ClimbingRoute

        climbing_route = """
r1 = ClimbingRoute("Edge", 38, "6A+")
r2 = ClimbingRoute("Smooth operator", 9, "7A")
r3 = ClimbingRoute("Syncro", 14, "8C+")
sort_by_difficulty([r1, r2, r3])

"""

        try:
            r1 = ClimbingRoute("Edge", 38, "6A+")
            r2 = ClimbingRoute("Smooth operator", 9, "7A")
            r3 = ClimbingRoute("Syncro", 14, "8C+")
            reply = sort_by_difficulty([r1, r2, r3])
        except:
            self.fail(f"Check that the following code can be executed\n{climbing_route}")

        exp = [r3, r2, r1]

        self.assertTrue(reply == exp,  f"When the following code is executed{climbing_route}the following routes should be returned\n{s(exp)}\nNow the function returns\n{s(reply)}")

    @points('12.climbing_route_part2')
    def test_8_sort_by_difficulty_works_2(self):
        from src.climbing_route import sort_by_difficulty
        from src.climbing_route import ClimbingRoute

        climbing_route = """
r1 = ClimbingRoute("Small steps", 13, "6A+")
r2 = ClimbingRoute("Edge", 38, "6A+")
r3 = ClimbingRoute("Bukowski", 9, "6A+")
reply = sort_by_difficulty([r1, r2, r3])

"""

        try:
            r1 = ClimbingRoute("Small steps", 13, "6A+")
            r2 = ClimbingRoute("Edge", 38, "6A+")
            r3 = ClimbingRoute("Bukowski", 9, "6A+")
            reply = sort_by_difficulty([r1, r2, r3])
        except:
            self.fail(f"Check that the following code can be executed\n{climbing_route}")

        exp = [r2, r1, r3]

        self.assertTrue(reply == exp,  f"When the following code is executed{climbing_route}the following routes should be returned\n{s(exp)}\nNow the function returns\n{s(reply)}")


    @points('12.climbing_route_part2')
    def test_9_sort_by_difficulty_works_3(self):
        from src.climbing_route import sort_by_difficulty
        from src.climbing_route import ClimbingRoute

        climbing_route = """
r1 = ClimbingRoute("Edge", 38, "6A+")
r2 = ClimbingRoute("Smooth operator", 9, "7A")
r3 = ClimbingRoute("Syncro", 14, "8C+")
r4 = ClimbingRoute("Big cut", 36, "6B")
r5 = ClimbingRoute("Fruit garden", 8, "6A")
r6 = ClimbingRoute("No grip", 12 , "6B+")
r7 = ClimbingRoute("Small steps", 13, "6A+")
r8 = ClimbingRoute("The Swedish route", 42, "5+")
sort_by_difficulty([r1, r2, r3, r4, r5, r6, r7, r8])

"""

        try:
            r1 = ClimbingRoute("Edge", 38, "6A+")
            r2 = ClimbingRoute("Smooth operator", 9, "7A")
            r3 = ClimbingRoute("Syncro", 14, "8C+")
            r4 = ClimbingRoute("Big cut", 36, "6B")
            r5 = ClimbingRoute("Fruit garden", 8, "6A")
            r6 = ClimbingRoute("No grip", 12 , "6B+")
            r7 = ClimbingRoute("Small steps", 13, "6A+")
            r8 = ClimbingRoute("The Swedish route", 42, "5+")
            reply = sort_by_difficulty([r1, r2, r3, r4, r5, r6, r7, r8])
        except:
            self.fail(f"Check that the following code can be executed\n{climbing_route}")

        exp = [r3, r2, r6, r4, r1, r7, r5, r8]

        self.assertTrue(reply == exp,  f"When the following code is executed{climbing_route}the following routes should be returned\n{s(exp)}\nNow the function returns\n{s(reply)}")


if __name__ == '__main__':
    unittest.main()
