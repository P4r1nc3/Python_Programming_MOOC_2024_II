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

exercise = 'src.money'

def f(attr: list):
    return "\n".join([str(x) for x in attr]) 

class MoneyTest(unittest.TestCase):
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
    
    @points('10.money_part1')
    def test_1_class_money_olemassa(self):
        try:
            from src.money import Money
            a = Money(1,1)
        except Exception as e:
            self.fail(f'Calling construtor Money(1,1) threw an error \n{e}\n' + 
            'Check that an object can be created!')

    @points('10.money_part1')
    def test_2_str(self):
        from src.money import Money
        test_cases = [(1,50), (2,75), (399,99), (4,1), (5,2), (1243,9)]
        for test_case in test_cases:
            money = Money(test_case[0], test_case[1])
            val = str(money)
            corr = f"{test_case[0]}.{test_case[1]:02d} eur"

            self.assertEqual(val, corr, f'Method __str__ should return ' +
                f'\n{corr}\nwhen Money object was initialized as:\n' +
                f'Money({test_case[0]}, {test_case[1]})\nNow method returns\n' + 
                f'{val}')


    @points('10.money_part2')
    def test_3_equality(self):
        from src.money import Money
        test_cases = [((1,0), (1,0)), ((2,50),(2,50)), ((4,5),(4,5)), ((15,95),(15,95)),
            ((1,0), (2,0)), ((4,50), (4,5)), ((3,95),(3,96)), ((1110,0),(1110,1))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            money1 = Money(tc1[0], tc1[1])
            money2 = Money(tc2[0], tc2[1])

            corr = tc1 == tc2
            val = (money1 == money2)
            stmt = "money1 == money2"
            met_name = "__eq__"

            self.assertEqual(val, corr, f'Expression\n{stmt}\nshould be ' +
                f'{corr},  when objects are initialized as:\n'
                f'money1 = Money({tc1[0]}, {tc1[1]})\n' + 
                f'money2 = Money({tc2[0]}, {tc2[1]})\n' + 
                f'Now expression returns {val}.\n' + 
                f'Check the method {met_name}')

    @points('10.money_part3')
    def test_4_less_than(self):
        from src.money import Money
        test_cases = [((1,0), (2,0)), ((2,50),(3,50)), ((4,5),(4,50)), ((15,95),(15,96)),
            ((2,0), (1,0)), ((4,50), (4,5)), ((3,95),(3,95)), ((1110,10),(1110,1))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            money1 = Money(tc1[0], tc1[1])
            money2 = Money(tc2[0], tc2[1])

            corr = tc1 < tc2
            val = (money1 < money2)
            stmt = "money1 < money2"
            met_name = "__lt__"

            self.assertEqual(val, corr, f'Expression\n{stmt}\nshould be ' +
                f'{corr},  when objects are initialized as:\n'
                f'money1 = Money({tc1[0]}, {tc1[1]})\n' + 
                f'money2 = Money({tc2[0]}, {tc2[1]})\n' + 
                f'Now expression returns {val}.\n' + 
                f'Check the method {met_name}')

    @points('10.money_part3')
    def test_5_greater_than(self):
        from src.money import Money
        test_cases = [((1,0), (2,0)), ((2,50),(3,50)), ((4,50),(4,50)), ((15,95),(15,96)),
            ((2,0), (1,0)), ((4,50), (4,5)), ((3,95),(3,90)), ((1110,10),(1110,1))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            money1 = Money(tc1[0], tc1[1])
            money2 = Money(tc2[0], tc2[1])

            corr = tc1 > tc2
            val = (money1 > money2)
            stmt = "money1 > money2"
            met_name = "__gt__"

            self.assertEqual(val, corr, f'Expression\n{stmt}\nshould be ' +
                f'{corr},  when objects are initialized as:\n'
                f'money1 = Money({tc1[0]}, {tc1[1]})\n' + 
                f'money2 = Money({tc2[0]}, {tc2[1]})\n' + 
                f'Now expression returns {val}.\n' + 
                f'Check the method {met_name}')

    @points('10.money_part3')
    def test_6_not_equal_to(self):
        from src.money import Money
        test_cases = [((1,0), (1,0)), ((2,50),(2,50)), ((4,5),(4,50)), ((15,95),(15,95)),
            ((2,0), (1,0)), ((4,50), (4,5)), ((3,95),(3,90)), ((1110,10),(1110,0))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            money1 = Money(tc1[0], tc1[1])
            money2 = Money(tc2[0], tc2[1])

            corr = tc1 != tc2
            val = (money1 != money2)
            stmt = "money1 != money2"
            met_name = "__ne__"

            self.assertEqual(val, corr, f'Expression\n{stmt}\nshould be ' +
                f'{corr},  when objects are initialized as:\n'
                f'money1 = Money({tc1[0]}, {tc1[1]})\n' + 
                f'money2 = Money({tc2[0]}, {tc2[1]})\n' + 
                f'Now expression returns {val}.\n' + 
                f'Check the method {met_name}')

    @points('10.money_part4')
    def test_7_plus(self):
        from src.money import Money
        test_cases = [((1,0), (1,0)), ((2,50),(2,50)), ((4,5),(4,50)), ((15,95),(15,95)),
            ((2,0), (1,0)), ((4,50), (4,5)), ((3,95),(3,90)), ((1110,10),(1110,0))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            money1 = Money(tc1[0], tc1[1])
            money2 = Money(tc2[0], tc2[1])

            e = tc1[0] + tc2[0]
            c = tc1[1] + tc2[1]
            if c >= 100:
                c -= 100
                e += 1
            corr = f"{e}.{c:02d} eur"
            val = str(money1 + money2)
            stmt = "print(money1 + money2)"
            met_name = "__add__"

            self.assertEqual(val, corr, f'Expression\n{stmt}\nshould be ' +
                f'{corr},  when objects are initialized as:\n'
                f'money1 = Money({tc1[0]}, {tc1[1]})\n' + 
                f'money2 = Money({tc2[0]}, {tc2[1]})\n' + 
                f'Now expression returns {val}.\n' + 
                f'Check the method {met_name}')

    @points('10.money_part4')
    def test_8a_minus1(self):
        from src.money import Money
        test_cases = [((3,0), (1,0)), ((2,50),(1,50)), ((4,5),(0,50)), ((15,95),(1,55)),
            ((2,0), (1,35)), ((4,30), (2,75)), ((3,95),(3,90)), ((1110,10),(1110,0))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            money1 = Money(tc1[0], tc1[1])
            money2 = Money(tc2[0], tc2[1])

            e = tc1[0] - tc2[0]
            c = tc1[1] - tc2[1]
            if c < 0:
                c += 100
                e -= 1
            corr = f"{e}.{c:02d} eur"
            val = str(money1 - money2)
            stmt = "print(money1 - money2)"
            met_name = "__sub__"

            self.assertEqual(val, corr, f'Expression\n{stmt}\nshould be ' +
                f'{corr},  when objects are initialized as:\n'
                f'money1 = Money({tc1[0]}, {tc1[1]})\n' + 
                f'money2 = Money({tc2[0]}, {tc2[1]})\n' + 
                f'Now expression returns {val}.\n' + 
                f'Check the method {met_name}')

    @points('10.money_part4')
    def test_8b_minus2(self):
        from src.money import Money
        test_cases = [((1,0), (2,0)), ((2,50),(3,50)), ((4,5),(4,6)), ((15,95),(15,96)),
            ((2,0), (2,1)), ((1110,10),(1110,11))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            money1 = Money(tc1[0], tc1[1])
            money2 = Money(tc2[0], tc2[1])

            
            
            stmt = "print(money1 - money2)"
            met_name = "__sub__"

            try:
                str(money1 - money2)
                self.fail(f'Expression\n{stmt}\nshould throw an error ' +
                    f'ValueError, when the objects were initialized as:\n'
                    f'money1 = Money({tc1[0]}, {tc1[1]})\n' + 
                    f'money2 = Money({tc2[0]}, {tc2[1]})\n' + 
                    f'Check the method {met_name}')
            except ValueError:
                pass

    @points('10.money_part5')
    def test_9_encapsulation(self):
        from src.money import Money
        ref = reflect.Reflect()
        r = Money(1,50)
        ref.set_object(r)

        attr = ref.list_attributes(True)
        for att in attr:
            if not att.startswith("_"):
                self.fail('Class should not have public attributes. ' +
                    f'\nNow it has a public attribute {att}')

        r.euros = 1000        
        test = "1000.50 eur"
        self.assertTrue(str(r) != test, f'Expression money.euros = 1000 should ' + 
        f'not set the value of Money type objec money.\n The attribute should be protected!')

        


    
    
if __name__ == '__main__':
    unittest.main()
