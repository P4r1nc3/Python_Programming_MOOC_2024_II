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

exercise = 'src.series'
classname = "Series"

def f(attr: list):
    return ",".join(attr)

class SeriesTest(unittest.TestCase):
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

    @points('8.series_part1')
    def test1_class_exists(self):
        try:
            from src.series import Series
        except:
            self.fail("Your program should have a class called Series")

    @points('8.series_part1')
    def test2_constructor(self):
        try:
            from src.series import Series
            series = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
        except Exception as e:
            self.fail('Calling constructor as Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])' +
                f' threw an error: {e}\nCheck that constructor is correctly defined!')

    @points('8.series_part1')
    def test3_test_str(self):
        test_case = ("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
        try:
            from src.series import Series
            code = f'Series("{test_case[0]}", {test_case[1]}, {test_case[2]})'
            series = Series(test_case[0], test_case[1], test_case[2])

            genres = ", ".join(test_case[2])
            corr = f'{test_case[0]} ({test_case[1]} seasons)\ngenres: {genres}\nno ratings'
            val = str(series)

            self.assertEqual(sanitize(corr), sanitize(val), f"Method __str__ should return a string\n{corr}\nwhen object was created as\n" + 
                f"{code}\nNow method returns\n{val}")

        except Exception as e:
            self.fail(f'Calling method __str__ threw an error: {e}\nwhen object was created as\n{code}')

    @points('8.series_part1')
    def test3_test_str2(self):
        test_case = ("South Park", 24, ["Animation", "Comedy"])
        try:
            from src.series import Series
            code = f'Series("{test_case[0]}", {test_case[1]}, {test_case[2]})'
            series = Series(test_case[0], test_case[1], test_case[2])

            genres = ", ".join(test_case[2])
            corr = f'{test_case[0]} ({test_case[1]} seasons)\ngenres: {genres}\nno ratings'
            val = str(series)

            self.assertEqual(sanitize(corr), sanitize(val), f"Method __str__ should return a string\n{corr}\nwhen object was created as\n" + 
                f"{code}\nNow method returns\n{val}")

        except Exception as e:
            self.fail(f'Calling method __str__ threw an error: {e}\nwhen object was created as\n{code}')


    @points('8.series_part2')
    def test5_rate_exists(self):
        try:
            from src.series import Series
            code = """
s = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s.rate(5)
"""
     
            s = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
            s.rate(5)

        except Exception as e:
            self.fail(f'Executing code\n{code}\threw an error\n{e}\nCheck that method rate(self, rating: int) is defined.')

    @points('8.series_part2')
    def test5_rate(self):
        from src.series import Series
        code = """
s = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s.rate(5)
"""

        test_case = ("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])

        s = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
        s.rate(5)

        arv = "1 ratings, average 5.0 points"
        
        genres = ", ".join(test_case[2])
        corr = f'{test_case[0]} ({test_case[1]} seasons)\ngenres: {genres}\n{arv}'
        val = str(s)

        self.assertTrue(sanitize(corr) == sanitize(val), f"Method __str__ should return a string\n{corr}\nwhen object was created as\n" + 
            f"{code}\nNow method returns a string\n{val}")


        s.rate(3)

        code += "s.rate(3)\n"
        arv = "2 ratings, average 4.0 points"

        corr = f'{test_case[0]} ({test_case[1]} seasons)\ngenres: {genres}\n{arv}'
        val = str(s)

        self.assertTrue(sanitize(corr) == sanitize(val), f"Method __str__ should return a string\n{corr}\nwhen object was created as\n" + 
            f"{code}\nNow method returns a string\n{val}")

        s.rate(2)

        code += "s.rate(2)\n"
        arv = "3  ratings, average 3.3 points"

        corr = f'{test_case[0]} ({test_case[1]} seasons)\ngenres: {genres}\n{arv}'
        val = str(s)

        self.assertTrue(sanitize(corr) == sanitize(val), f"Method __str__ should return a string\n{corr}\nwhen object was created as\n" + 
            f"{code}\nNow method returns a string\n{val}")

        s.rate(5)

        code += "s.rate(5)\n"
        arv = "4 ratings, average 3.8 points"

        corr = f'{test_case[0]} ({test_case[1]} seasons)\ngenres: {genres}\n{arv}'
        val = str(s)

        self.assertTrue(sanitize(corr) == sanitize(val), f"Method __str__ should return a string\n{corr}\nwhen object was created as\n" + 
            f"{code}\nNow method returns a string\n{val}")

    @points('8.series_part3')
    def test6_function_minimum_grade_olemassa(self):
        try:
            from src.series import minimum_grade
        except:
            self.fail("Your program should have a function called minimum_grade(grade: float, series: list)")

    @points('8.series_part3')
    def test7_function_minimum_grade(self):
        from src.series import minimum_grade
        from src.series import Series

        s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
        s1.rate(5)

        s2 = Series("South Park", 24, ["Animation", "Comedy"])
        s2.rate(3)

        s3 = Series("Friends", 10, ["Romance", "Comedy"])
        s3.rate(2)

        series = [s1, s2, s3]

        code = """
s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)
s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)
s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)
series = [s1, s2, s3]

vastaus = minimum_grade(4.5, series)
"""
        try:
            answer = minimum_grade(4.5, series)
        except:
            self.fail(f"Check that the following code can be executed\n{code}")
        
        self.assertTrue(type(answer) == list, "Function minimum_grade(rating: float, series: list) should return a list")

        expected = 1
        self.assertTrue(len(answer)==expected, f"When this code is executed\n{code}\nthe length of the list returned should be {expected}, however, it was {len(answer)}")
        self.assertTrue(answer[0].title=="Dexter", f"When this code is executed,\n{code}\nthe only series in the list should be Dexter, list however is {answer[0].title}")

        code = """
s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)
s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)
s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)
series = [s1, s2, s3]

vastaus = minimum_grade(1.5, series)
"""
        try:
            answer = minimum_grade(2.5, series)
        except:
            self.fail(f"Check that the following code can be executed\n{code}")
        
        self.assertTrue(type(answer) == list, "Function minimum_grade(grade: float, series: list) should return a list")

        expected = 2
        self.assertTrue(len(answer)==expected, f"When this code is executed\n{code}\nthe length of the list returned should be {expected}, however, it was {len(answer)}")
        ehto = (answer[0].title=="Dexter" and answer[1].title=="South Park") or (answer[1].title=="Dexter" and answer[0].title=="South Park")
        self.assertTrue(ehto, f"When this code is executed code\n{code}\nthe list should include Dexter and South park, now the list was {answer[0].title} ja {answer[1].title}")

    @points('8.series_part3')
    def test8_function_includes_genre_olemassa(self):
        try:
            from src.series import includes_genre
        except:
            self.fail("Your program should include a function  includes_genre(genre: str, series: list)")

    @points('8.series_part3')
    def test9_function_includes_genre(self):
        from src.series import includes_genre
        from src.series import Series

        s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
        s1.rate(5)

        s2 = Series("South Park", 24, ["Animation", "Comedy"])
        s2.rate(3)

        s3 = Series("Friends", 10, ["Romance", "Comedy"])
        s3.rate(2)

        series = [s1, s2, s3]

        code = """
s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)
s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)
s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)
series = [s1, s2, s3]

vastaus = includes_genre("Crime", series)
"""
        try:
            answer = includes_genre("Crime", series)
        except:
            self.fail(f"Check that the following code can be executedn{code}")

        self.assertTrue(type(answer) == list, "Function includes_genre(genre: str, series: list) should return a list")

        expected = 1
        self.assertTrue(len(answer)==expected, f"When this code is executed\n{code}\nthe length of the list returned should be {expected}, however, it was {len(answer)}")
        self.assertTrue(answer[0].title=="Dexter", f"When this code is executed,\n{code}\nthe only series in the list should be Dexter, list however is {answer[0].title}")

        code = """
s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)
s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)
s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)
series = [s1, s2, s3]

vastaus = includes_genre("Programming", series)
"""
        try:
            answer = includes_genre("Programming", series)
        except:
            self.fail(f"Check that the following code can be executedn{code}")


        expected = 0
        self.assertTrue(len(answer)==expected, f"When this code is executed\n{code}\nthe length of the list returned should be {expected}, however, it was {len(answer)}")
        
        code = """
s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)
s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)
s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)
series = [s1, s2, s3]

vastaus = includes_genre("Comedy", series)
"""
        try:
            answer = includes_genre("Comedy", series)
        except:
            self.fail(f"Check that the following code can be executedu\n{code}")
        
        expected = 2
        self.assertTrue(len(answer)==expected, f"When this code is executed\n{code}\nthe length of the list returned should be {expected}, however, it was {len(answer)}")
        ehto = (answer[0].title=="Friends" and answer[1].title=="South Park") or (answer[1].title=="Friends" and answer[0].title=="South Park")
        self.assertTrue(ehto, f"When this code is executed code\n{code}\nthe list should include Friends and South park, now the list was {answer[0].title} ja {answer[1].title}")

if __name__ == '__main__':
    unittest.main()