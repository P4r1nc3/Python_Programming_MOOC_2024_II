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

exercise = 'src.code'

def f(attr: list):
    return ",".join(attr)

class CargoHoldTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected.")]):
           cls.module = load_module(exercise, 'en')

    @points('8.item_suitcase_hold_part6')
    def test1_cargo_hold_exists(self):
        try:
            from src.code import CargoHold
        except:
            self.assertTrue(False, "your program should contain class named CargoHold")

    @points('8.item_suitcase_hold_part6')
    def test2_cargo_hold_constructor(self):
        try:
            from src.code import CargoHold
            hold = CargoHold(100)
        except Exception as e:
            self.assertTrue(False, 'Calling constructor of the class CargoHold as follows CargoHold(100)' +
                f' threw an error: {e}\nMake sure, that the constructor is defined properly.')

    @points('8.item_suitcase_hold_part6')
    def test3_empty_hold_str(self):
            from src.code import CargoHold
            hold = CargoHold(100)

            corr1 = "0 suitcases, space for 100 kg"
            val = str(hold)

            self.assertTrue(corr1 == val, f"Method __str__ should return a string\n{corr1}\nwhen object is initialized as follows\n" + 
                f'CargoHold(100)\nNow method returns a string\n{val}')

    @points('8.item_suitcase_hold_part6')
    def test4_hold_add_item(self):
        try:
            from src.code import Item
            from src.code import Suitcase
            from src.code import CargoHold
            hold = CargoHold(100)
            code = """
hold = CargoHold(100)
suitcase = Suitcase(25)
item = Item("ABC Book", 2)
suitcase.add_item(item)
hold.add_suitcase(suitcase)
"""
            hold = CargoHold(100)
            suitcase = Suitcase(25)
            item = Item("ABC Book", 2)
            suitcase.add_item(item)
            hold.add_suitcase(suitcase)

        except Exception as e:
            self.assertTrue(False, f'Executing the following code\n{code}\n threw an error\n{e}\nIs method add_suitcase(self, suitcase) defined?')

        corr1 = "1 suitcase, space for 98 kg"
        val = str(hold)

        self.assertTrue(corr1 == val, f"Method __str__ should return a string\n{corr1}\nwhen the following code is executed\n{code}\n" + 
            f'Now method returns a string\n{val}')     

        code = """
hold = CargoHold(50)
suitcase = Suitcase(25)
item = Item("ABC Book", 2)
suitcase.add_item(item)
hold.add_suitcase(suitcase)
suitcase2 = Suitcase(10)
suitcase2.add_item(Item("Rock", 1))
suitcase2.add_item(Item("Mouse", 2))
hold.add_suitcase(suitcase2)
"""

        hold = CargoHold(50)
        suitcase = Suitcase(25)
        item = Item("ABC Book", 2)
        suitcase.add_item(item)
        hold.add_suitcase(suitcase)
        suitcase2 = Suitcase(10)
        suitcase2.add_item(Item("Rock", 1))
        suitcase2.add_item(Item("Mouse", 2))
        hold.add_suitcase(suitcase2)

        corr1 = "2 suitcases, space for 45 kg"
        val = str(hold)

        self.assertTrue(corr1 == val, f"Method __str__ should return a string\n{corr1}\nwhen the following code is executed\n{code}\n" + 
            f'Now method returns a string\n{val}')     

    @points('8.item_suitcase_hold_part6')
    def test_5_hold_can_not_be_overloaded(self):
        try:
            from src.code import Item
            from src.code import Suitcase
            from src.code import CargoHold
            hold = CargoHold(100)
            code = """
hold = CargoHold(10)
suitcase = Suitcase(25)
item = Item("Anvil", 24)
suitcase.add_item(item)
hold.add_suitcase(suitcase)
"""
            hold = CargoHold(10)
            suitcase = Suitcase(25)
            item = Item("Anvil", 24)
            suitcase.add_item(item)
            hold.add_suitcase(suitcase)

        except Exception as e:
            self.assertTrue(False, f'Executing the following code\n{code}\n threw an error\n{e}\nIs method add_suitcase(self, suitcase) defined?')

        corr1 = "0 suitcases, space for 10 kg"
        val = str(hold)

        self.assertTrue(corr1 == val, f"Method __str__ should return a string\n{corr1}\nwhen the following code is executed\n{code}\n" + 
            f'Now method returns a string\n{val}\nNote, that it is not allowed to add more items to the cargo hold than it\'s capacity is!')    

    @points('8.item_suitcase_hold_part7')
    def test_6_hold_print_items(self):
        try:
            from src.code import Item
            from src.code import Suitcase
            from src.code import CargoHold
            hold = CargoHold(100)
            code = """
hold = CargoHold(100)
suitcase = Suitcase(25)
item = Item("ABC Book", 2)
suitcase.add_item(item)
hold.add_suitcase(suitcase)
hold.print_items()
"""
            hold = CargoHold(100)
            suitcase = Suitcase(25)
            item = Item("ABC Book", 2)
            suitcase.add_item(item)
            hold.add_suitcase(suitcase)
            hold.print_items()

        except Exception as e:
            self.assertTrue(False, f'Executing the following code\n{code}\n threw an error\n{e}\nIs method print_items(self) defined?')

        out = get_stdout()
        self.assertTrue(0<len(out), f'When executing the following code\n{code}\nmethod should print out one row\nNow it does not print out anything')
       
        lines = [x for x in out.split('\n') if len(x)>0]
        self.assertTrue(1 == len(lines), f'When executing the following code\n{code}\nmethod should print out one row\nThe print out was\n{out}')
       
        expected = "ABC Book (2 kg)"
        self.assertTrue(out == expected, f'When executing the following code\n{code}\nmethod should print out\n{expected}\nThe print out was\n{out}')

    @points('8.item_suitcase_hold_part7')
    def test_6_hold_print_items2(self):
        try:
            from src.code import Item
            from src.code import Suitcase
            from src.code import CargoHold
            hold = CargoHold(100)
            code = """
hold = CargoHold(50)
suitcase = Suitcase(25)
item = Item("ABC Book", 2)
suitcase.add_item(item)
hold.add_suitcase(suitcase)
suitcase2 = Suitcase(10)
suitcase2.add_item(Item("Rock", 1))
suitcase2.add_item(Item("Mouse", 2))
hold.add_suitcase(suitcase2)
hold.print_items()
"""

            hold = CargoHold(50)
            suitcase = Suitcase(25)
            item1 = Item("ABC Book", 2)
            suitcase.add_item(item1)
            hold.add_suitcase(suitcase)
            suitcase2 = Suitcase(10)
            item2 = Item("Rock", 1)
            suitcase2.add_item(item2)
            item3 =Item("Mouse", 2)
            suitcase2.add_item(item3)
            hold.add_suitcase(suitcase2)
            hold.print_items()

        except Exception as e:
            self.assertTrue(False, f'Executing the following code\n{code}\n threw an error\n{e}\nIs method print_items(self) defined?')

        out = get_stdout()
        self.assertTrue(0<len(out), f'When executing the following code\n{code}\nmethod should print out one row\nNow it does not print out anything')
       
        lines = [x for x in out.split('\n') if len(x)>0]
        self.assertTrue(3 == len(lines), f'When executing the following code\n{code}\nmethod should print out three rows\nThe print out was\n{out}')
       
        tt = [ f"{t}" for t in [item1, item2, item3]]
        expected = "\n".join(tt)
        self.assertTrue(sorted(lines) == sorted(tt), f'When executing the following code\n{code}\nmethod should print out\n{expected}\nThe print out was\n{out}')

if __name__ == '__main__':
    unittest.main()