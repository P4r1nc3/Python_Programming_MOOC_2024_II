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

exercise = 'src.attempted_courses'

def f(attr: list):
    return ",".join(attr)

def s(response):
    output = ""
    for n in response:
        output += n + "\n"
    return output

class AttemptedCoursesTest(unittest.TestCase):
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

    @points('12.attempted_courses_part1')
    def test_01_function_names_of_students_exists(self):
        try:
            from src.attempted_courses import names_of_students
        except:
            self.fail("Your program should have a function called names_of_students(attempts: list)")

    @points('12.attempted_courses_part1')
    def test_02_course_names_return_type(self):
        from src.attempted_courses import names_of_students
        from src.attempted_courses import CourseAttempt

        code = """
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Programming", 2)
course_names([s1, s2, s3])
"""

        try:
            s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
            s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
            s3 = CourseAttempt("Peter Python", "Advanced Programming", 2)
            response = names_of_students([s1, s2, s3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        m = map(None, [])
        taip = str(type(response)).replace("<class '","").replace("'>","")
        self.assertTrue(type(response) == type(m) or type(response) == list, f"Function names_of_students(students: list) should return map or list, now the return value was of type {taip}")
        for alkio in response:
            etaip = str(type("")).replace("<class '","").replace("'>","")
            taip = str(type(alkio)).replace("<class '","").replace("'>","")
            self.assertTrue(type(alkio) == type(""),  f"When this code is executed {code}the values returned should be of type {etaip} now the type is {taip}")
             
    @points('12.attempted_courses_part1')
    def test_03_names_of_students_works_1(self):
        from src.attempted_courses import names_of_students
        from src.attempted_courses import CourseAttempt

        code = """
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Programming", 2)
course_names([s1, s2, s3])
"""

        try:
            s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
            s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
            s3 = CourseAttempt("Peter Python", "Advanced Programming", 2)
            response = names_of_students([s1, s2, s3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = [ s.student_name for s in [s1, s2, s3]]

        output = ""
        vast = []
        for n in response:
            output += n + "\n"
            vast.append(n)

        self.assertEquals(sorted(vast), sorted(exp),  f"When this code is executed {code}it should retunrn \n{s(exp)}\nnow the function returns\n{output}")

    @points('12.attempted_courses_part1')
    def test_04_names_of_students_map_used(self):
        src_file = os.path.join('src', 'attempted_courses.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def names_of_students"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def names_of_students" in line):
                    p = False 
                elif p:
                    lines.append(line)

        on = False
        for line in lines:
            if "map" in line:
                on = True              
        self.assertTrue(on, f"Function names_of_students(attempts: list) must use map!")   

    @points('12.attempted_courses_part1')
    def test_05_names_of_students_works_2(self):
        from src.attempted_courses import names_of_students
        from src.attempted_courses import CourseAttempt

        code = """
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Programming", 2)
s4 = CourseAttempt("Hector Helastic", "Introduction to Programming", 3)
s5 = CourseAttempt("Lady Gaga", "Introduction to Programming", 5)
s6 = CourseAttempt("Eila Karkki", "Advanced Programming", 2)

course_names([s1, s2, s3, s4, s5, s6])
"""

        try:
            s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
            s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
            s3 = CourseAttempt("Peter Python", "Advanced Programming", 2)
            s4 = CourseAttempt("Hector Helastic", "Introduction to Programming", 3)
            s5 = CourseAttempt("Lady Gaga", "Introduction to Programming", 5)
            s6 = CourseAttempt("Eila Karkki", "Advanced Programming", 2)

            response = names_of_students([s1, s2, s3, s4, s5, s6])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = [ s.student_name for s in [s1, s2, s3, s4, s5, s6]]

        output = ""
        vast = []
        for n in response:
            output += n + "\n"
            vast.append(n)

        self.assertEquals(sorted(vast), sorted(exp),  f"When this code is executed {code}it should retunrn \n{s(exp)}\nnow the function returns\n{output}")

    @points('12.attempted_courses_part2')
    def test_06_function_course_names_exists(self):
        try:
            from src.attempted_courses import course_names
        except:
            self.fail("Your program should have a function called course_names(attempts: list)")

    @points('12.attempted_courses_part2')
    def test_07_course_names_return_type(self):
        from src.attempted_courses import course_names
        from src.attempted_courses import CourseAttempt

        code = """
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Programming", 2)
course_names([s1, s2, s3])
"""

        try:
            s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
            s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
            s3 = CourseAttempt("Peter Python", "Advanced Programming", 2)
            response = course_names([s1, s2, s3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        m = map(None, [])
        taip = str(type(response)).replace("<class '","").replace("'>","")
        self.assertTrue(type(response) == type(m) or type(response) == list or type(response) == set, f"Function course_names(course_namet: list) should return map or list, now the return value was of type {taip}")
        for alkio in response:
            etaip = str(type("")).replace("<class '","").replace("'>","")
            taip = str(type(alkio)).replace("<class '","").replace("'>","")
            self.assertTrue(type(alkio) == type(""),  f"When this code is executed {code}the values returned should be of type {etaip} now the type is {taip}")
     
    @points('12.attempted_courses_part2')
    def test_08_course_names_works_1(self):
        from src.attempted_courses import course_names
        from src.attempted_courses import CourseAttempt

        code = """
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Programming", 2)
course_names([s1, s2, s3])
"""

        try:
            s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
            s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
            s3 = CourseAttempt("Peter Python", "Advanced Programming", 2)
            response = course_names([s1, s2, s3])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        m = map(None, [])
        taip = str(type(response)).replace("<class '","").replace("'>","")
        self.assertTrue(type(response) == type(m) or type(response) == list or type(response) == set, f"Function course_names(course_namet: list) should return map or list, now the return value was of type {taip}")
        
        response = list(response)

        for alkio in response:
            etaip = str(type("")).replace("<class '","").replace("'>","")
            taip = str(type(alkio)).replace("<class '","").replace("'>","")
            self.assertTrue(type(alkio) == type(""),  f"When this code is executed {code}the values returned should be of type {etaip} now the type is {taip}")
     
        exp = sorted(set( s.course_name for s in [s1, s2, s3]))

        output = ""
        vast = []
        for n in response:
            output += n + "\n"
            vast.append(n)

        self.assertTrue(sorted(vast) == sorted(exp),  f"When this code is executed {code}should return course names \n{s(exp)}\nnow the function returns\n{output}")

    @points('12.attempted_courses_part2')
    def test_09_course_names_uses_map(self):
        src_file = os.path.join('src', 'attempted_courses.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def course_names"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def course_names" in line):
                    p = False 
                elif p:
                    lines.append(line)

        on = False
        for line in lines:
            if "map" in line:
                on = True              
        self.assertTrue(on, f"Function course_names(attempts: list) must use map!")   

    @points('12.attempted_courses_part2')
    def test_10_course_names_works_2(self):
        from src.attempted_courses import course_names
        from src.attempted_courses import CourseAttempt

        code = """
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Algorithms", 2)
s4 = CourseAttempt("Hector Helastic", "Full stack", 3)
s5 = CourseAttempt("Lady Gaga", "Advanced Programming", 5)
s6 = CourseAttempt("Eila Karkki", "Data Communications 1", 2)

course_names([s1, s2, s3, s4, s5, s6])
"""

        try:
            s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
            s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
            s3 = CourseAttempt("Peter Python", "Algorithms", 2)
            s4 = CourseAttempt("Hector Helastic", "Full stack", 3)
            s5 = CourseAttempt("Lady Gaga", "Advanced Programming", 5)
            s6 = CourseAttempt("Eila Karkki", "Data Communications 1", 2)

            response = course_names([s1, s2, s3, s4, s5, s6])
        except:
            self.fail(f"Check that the following code can be executed\n{code}")

        exp = sorted(set( s.course_name for s in [s1, s2, s3, s4, s5, s6]))

        output = ""
        vast = []
        for n in response:
            output += n + "\n"
            vast.append(n)

        self.assertEquals(sorted(vast), sorted(exp),  f"When this code is executed {code}it should return courses\n{s(exp)}\nnow the function returns\n{output}")


if __name__ == '__main__':
    unittest.main()
