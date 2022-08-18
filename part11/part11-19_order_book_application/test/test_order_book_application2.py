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

@points('11.order_book_application_part2')
class OrderBookApplication2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'en')

    def test_1_workload_not_int(self):
        syote = [
            "1", "code new facebook", "jonas x", 
            "0"
        ]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()
            expected = "erroneous input"
            self.assertTrue(expected in output, f"The print out of your program is expected to contain\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   

    def test_2_missing_workload(self):
        syote = [
            "1", "code new facebook", "jonas", 
            "0"
        ]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()
            expected = "erroneous input"
            self.assertTrue(expected in output, f"The print out of your program is expected to contain\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   

    def test_3_add_works_after_error(self):
        syote = [
            "1", "code new facebook", "jonas",
            "1", "code new facebook", "jonas 10", 
            "3",
            "0"
        ]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()
            expected = "erroneous input"
            self.assertTrue(expected in output, f"The print out of your program is expected to contain\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   
            expected = "added!"
            self.assertTrue(expected in output, f"The print out of your program is expected to contain\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   
            expected = tt("code new facebook", "jonas 10", False)
            self.assertTrue(expected in output, f"The print out of your program is expected to contain\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")  

    def test_4_mark_as_finished_not_int(self):
        syote = [
            "1", "code new facebook", "jonas 10", 
            "4", "xx",
            "0"
        ]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()
            expected = "erroneous input"
            self.assertTrue(expected in output, f"The print out of your program is expected to contain\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")

            notexpected = "marked as finished"
            self.assertFalse(notexpected in output, f"The print out of your program is not expected to contain\n{notexpected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   


    def test_5_mark_as_finished_does_not_exists(self):
        syote = [
            "1", "code new facebook", "jonas 10", 
            "4", "100",
            "0"
        ]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()
            expected = "erroneous input"
            self.assertTrue(expected in output, f"The print out of your program is expected to contain\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")

            eiexpected = "marked as finished"
            self.assertFalse(eiexpected in output, f"The print out of your program is not expected to contain\n{eiexpected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")   

    def test_5_mark_as_finished_works_after_error(self):
        syote = [
            "1", "code new facebook", "jonas 10", 
            "4", "100",
            "4", "1",
            "0"
        ]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()
            expected = "erroneous input"
            self.assertTrue(expected in output, f"The print out of your program is expected to contain\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")

            expected = "marked as finished"
            self.assertTrue(expected in output, f"The print out of your program is expected to contain\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")

    def test_6_unknown_programmer(self):
        syote = [
            "1", "code new facebook", "jonas 10", 
            "6", "Brian",
            "0"
        ]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Make sure, that the program works with the input\n{s(syote)}")

            output = get_stdout()
            expected = "erroneous input"
            self.assertTrue(expected in output, f"The print out of your program is expected to contain\n{expected}\nwith the input\n{s(syote)}\nThe print out was\n{output}")