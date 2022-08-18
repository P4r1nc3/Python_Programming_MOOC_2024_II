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

exercise = 'src.order_book_application'

def f(attr: list):
    return ",".join(attr)

def s(l: list):
    return "\n".join(l)

def tt(d, kh, s):
    status = "NOT FINISHED" if not s else "FINISHED"
    k, h, *x = kh.split(' ')
    return f"{d} ({h} hours), programmer {k} {status}"

@points('11.order_book_application_part1')
class Tilauskirjasovellus1Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'en')

    def test_01_stops(self):
        syote = ["0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

    def test_02_instructions_is_printed(self):
        syote = ["0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your program does not print out anything. Make sure, that it is NOT inside the if __name__ == "__main__" -block')

            exp = """commands:
0 exit
1 add order
2 list finished tasks
3 list unfinished tasks
4 mark task as finished
5 programmers
6 status of programmer"""

            for row in exp.split("\n"):
                if not row in output:
                    self.fail(f"The program should print out row\n{row}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   
            
            not_expected = "added!"
            self.assertFalse(not_expected in output, f"The following row is not expected to be in print out\n{not_expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   

    def test_03_add_order_works(self):
        syote = ["1", "code new facebook", "jonas 10", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()
            expected = "added!"
            self.assertTrue(expected in output, f"The following row was expected to be in the print out\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   

    def test_04_unfinished_1(self):
        syote = ["1", "code new facebook", "jonas 10", "3","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()
            expected = tt("code new facebook", "jonas 10", False)
            self.assertTrue(expected in output, f"The following row was expected to be in the print out\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   

    def test_05_ei_valmiit_2(self):
        syote = [
            "1", "code new facebook", "jonas 10", 
            "1", "code new twitter", "elina 95",
            "3","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()
            expected = tt("code new facebook", "jonas 10", False)
            self.assertTrue(expected in output, f"The following row was expected to be in the print out\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   
            expected = tt("code new twitter", "elina 95", False)
            self.assertTrue(expected in output, f"The following row was expected to be in the print out\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   

    def test_06_mark_as_finished(self):
        syote = ["1", "code new facebook", "jonas 10", "4", "1","3","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()

            expected = "marked as finished"
            self.assertTrue(expected in output, f"The following row was expected to be in the print out\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   

            eiexpected = tt("code new facebook", "jonas 10", False)
            self.assertFalse(eiexpected in output, f"The following row is not expected to be in print out\n{eiexpected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   

    def test_07_finished(self):
        syote = ["1", "code new facebook", "jonas 10", "4", "1","2","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()

            expected = "marked as finished"
            self.assertTrue(expected in output, f"The following row was expected to be in the print out\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   

            expected = tt("code new facebook", "jonas 10", True)
            self.assertTrue(expected in output, f"The following row was expected to be in the print out\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   

    def test_08_programmers(self):
        syote = ["1", "code new facebook", "jonas 10", "5", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()

            expected = "jonas"
            self.assertTrue(expected in output, f"The following row was expected to be in the print out\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   

    def test_09_status_of_programmer_1(self):
        syote = ["1", "code new facebook", "jonas 10", "6", "jonas","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()

            expected = "tasks: finished 0 not finished 1, hours: done 0 scheduled 10"
            self.assertTrue(expected in output, f"The following row was expected to be in the print out\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   

    def test_10_status_of_programmer_2(self):
        syote = [
            "1", "code new facebook", "jonas 10", 
            "1", "code new twitter", "jonas 95",
            "4", "1",
            "6", "jonas","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()

            expected = "tasks: finished 1 not finished 1, hours: done 10 scheduled 95"
            self.assertTrue(expected in output, f"The following row was expected to be in the print out\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   


    def test_11_valmiita(self):
        syote = ["1", "code new facebook", "jonas 10", "2" ,"0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()

            expected = "no finished tasks"
            self.assertTrue(expected in output, f"The following row was expected to be in the print out\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   

    def test_12_ei_valmiit_2(self):
        syote = [
            "1", "code new facebook", "jonas 10", 
            "1", "code new twitter", "elina 95",
            "4","1",
            "4","2",
            "2","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()
            expected = tt("code new facebook", "jonas 10", True)
            self.assertTrue(expected in output, f"The following row was expected to be in the print out\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   
            expected = tt("code new twitter", "elina 95", True)
            self.assertTrue(expected in output, f"The following row was expected to be in the print out\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   

if __name__ == '__main__':
    unittest.main()