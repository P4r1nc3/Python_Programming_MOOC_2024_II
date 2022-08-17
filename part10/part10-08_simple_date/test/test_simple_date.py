import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint, shuffle
from datetime import date

exercise = 'src.simple_date'

def f(attr: list):
    return "\n".join([str(x) for x in attr]) 

class SimpleDateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
           cls.module = load_module(exercise, 'en')

    
    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)
    
    @points('10.simple_date_part1')
    def test_1_class_exists(self):
        try:
            from src.simple_date import SimpleDate
            a = SimpleDate(1,1,1900)
        except Exception as e:
            self.fail(f'Calling constructor SimpleDate(1,1,1900) threw an error \n{e}\n' + 
            'Check that an object can be created from the class.')

    @points('10.simple_date_part1')
    def test_2_str(self):
        from src.simple_date import SimpleDate
        test_cases = [(1,1,1900),(2,4,1984),(9,9,1976),(10,11,2015),(24,11,1299)]
        for test_case in test_cases:
            sdate = SimpleDate(test_case[0], test_case[1], test_case[2])
            val = str(sdate)
            corr = f"{test_case[0]}.{test_case[1]}.{test_case[2]}"

            self.assertEqual(val, corr, f'Method __str__ should return ' +
                f'\n{corr}\nwhen date is initialized like this:\n' +
                f'SimpleDate({test_case[0]}, {test_case[1]}, {test_case[2]})\n' + 
                f'Now the method returns\n{val}')


    @points('10.simple_date_part1')
    def test_3_equality(self):
        from src.simple_date import SimpleDate
        test_cases = [((1,1,1900),(1,1,1900)),((5,6,1876),(5,6,1876)),
            ((9,9,1976),(9,9,1976)), ((1,4,1800),(2,4,1800)), 
            ((1,7,1999),(1,8,1999)),((25,5,1943),(25,5,1944))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            sd1 = SimpleDate(tc1[0], tc1[1], tc1[2])
            sd2 = SimpleDate(tc2[0], tc2[1], tc2[2])

            corr = (tc1 == tc2)
            val = (sd1 == sd2)
            stmt = "sd1 == sd2"
            met_name = "__eq__"

            self.assertEqual(val, corr, f'Value of expression\n{stmt}\nshould be ' +
                f'{corr},  when objects are initialized as:\n'
                f'sd1 = SimpleDate({tc1[0]}, {tc1[1]}, {tc1[2]})\n' + 
                f'sd2 = SimpleDate({tc2[0]}, {tc2[1]}, {tc2[2]})\n' + 
                f'Now the value of expression is {val}.\n' + 
                f'Check method {met_name}')

    @points('10.simple_date_part1')
    def test_4_less_than(self):
        from src.simple_date import SimpleDate
        test_cases = [((1,1,1900),(1,1,1901)),((5,6,1876),(6,6,1876)),
            ((9,9,1976),(9,10,1976)), ((2,4,1800),(1,4,1800)), 
            ((1,8,1999),(1,7,1999)),((25,5,1944),(25,5,1943)), 
            ((1,3,1900),(2,4,1889))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            sd1 = SimpleDate(tc1[0], tc1[1], tc1[2])
            sd2 = SimpleDate(tc2[0], tc2[1], tc2[2])

            tv1 = tc1[2] * 360 + tc1[1] * 30 + tc1[0]
            tv2 = tc2[2] * 360 + tc2[1] * 30 + tc2[0]
            corr = (tv1 < tv2)
            val = (sd1 < sd2)
            stmt = "sd1 < sd2"
            met_name = "__lt__"

            self.assertEqual(val, corr, f'Value of expression\n{stmt}\nshould be ' +
                f'{corr},  when objects are initialized as:\n'
                f'sd1 = SimpleDate({tc1[0]}, {tc1[1]}, {tc1[2]})\n' + 
                f'sd2 = SimpleDate({tc2[0]}, {tc2[1]}, {tc2[2]})\n' + 
                f'Now the value of expression is {val}.\n' + 
                f'Check method {met_name}')

    @points('10.simple_date_part1')
    def test_5_greater_than(self):
        from src.simple_date import SimpleDate
        test_cases = [((1,1,1900),(1,1,1901)),((5,6,1876),(6,6,1876)),
            ((9,9,1976),(9,10,1976)), ((2,4,1800),(1,4,1800)), 
            ((1,8,1999),(1,7,1999)),((25,5,1944),(25,5,1943)), 
            ((9,9,1900),(8,8,1901))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            sd1 = SimpleDate(tc1[0], tc1[1], tc1[2])
            sd2 = SimpleDate(tc2[0], tc2[1], tc2[2])

            tv1 = tc1[2] * 360 + tc1[1] * 30 + tc1[0]
            tv2 = tc2[2] * 360 + tc2[1] * 30 + tc2[0]
            corr = (tv1 > tv2)
            val = (sd1 > sd2)
            stmt = "sd1 > sd2"
            met_name = "__gt__"

            self.assertEqual(val, corr, f'Value of expression\n{stmt}\nshould be ' +
                f'{corr},  when objects are initialized as:\n'
                f'sd1 = SimpleDate({tc1[0]}, {tc1[1]}, {tc1[2]})\n' + 
                f'sd2 = SimpleDate({tc2[0]}, {tc2[1]}, {tc2[2]})\n' + 
                f'Now the value of expression is {val}.\n' + 
                f'Check method {met_name}')

    @points('10.simple_date_part1')
    def test_6_not_equal_to(self):
        from src.simple_date import SimpleDate
        test_cases = [((1,1,1900),(1,1,1900)),((5,6,1876),(5,6,1876)),
            ((9,9,1976),(9,9,1976)), ((1,4,1800),(2,4,1800)), 
            ((1,7,1999),(1,8,1999)),((25,5,1943),(25,5,1944))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            sd1 = SimpleDate(tc1[0], tc1[1], tc1[2])
            sd2 = SimpleDate(tc2[0], tc2[1], tc2[2])

            corr = (tc1 != tc2)
            val = (sd1 != sd2)
            stmt = "sd1 != sd2"
            met_name = "__ne__"

            self.assertEqual(val, corr, f'Value of expression\n{stmt}\nshould be ' +
                f'{corr},  when objects are initialized as:\n'
                f'sd1 = SimpleDate({tc1[0]}, {tc1[1]}, {tc1[2]})\n' + 
                f'sd2 = SimpleDate({tc2[0]}, {tc2[1]}, {tc2[2]})\n' + 
                f'Now the value of expression is {val}.\n' + 
                f'Check method {met_name}')

    @points('10.simple_date_part2')
    def test_7a_plus(self):
        from src.simple_date import SimpleDate
        test_cases = [(1,1,1900,1),(5,5,1900,20),(1,5,1878,30),(23,5,1999,45), 
            (1,12,1999,150),(29,12,1999,790)]
        for test_case in test_cases:
            sdate = SimpleDate(test_case[0], test_case[1], test_case[2])
            
            d,m,y = test_case[:-1]
            d += test_case[-1]
            while d > 30:
                d -= 30
                m += 1
            while m> 12:
                m -= 12
                y += 1
            corr = f"{d}.{m}.{y}"
            val = str(sdate + test_case[-1])
            stmt = f"print(sdate + {test_case[-1]})"
            met_name = "__add__"

            self.assertEqual(val, corr, f'Statement\n{stmt}\nshould output ' +
                f'{corr},  when object is initialized as:\n'
                f'sdate = SimpleDate({test_case[0]}, {test_case[1]}, {test_case[2]})\n' + 
                f'Now the statement outputs {val}.\n' + 
                f'Check method {met_name}')

            self.assertTrue(isinstance(sdate + test_case[-1], SimpleDate), f'Method __add__ should return a new SimpleDate object.\n' +
                f'Check method {met_name}')

    @points('10.simple_date_part2')
    def test_7b_plus(self):
        from src.simple_date import SimpleDate
        test_cases = [(1,1,1900,1),(5,5,1900,20),(1,5,1878,30),(23,5,1999,45),
            (1,12,1999,150),(29,12,1999,790)]
        for test_case in test_cases:
            sdate = SimpleDate(test_case[0], test_case[1], test_case[2])
            orig_date = f'{test_case[0]}.{test_case[1]}.{test_case[2]}'
            val = sdate + test_case[-1]
            code = f"d1 = SimpleDate({test_case[0]}, {test_case[1]}, {test_case[2]})\nd2 = d1 + {test_case[-1]}"

            self.assertEqual(orig_date, str(sdate), f'Adding days to a date should not change the original date.' +
                f'\nAfter executing the following code:\n{code}\n' +
                f'original date is expected to be {orig_date}, but it is {sdate}\n' + '')

    @points('10.simple_date_part3')
    def test_8_minus(self):
        from src.simple_date import SimpleDate
        test_cases = [((2,1,1900),(1,1,1900)),((5,6,1876),(4,6,1876)),
            ((9,9,1976),(9,10,1976)), ((1,4,1800),(1,5,1800)), 
            ((1,7,1999),(1,8,1998)),((25,5,1943),(25,5,1942)), 
            ((9,9,1976),(9,10,1966)), ((1,4,1800),(3,5,1842)),
            ((1,7,1999),(1,8,1998)),((25,5,1943),(25,5,1942))]

        for test_case in test_cases:
            tc1,tc2 = test_case
            sd1 = SimpleDate(tc1[0], tc1[1], tc1[2])
            sd2 = SimpleDate(tc2[0], tc2[1], tc2[2])

            tv1 = tc1[2] * 360 + tc1[1] * 30 + tc1[0]
            tv2 = tc2[2] * 360 + tc2[1] * 30 + tc2[0]

            corr = abs(tv1 - tv2)
            val = (sd1 - sd2)
            stmt = "sd1 - sd2"
            met_name = "__sub__"

            self.assertEqual(val, corr, f'Value of expression\n{stmt}\nshould be ' +
                f'{corr},  when objects are initialized as:\n'
                f'sd1 = SimpleDate({tc1[0]}, {tc1[1]}, {tc1[2]})\n' + 
                f'sd2 = SimpleDate({tc2[0]}, {tc2[1]}, {tc2[2]})\n' + 
                f'Now the value of expression is {val}.\n' + 
                f'Check method {met_name}')

 
    
if __name__ == '__main__':
    unittest.main()
