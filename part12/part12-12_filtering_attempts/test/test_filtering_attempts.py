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

exercise = 'src.filtering_attempts'

def f(attr: list):
    return ",".join(attr)

def s(response):
    output = ""
    for n in response:
        output += f"{n}\n"
    return output

class FilteringAttemptstTest(unittest.TestCase):
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

    @points('12.filtering_attempts_part1')
    def test_01_function_accepted_exists(self):
        try:
            from src.filtering_attempts import accepted
        except:
            self.fail("Your program should have a function called accepted(attempts: list)")

    @points('12.filtering_attempts_part1')
    def test_2_accepted_return_type(self):
        from src.filtering_attempts import accepted
        from src.filtering_attempts import CourseAttempt

        code = """
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced programming", 0)
accepted([s1, s2, s3])
"""

        try:
            s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
            s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
            s3 = CourseAttempt("Peter Python", "Advanced programming", 0)
            response = accepted([s1, s2, s3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        m = filter(None, [])
        taip = str(type(response)).replace("<class '","").replace("'>","")
        self.assertTrue(type(response) == type(m) or type(response) == list, f"Function accepted(courses: list) must return filter or list, now the type of the return value was {taip}")
        for item in response:
            etaip = str(type(s2)).replace("<class '","").replace("'>","").replace("src.filtering_attempts.", "")
            taip = str(type(item)).replace("<class '","").replace("'>","")
            self.assertTrue(type(item) == type(s2),  f"When this code is executed: {code}returned items should be of type {etaip} now the type is{taip}")
             
    @points('12.filtering_attempts_part1')
    def test_03_accepted_works_1(self):
        from src.filtering_attempts import accepted
        from src.filtering_attempts import CourseAttempt

        code = """
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced programming", 0)
accepted([s1, s2, s3])
"""

        try:
            s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
            s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
            s3 = CourseAttempt("Peter Python", "Advanced programming", 0)
            response = accepted([s1, s2, s3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = [ s1, s2 ]

        output = ""
        vast = []
        for n in response:
            output += f"{n}\n"
            vast.append(n)

        def nimi(s):
            return s.course_name

        self.assertEquals(sorted(vast, key=nimi), sorted(exp,key=nimi),  f"When this code is executed: {code}should return \n{s(exp)}\nfunction returned\n{output}")

    @points('12.filtering_attempts_part1')
    def test_04_accepted_filter_used(self):
        src_file = os.path.join('src', 'filtering_attempts.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def accepted"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def attempts_with_grade" in line or "def passed_students" in line):
                    p = False 
                elif p:
                    lines.append(line)

        required = [
            "filter(",
        ]

        for v in required:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"Function accepted(attempts: list) must use the filter function!")          

    @points('12.filtering_attempts_part1')
    def test_05_accepted_works_2(self):
        from src.filtering_attempts import accepted
        from src.filtering_attempts import CourseAttempt

        code = """
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced programming", 0)
s4 = CourseAttempt("Hector Helastic", "Introduction to Programming", 3)
s5 = CourseAttempt("Lady Gaga", "Introduction to Programming", 0)
s6 = CourseAttempt("Eila Karkki", "Advanced programming", 2)

accepted([s1, s2, s3, s4, s5, s6])
"""

        try:
            s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
            s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
            s3 = CourseAttempt("Peter Python", "Advanced programming", 0)
            s4 = CourseAttempt("Hector Helastic", "Introduction to Programming", 3)
            s5 = CourseAttempt("Lady Gaga", "Introduction to Programming", 0)
            s6 = CourseAttempt("Eila Karkki", "Advanced programming", 2)

            response = accepted([s1, s2, s3, s4, s5, s6])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = [s1, s2, s4, s6]

        output = ""
        vast = []
        for n in response:
            output += f"{n}\n"
            vast.append(n)

        def nimi(s):
            return s.course_name

        self.assertEquals(sorted(vast, key=nimi), sorted(exp,key=nimi),  f"When this code is executed: {code}should return \n{s(exp)}\nfunction returned\n{output}")

    @points('12.filtering_attempts_part2')
    def test_06_function_attempts_with_grade_exists(self):
        try:
            from src.filtering_attempts import attempts_with_grade
        except:
            self.assertTrue(False, "Your program should have a function called attempts_with_grade(attempts: list, grade: int) ")

    @points('12.filtering_attempts_part2')
    def test_07_attempts_with_grade_tyyppi(self):
        from src.filtering_attempts import attempts_with_grade
        from src.filtering_attempts import CourseAttempt

        code = """
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced programming", 3)
attempts_with_grade([s1, s2, s3], 3)
"""

        try:
            s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
            s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
            s3 = CourseAttempt("Peter Python", "Advanced programming", 3)
            response = attempts_with_grade([s1, s2, s3], 3)
            
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        m = filter(None, [])
        taip = str(type(response)).replace("<class '","").replace("'>","")
        self.assertTrue(type(response) == type(m) or type(response) == list, f"Function attempts_with_grade(courses: list, grade: int) must return filter or list, now the type of the return value was {taip}")
        for item in response:
            etaip = str(type(s2)).replace("<class '","").replace("'>","").replace("src.filtering_attempts.", "")
            taip = str(type(item)).replace("<class '","").replace("'>","")
            self.assertTrue(type(item) == type(s2),  f"When this code is executed: {code}returned items should be of type {etaip} now the type is{taip}")
            
    @points('12.filtering_attempts_part2')
    def test_08_attempts_with_grade_works_1(self):
        from src.filtering_attempts import attempts_with_grade
        from src.filtering_attempts import CourseAttempt

        code = """
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced programming", 3)
attempts_with_grade([s1, s2, s3], 3)
"""

        try:
            s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
            s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
            s3 = CourseAttempt("Peter Python", "Advanced programming", 3)
            response = attempts_with_grade([s1, s2, s3], 3)
            
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = [ s1, s3 ]

        output = ""
        vast = []
        for n in response:
            output += f"{n}\n"
            vast.append(n)

        def nimi(s):
            return s.course_name

        self.assertEquals(sorted(vast, key=nimi), sorted(exp,key=nimi),  f"When this code is executed: {code}should return \n{s(exp)}\nfunction returned\n{output}")

    @points('12.filtering_attempts_part2')
    def test_09_attempts_with_grade_filter_used(self):
        src_file = os.path.join('src', 'filtering_attempts.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def attempts_with_grade"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def accepted" in line or "def passed_students" in line): 
                    p = False 
                elif p:
                    lines.append(line)

        required = [
            "filter(",
        ]

        for v in required:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"Function attempts_with_grade(courses: list, grade: int) must use the filter function!")          

    @points('12.filtering_attempts_part2')
    def test_10_attempts_with_grade_works_2(self):
        from src.filtering_attempts import attempts_with_grade
        from src.filtering_attempts import CourseAttempt

        code = """
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced programming", 0)
s4 = CourseAttempt("Hector Helastic", "Introduction to Programming", 3)
s5 = CourseAttempt("Lady Gaga", "Introduction to Programming", 0)
s6 = CourseAttempt("Eila Karkki", "Advanced programming", 3)

attempts_with_grade([s1, s2, s3, s4, s5, s6].)
"""

        try:
            s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
            s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
            s3 = CourseAttempt("Peter Python", "Advanced programming", 0)
            s4 = CourseAttempt("Hector Helastic", "Introduction to Programming", 3)
            s5 = CourseAttempt("Lady Gaga", "Introduction to Programming", 0)
            s6 = CourseAttempt("Eila Karkki", "Advanced programming", 3)

            response = attempts_with_grade([s1, s2, s3, s4, s5, s6], 3)
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = [s1, s4, s6]

        output = ""
        vast = []
        for n in response:
            output += f"{n}\n"
            vast.append(n)

        def nimi(s):
            return s.course_name

        self.assertEquals(sorted(vast, key=nimi), sorted(exp,key=nimi),  f"When this code is executed: {code}should return \n{s(exp)}\nfunction returned\n{output}")


    @points('12.filtering_attempts_part3')
    def test_11_function_passed_students_exists(self):
        try:
            from src.filtering_attempts import passed_students
        except:
            self.assertTrue(False, "Your program should have a function called passed_students(attempts: list, course_name: str) ")

    @points('12.filtering_attempts_part3')
    def test_12_passed_students_tyyppi(self):
        from src.filtering_attempts import passed_students
        from src.filtering_attempts import CourseAttempt

        code = """
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced programming", 3)
s4 = CourseAttempt("Niles Nerd", "Networking", 3)
passed_students([s1, s2, s3, s4], "Introduction to Programming")

"""

        try:
            s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
            s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
            s3 = CourseAttempt("Peter Python", "Advanced programming", 3)
            s4 = CourseAttempt("Niles Nerd", "Networking", 3)
            response = passed_students([s1, s2, s3, s4], "Introduction to Programming")
            
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        m = filter(None, [])
        m2 = map(None, [])
        taip = str(type(response)).replace("<class '","").replace("'>","")
        self.assertTrue(type(response) == type(m2) or type(response) == type(m) or type(response) == list, f"Function attempts_with_grade(courses: list, grade: int) must return filter or list, now the type of the return value was {taip}")
        for item in response:
            etaip = "str"
            taip = str(type(item)).replace("<class '","").replace("'>","")
            self.assertTrue(type(item) == type(""),  f"When this code is executed: {code}returned items should be of type {etaip} now the type is{taip}")
            
    @points('12.filtering_attempts_part3')
    def test_13_passed_students_works_1(self):
        from src.filtering_attempts import passed_students
        from src.filtering_attempts import CourseAttempt

        code = """
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced programming", 3)
s4 = CourseAttempt("Niles Nerd", "Networking", 3)
passed_students([s1, s2, s3, s4], "Introduction to Programming")

"""

        try:
            s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
            s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
            s3 = CourseAttempt("Peter Python", "Advanced programming", 3)
            s4 = CourseAttempt("Niles Nerd", "Networking", 3)
            response = passed_students([s1, s2, s3, s4], "Introduction to Programming")
            
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = ["Paula Programmer", "Peter Python"]

        output = ""
        vast = []
        for n in response:
            output += f"{n}\n"
            vast.append(n)

        self.assertEquals(vast, exp,  f"When this code is executed: {code}should return \n{s(exp)}\nfunction returned\n{output}")

    @points('12.filtering_attempts_part3')
    def test_14_passed_students_map_ja_filter_used(self):
        src_file = os.path.join('src', 'filtering_attempts.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def passed_students"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def attempts_with_grade" in line or "def accepted" in line):
                    p = False 
                elif p:
                    lines.append(line)

        required = [
            "filter(",
            "map"
        ]

        for v in required:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"Function passed_students(attempts: list, course_name: str) must use map and filter functions!")          

    @points('12.filtering_attempts_part3')
    def test_15_passed_students_works_2(self):
        from src.filtering_attempts import passed_students
        from src.filtering_attempts import CourseAttempt

        code = """
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Yomi Cosa", "Networking", 5)
s3 = CourseAttempt("Peter Python", "Data Structures", 2)
s4 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
s5 = CourseAttempt("Peter Python", "Advanced programming", 3)
s6 = CourseAttempt("Niles Nerd", "Networking", 3)
s7 = CourseAttempt("Peter Python", "Networking", 0)
passed_students([s1, s2, s3, s4, s5, s6, s7], "Networking")

"""

        try:
            s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
            s2 = CourseAttempt("Yomi Cosa", "Networking", 5)
            s3 = CourseAttempt("Peter Python", "Data Structures", 2)
            s4 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
            s5 = CourseAttempt("Peter Python", "Advanced programming", 3)
            s6 = CourseAttempt("Niles Nerd", "Networking", 3)
            s7 = CourseAttempt("Peter Python", "Networking", 0)
            response = passed_students([s1, s2, s3, s4, s5, s6, s7], "Networking")
            
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = ["Niles Nerd", "Yomi Cosa"]

        output = ""
        vast = []
        for n in response:
            output += f"{n}\n"
            vast.append(n)

        self.assertEquals(vast, exp,  f"When this code is executed: {code}should return \n{s(exp)}\nfunction returned\n{output}")


if __name__ == '__main__':
    unittest.main()
