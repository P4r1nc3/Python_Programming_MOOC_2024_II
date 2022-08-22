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

exercise = 'src.credits'

def f(attr: list):
    return ",".join(attr)

def s(response):
    output = ""
    for n in response:
        output += f"{n}\n"
    return output

class CreditsTest(unittest.TestCase):
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

    @points('12.credits_part1')
    def test_01_function_sum_of_all_credits_exists(self):
        try:
            from src.credits import sum_of_all_credits
        except:
            self.fail("Your program should have a function called sum_of_all_credits(attempts: list)")

    @points('12.credits_part1')
    def test_02_hsum_of_all_credits_type(self):
        from src.credits import sum_of_all_credits
        from src.credits import CourseAttempt

        code = """
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Programming Course", 4, 5)
s3 = CourseAttempt("Algorithms", 3, 10)
sum_of_all_credits([s1, s2, s3])
"""

        try:
            s1 = CourseAttempt("Introduction to Programming", 5, 5)
            s2 = CourseAttempt("Advanced Programming Course", 4, 5)
            s3 = CourseAttempt("Algorithms", 3, 10)
            response = sum_of_all_credits([s1, s2, s3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        taip = str(type(response)).replace("<class '","").replace("'>","")
        self.assertTrue(type(response) == int, f"Function sum_of_all_credits(courses: list) should return int, now the type of the return value was {taip}")

    @points('12.credits_part1')
    def test_03_sum_of_all_credits_works_1(self):
        from src.credits import sum_of_all_credits
        from src.credits import CourseAttempt

        code = """
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Programming Course", 4, 5)
s3 = CourseAttempt("Algorithms", 3, 10)
sum_of_all_credits([s1, s2, s3])
"""

        try:
            s1 = CourseAttempt("Introduction to Programming", 5, 5)
            s2 = CourseAttempt("Advanced Programming Course", 4, 5)
            s3 = CourseAttempt("Algorithms", 3, 10)
            response = sum_of_all_credits([s1, s2, s3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = 20

        self.assertEquals(response, exp,  f"When this code is executed {code}it should return\n{exp}\nNow the function returns\n{response}")

    @points('12.credits_part1')
    def test_04_sum_of_credits_reduce_used(self):
        src_file = os.path.join('src', 'credits.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def sum_of_all_credits"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def sum_of_passed_credits" in line or "def average" in line):
                    p = False 
                elif p:
                    lines.append(line)

        required = [
            "reduce(",
        ]

        for v in required:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"Function sum_of_all_credits(courses: list) must use reduce!")          

    @points('12.credits_part1')
    def test_05_sum_of_all_credits_works_2(self):
        from src.credits import sum_of_all_credits
        from src.credits import CourseAttempt

        code = """
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Programming Course", 4, 5)
s3 = CourseAttempt("Algorithms", 3, 10)
s4 = CourseAttempt("Full stack", 4, 8)
s5 = CourseAttempt("DevOps with Docker", 5, 3)
s6 = CourseAttempt("Language Studies", 0, 2)
sum_of_all_credits([s1, s2, s3, s4, s5, s6])
"""

        try:
            s1 = CourseAttempt("Introduction to Programming", 5, 5)
            s2 = CourseAttempt("Advanced Programming Course", 4, 5)
            s3 = CourseAttempt("Algorithms", 3, 10)
            s4 = CourseAttempt("Full stack", 4, 8)
            s5 = CourseAttempt("DevOps with Docker", 5, 3)
            s6 = CourseAttempt("Language Studies", 0, 2)
            response = sum_of_all_credits([s1, s2, s3, s4, s5, s6])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = 33

        self.assertEquals(response, exp,  f"When this code is executed {code}it should return\n{exp}\nNow the function returns\n{response}")

    @points('12.credits_part2')
    def test_06_function_sum_of_passed_credits_exists(self):
        try:
            from src.credits import sum_of_passed_credits
        except:
            self.fail("Your program should have a function called sum_of_passed_credits(attempts: list)")

    @points('12.credits_part2')
    def test_07_sum_of_passed_credits_type(self):
        from src.credits import sum_of_passed_credits
        from src.credits import CourseAttempt

        code = """
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Programming Course", 4, 5)
s3 = CourseAttempt("Algorithms", 3, 0)
sum_of_all_credits([s1, s2, s3])
"""

        try:
            s1 = CourseAttempt("Introduction to Programming", 5, 5)
            s2 = CourseAttempt("Advanced Programming Course", 4, 5)
            s3 = CourseAttempt("Algorithms", 3, 10)
            response = sum_of_passed_credits([s1, s2, s3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        taip = str(type(response)).replace("<class '","").replace("'>","")
        self.assertTrue(type(response) == int, f"Function sum_of_passed_credits(courses: list) should return int, now the type of the return value was {taip}")

    @points('12.credits_part2')
    def test_08_sum_of_passed_credits_works_1(self):
        from src.credits import sum_of_passed_credits
        from src.credits import CourseAttempt

        code = """
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Programming Course", 4, 5)
s3 = CourseAttempt("Algorithms", 0, 10)
sum_of_passed_credits([s1, s2, s3])
"""

        try:
            s1 = CourseAttempt("Introduction to Programming", 5, 5)
            s2 = CourseAttempt("Advanced Programming Course", 4, 5)
            s3 = CourseAttempt("Algorithms", 0, 10)
            response = sum_of_passed_credits([s1, s2, s3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = 10

        self.assertEquals(response, exp,  f"When this code is executed {code}it should return\n{exp}\nNow the function returns\n{response}")


    @points('12.credits_part2')
    def test_09_sum_of_credits_reduce_used(self):
        src_file = os.path.join('src', 'credits.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def sum_of_passed_credits"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def sum_of_all_credits" in line or "def average" in line):
                    p = False 
                elif p:
                    lines.append(line)

        required = [
            "reduce(",
            "filter"
        ]

        for v in required:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"Function sum_of_passed_credits(courses: list) should use reduce and filter!")          

    @points('12.credits_part2')
    def test_10_sum_of_passed_credits_works_2(self):
        from src.credits import sum_of_passed_credits
        from src.credits import CourseAttempt

        code = """
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Programming Course", 4, 5)
s3 = CourseAttempt("Algorithms", 0, 10)
s4 = CourseAttempt("Full stack", 4, 8)
s5 = CourseAttempt("DevOps with Docker", 5, 3)
s6 = CourseAttempt("Language Studies", 0, 2)
sum_of_passed_credits([s1, s2, s3, s4, s5, s6])
"""

        try:
            s1 = CourseAttempt("Introduction to Programming", 5, 5)
            s2 = CourseAttempt("Advanced Programming Course", 4, 5)
            s3 = CourseAttempt("Algorithms", 0, 10)
            s4 = CourseAttempt("Full stack", 4, 8)
            s5 = CourseAttempt("DevOps with Docker", 5, 3)
            s6 = CourseAttempt("Language Studies", 0, 2)
            response = sum_of_passed_credits([s1, s2, s3, s4, s5, s6])
            
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = 21

        self.assertEquals(response, exp,  f"When this code is executed {code}it should return\n{exp}\nNow the function returns\n{response}")

    @points('12.credits_part3')
    def test_11_function_average_exists(self):
        try:
            from src.credits import average
        except:
            self.fail("Your program should have a function called average(attempts: list)")

    @points('12.credits_part3')
    def test_12_average_type(self):
        from src.credits import average
        from src.credits import CourseAttempt

        code = """
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Programming Course", 4, 5)
s3 = CourseAttempt("Algorithms", 3, 0)
average([s1, s2, s3])
"""

        try:
            s1 = CourseAttempt("Introduction to Programming", 5, 5)
            s2 = CourseAttempt("Advanced Programming Course", 4, 5)
            s3 = CourseAttempt("Algorithms", 3, 10)
            response = average([s1, s2, s3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        taip = str(type(response)).replace("<class '","").replace("'>","")
        self.assertTrue(type(response) == float or type(response) == int, f"Function average(courses: list) should return int tai float, now the type of the return value was {taip}")

    @points('12.credits_part3')
    def test_13_average_works_1(self):
        from src.credits import average
        from src.credits import CourseAttempt

        code = """
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Programming Course", 4, 5)
s3 = CourseAttempt("Algorithms", 3, 10)
average([s1, s2, s3])
"""

        try:
            s1 = CourseAttempt("Introduction to Programming", 5, 5)
            s2 = CourseAttempt("Advanced Programming Course", 4, 5)
            s3 = CourseAttempt("Algorithms", 3, 10)
            response = average([s1, s2, s3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = 4

        self.assertEquals(response, exp,  f"When this code is executed {code}it should return\n{exp}\nNow the function returns\n{response}")

    @points('12.credits_part3')
    def test_14_sum_of_credits_reduce_used(self):
        src_file = os.path.join('src', 'credits.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def average"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def sum_of_all_credits" in line or "def sum_of_passed_credits" in line):
                    p = False 
                elif p:
                    lines.append(line)

        required = [
            "reduce(",
            "filter"
        ]

        for v in required:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"Function average(courses: list) should use reduce and filter!")          

    @points('12.credits_part3')
    def test_15_average_works_2(self):
        from src.credits import average
        from src.credits import CourseAttempt

        code = """
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Programming Course", 4, 5)
s3 = CourseAttempt("Algorithms", 0, 10)
average([s1, s2, s3])
"""

        try:
            s1 = CourseAttempt("Introduction to Programming", 5, 5)
            s2 = CourseAttempt("Advanced Programming Course", 4, 5)
            s3 = CourseAttempt("Algorithms", 0, 10)
            response = average([s1, s2, s3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = 4.5

        self.assertEquals(response, exp,  f"When this code is executed {code}it should return\n{exp}\nNow the function returns\n{response}")

    @points('12.credits_part3')
    def test_16_average_works_2(self):
        from src.credits import average
        from src.credits import CourseAttempt

        code = """
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Programming Course", 4, 5)
s3 = CourseAttempt("Algorithms", 3, 10)
s4 = CourseAttempt("Full stack", 4, 8)
s5 = CourseAttempt("DevOps with Docker", 5, 3)
s6 = CourseAttempt("Language Studies", 0, 2)
average([s1, s2, s3, s4, s5, s6])
"""

        try:
            s1 = CourseAttempt("Introduction to Programming", 5, 5)
            s2 = CourseAttempt("Advanced Programming Course", 4, 5)
            s3 = CourseAttempt("Algorithms", 3, 10)
            s4 = CourseAttempt("Full stack", 4, 8)
            s5 = CourseAttempt("DevOps with Docker", 5, 3)
            s6 = CourseAttempt("Language Studies", 0, 2)            
            response = average([s1, s2, s3, s4, s5, s6])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = 4.2

        self.assertEquals(response, exp,  f"When this code is executed {code}it should return\n{exp}\nNow the function returns\n{response}")


if __name__ == '__main__':
    unittest.main()
