import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date, datetime, timedelta

exercise = 'src.course_records'

def f(attr: list):
    return ",".join(attr)

def s(l: list):
    return "\n".join(l)

class CourseRecordsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'en')

    @points('10.course_records_part1')
    def test_0_stops(self):
        input_values = ["0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with input\n{s(input_values)}")
                
            output = get_stdout()

    @points('10.course_records_part1')
    def test_1_add_works_1(self):
        input_values = ["1", "Programming", "3", "5", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with inputn{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your program does not output anything.\n Check that it is not insde if __name__ == "__main__" block!')

    @points('10.course_records_part1')
    def test_2_add_found(self):
        input_values = ["1", "Programming", "3", "5", "2", "Programming", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with inputn{s(input_values)}")
                
            output = get_stdout()
            expected = "Programming (5 cr) grade 3"
            self.assertTrue(expected in output, f"Program output should be\n{expected}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   

    @points('10.course_records_part1')
    def test_3_increase_works(self):
        input_values = ["1", "Programming", "3", "5","1","Programming", "5", "5", "2", "Programming", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with inputn{s(input_values)}")
                
            output = get_stdout()
            expected = "Programming (5 cr) grade 5"
            self.assertTrue(expected in output, f"Program output should be\n{expected}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   
            expected = "Programming (5 cr) grade 3"
            self.assertFalse(expected in output, f"The output should NOT contain\n{expected}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   

    @points('10.course_records_part1')
    def test_4_grade_does_not_decrease(self):
        input_values = ["1", "Programming", "3", "5", "1","Programming", "1", "5", "2", "Programming", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with inputn{s(input_values)}")
                
            output = get_stdout()
            expected = "Programming (5 cr) grade 3"
            self.assertTrue(expected in output, f"Program output should be\n{expected}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   
            expected = "Programming (5 cr) grade 1"
            self.assertFalse(expected in output, f"The output should NOT contain\n{expected}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   

    @points('10.course_records_part1')
    def test_5_unkonow_completion(self):
        input_values = ["1", "Programming", "3", "5", "2", "Java-ohjelmointi","0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with inputn{s(input_values)}")

            output = get_stdout()
            expected = "no entry for this course"
            self.assertTrue(expected in output, f"Program output should be\n{expected}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   
            expected = "Programming (5 cr) grade"
            self.assertFalse(expected in output, f"The output should NOT contain\n{expected}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   

    @points('10.course_records_part2')
    def test_6_stats_1(self):
        input_values = ["1", "Programming", "3", "5", "3","0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with inputn{s(input_values)}")

            output = get_stdout()
            exp = """
1 completed courses, a total of 5 credits
mean 3
grade distribution
5:
4:
3: x
2:
1:
"""

            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"Program should output line\n{line}\nwith input\n{s(input_values)}\nOutput was\n{output}")   

    @points('10.course_records_part2')
    def test_7_stats_2(self):
        input_values = ["1", "Programming", "3", "5", "1", "Ohja", "5", "5", "3", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with inputn{s(input_values)}")

            output = get_stdout()
            exp = """
2 completed courses, a total of 10 credits
mean 4
grade distribution
5: x
4:
3: x
2:
1:
"""

            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"Program should output line\n{line}\nwith input\n{s(input_values)}\nOutput was\n{output}")   

    @points('10.course_records_part2')
    def test_7_stats_3(self):
        input_values = ["1", "Programming", "3", "5", "1", "Programming", "5", "5", "3", "1", "Algorithms", "5", "10", "3", "1", "Statistics", "1", "5", "3", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with inputn{s(input_values)}")

            output = get_stdout()
            exp = """
3 completed courses, a total of 20 credits
mean 3.7
grade distribution
5: xx
4:
3:
2:
1: x
"""

            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"Program should output line\n{line}\nwith input\n{s(input_values)}\nOutput was\n{output}")   

    @points('10.course_records_part2')
    def test_8_stats_4(self):
        input_values = ["1", "Programming", "3", "5", 
                 "1", "Programming", "5", "5", 
                 "1", "Algorithms", "5", "10",
                 "1", "Statistics", "1", "5", 
                 "1", "Databases", "4", "5", 
                 "1", "Operating Systems", "2", "5",
                 "1", "Distributed Systems", "4", "5", 
                 "1", "Unix", "2", "1", 
                 "3", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that the program works with inputn{s(input_values)}")

            output = get_stdout()
            exp = """
7 completed courses, a total of 36 credits
mean 3.3
grade distribution
5: xx
4: xx
3:
2: xx
1: x
"""

            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"Program should output line\n{line}\nwith input\n{s(input_values)}\nOutput was\n{output}")   

if __name__ == '__main__':
    unittest.main()
