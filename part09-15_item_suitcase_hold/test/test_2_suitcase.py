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

class SuitcaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected.")]):
           cls.module = load_module(exercise, 'en')

    @points('8.item_suitcase_hold_part2')
    def test1_suitcase_exists(self):
        try:
            from src.code import Suitcase
        except:
            self.assertTrue(False, "Your program should contain class named Suitcase")

    @points('8.item_suitcase_hold_part2')
    def test2_suitcase_constructor(self):
        try:
            from src.code import Suitcase
            suitcase = Suitcase(25)
        except Exception as e:
            self.assertTrue(False, 'Calling constructor of the class Suitcase as follows Suitcase(25)' +
                f' threw an error: {e}\nMake sure, that the constructor is defined properly.')

    @points('8.item_suitcase_hold_part2')
    def test3_empty_suitcase_str(self):
            from src.code import Suitcase
            suitcase = Suitcase(25)

            corr1 = "0 items (0 kg)"
            val = str(suitcase)

            self.assertTrue(corr1 == val, f"Method __str__ should return a string\n{corr1}\nwhen object is initialized as follows\n" + 
                f'Suitcase(25)\nNow method returns a string\n{val}')

    @points('8.item_suitcase_hold_part2')
    def test4_suitcase_add_item(self):
        try:
            from src.code import Item
            from src.code import Suitcase
            code = """
suitcase = Suitcase(25)
item = Item("ABC Book", 2)
suitcase.add_item(item)
"""
            item = Item("ABC Book", 2)
            suitcase = Suitcase(25)
            suitcase.add_item(item)

        except Exception as e:
            self.assertTrue(False, f'Executing the following code\n{code}\n threw an error\n{e}\nIs method add_item(self, item) defined?')

        corr0 = "1 items (2 kg)"
        corr1 = "1 item (2 kg)"
        val = str(suitcase)

        self.assertTrue(corr1 == val or corr0 == val, f"Suitcase\'s method __str__ should return a string\n{corr1}\nwhen the following code is executed\n{code}\n" + 
            f'Now method returns a string\n{val}')       

        corr0 = "1 items (2 kg)"
        corr1 = "1 item (2 kg)"
        val = str(suitcase)

        self.assertTrue(corr1 == val or corr0 == val, f"Suitcase\'s method __str__ should return a string\n{corr1}\nwhen the following code is executed\n{code}\n" + 
            f'Now method returns a string\n{val}')       

        item2 = Item("Brick", 5)
        try:
            suitcase.add_item(item2)
        except:
            self.fail(f"Make sure, that executing following code works\n{code}")

        code += """item2 = Item("Brick", 5)
suitcase.add_item(item2)
"""

        corr1 = "2 items (7 kg)"
        val = str(suitcase)

        self.assertTrue(corr1 == val, f"Suitcase\'s method __str__ should return a string\n{corr1}\nwhen the following code is executed\n{code}\n" + 
            f'Now method returns a string\n{val}')               

        item3 = Item("iPhone", 1)
        suitcase.add_item(item3)

        code += """item3 = Item("iPhone", 1)
suitcase.add_item(item3)
"""

        corr1 = "3 items (8 kg)"
        val = str(suitcase)

        self.assertTrue(corr1 == val, f"Suitcase\'s method __str__ should return a string\n{corr1}\nwhen the following code is executed\n{code}\n" + 
            f'Now method returns a string\n{val}')               

    @points('8.item_suitcase_hold_part2')
    def test5_suitcase_can_not_be_overloaded(self):
        from src.code import Item
        from src.code import Suitcase
        code = """
suitcase = Suitcase(4)
item = Item("Encyclopedia", 5)
suitcase.add_item(item)
"""

        suitcase = Suitcase(4)
        item = Item("Encyclopedia", 5)
        suitcase.add_item(item)

        corr1 = "0 items (0 kg)"
        val = str(suitcase)

        self.assertTrue(corr1 == val, f"Suitcase\'s method __str__ should return a string\n{corr1}\nwhen the following code is executed\n{code}\n" + 
            f'Now method returns a string\n{val}\nNote, that it is not allowed to add more items to the suitcase than it\'s capacity is!')       

        code = """
suitcase = Suitcase(3)
item1 = Item("Rock", 1)
item2 = Item("Energy drink", 1)
suitcase.add_item(item1)
suitcase.add_item(item2)
item3 = Item("Sledgehammer", 2)
suitcase.add_item(item3)
"""    

        suitcase = Suitcase(3)
        item1 = Item("Rock", 1)
        item2 = Item("Energy drink", 1)
        suitcase.add_item(item1)
        suitcase.add_item(item2)
        item3 = Item("Sledgehammer", 2)
        suitcase.add_item(item3)

        corr1 = "2 items (2 kg)"
        val = str(suitcase)

        self.assertTrue(corr1 == val, f"Suitcase\'s method __str__ should return a string\n{corr1}\nwhen the following code is executed\n{code}\n" + 
            f'Now method returns a string\n{val}\nNote, that it is not allowed to add more items to the suitcase than it\'s capacity is!')       

    @points('8.item_suitcase_hold_part3')
    def test6_suitcase_with_one_item(self):

        from src.code import Item
        from src.code import Suitcase
        code = """
suitcase = Suitcase(25)
item = Item("ABC Book", 2)
suitcase.add_item(item)
"""
        item = Item("ABC Book", 2)
        suitcase = Suitcase(25)
        suitcase.add_item(item)

        corr1 = "1 item (2 kg)"
        val = str(suitcase)

        self.assertTrue(corr1 == val, f"Suitcase\'s method __str__ should return a string\n{corr1}\nwhen the following code is executed\n{code}\n" + 
            f'Now method returns a string\n{val}\nRead carefully assimgments of part 3!')    

    @points('8.item_suitcase_hold_part4')
    def test6_suitcase_weight(self):
        try:
            from src.code import Item
            from src.code import Suitcase
            code = """
suitcase = Suitcase(25)
item = Item("ABC Book", 2)
suitcase.add_item(item)
suitcase.weight()
"""

            suitcase = Suitcase(25)
            item = Item("ABC Book", 2)
            suitcase.add_item(item)
            weight = suitcase.weight()

        except Exception as e:
            self.assertTrue(False, f'Executing the following code\n{code}\n threw an error\n{e}\nIs method weight(self) defined?')
         
        self.assertTrue(weight == 2, f'When executing the following code\n{code}\nmethod should return 2, but the return value was {weight}')

        code = """
suitcase = Suitcase(25)
item1 = Item("Rock", 1)
item2 = Item("Energy drink", 1)
suitcase.add_item(item1)
suitcase.add_item(item2)
item3 = Item("Sledgehammer", 2)
suitcase.add_item(item3)
weight = suitcase.weight()
"""

        suitcase = Suitcase(25)
        item1 = Item("Rock", 1)
        item2 = Item("Energy drink", 1)
        suitcase.add_item(item1)
        suitcase.add_item(item2)
        item3 = Item("Sledgehammer", 2)
        suitcase.add_item(item3)
        weight = suitcase.weight()
        self.assertTrue(weight == 4, f'When executing the following code\n{code}\nmethod should return 4, but the return value was {weight}')

    @points('8.item_suitcase_hold_part4')
    def test6_suitcase_print_items(self):
        try:
            from src.code import Item
            from src.code import Suitcase
            code = """
suitcase = Suitcase(25)
item = Item("ABC Book", 2)
suitcase.add_item(item)
suitcase.print_items()
"""

            suitcase = Suitcase(25)
            item = Item("ABC Book", 2)
            suitcase.add_item(item)
            suitcase.print_items()

        except Exception as e:
            self.assertTrue(False, f'Executing the following code\n{code}\n threw an error\n{e}\nIs method print_items(self) defined?')
         
        out = get_stdout()
        self.assertTrue(0<len(out), f'When executing the following code\n{code}\nmethod should print out one row\nNow it does not print out anything')
       
        lines = [x for x in out.split('\n') if len(x)>0]
        self.assertTrue(1 == len(lines), f'When executing the following code\n{code}\nmethod should print out one row\nThe print out was\n{out}')

        expected = "ABC Book (2 kg)"
        self.assertTrue(out == expected, f'When executing the following code\n{code}\nmethod should print out\n{expected}\nThe print out was\n{out}')

    @points('8.item_suitcase_hold_part4')
    def test7_matkasuitcase_print_items2(self):
        try:
            from src.code import Item
            from src.code import Suitcase
            code = """
suitcase = Suitcase(25)
item1 = Item("Rock", 1)
item2 = Item("Energy drink", 1)
suitcase.add_item(item1)
suitcase.add_item(item2)
item3 = Item("Sledgehammer", 2)
suitcase.add_item(item3)
"""

            suitcase = Suitcase(25)
            item1 = Item("Rock", 1)
            item2 = Item("Energy drink", 1)
            suitcase.add_item(item1)
            suitcase.add_item(item2)
            item3 = Item("Sledgehammer", 2)
            suitcase.add_item(item3)
            suitcase.print_items()

        except Exception as e:
            self.assertTrue(False, f'Executing the following code\n{code}\n threw an error\n{e}\nIs method print_items(self) defined?')
         
        out = get_stdout()
        lines = [x for x in out.split('\n') if len(x)>0]
        self.assertTrue(3 == len(lines), f'When executing the following code\n{code}\nmethod should print out three rows\nThe print out was\n{out}')

        tt = [ f"{t}" for t in [item1, item2, item3]]
        expected = "\n".join(tt)

        self.assertTrue(sorted(lines) == sorted(tt), f'When executing the following code\n{code}\nmethod should print out\n{expected}\nThe print out was\n{out}')

    @points('8.item_suitcase_hold_part5')
    def test9_suitcase_heaviest_item(self):
        try:
            from src.code import Item
            from src.code import Suitcase
            code = """
suitcase = Suitcase(25)
item = Item("ABC Book", 2)
suitcase.add_item(item)
suitcase.heaviest_item()
"""

            suitcase = Suitcase(25)
            item = Item("ABC Book", 2)
            suitcase.add_item(item)
            try:
                r = suitcase.heaviest_item()
            except:
                self.fail(f"Make sure, that executing following code works\n{code}")

        except Exception as e:
            self.assertTrue(False, f'Executing the following code\n{code}\n threw an error\n{e}\nIs method heaviest_item(self) defined?')
        
        try:
           r.name() 
        except:
            code2 = """
suitcase = Suitcase(25)
item = Item("ABC Book", 2)
suitcase.add_item(item)
heaviest = suitcase.heaviest_item()
print(heaviest.name())
"""
            self.fail(f"Does method heaviest_item(self) return object of correct type? Make sure, that executing following code works\n{code2}")

        self.assertTrue(r.name() == "ABC Book", f'When executing the following code\n{code}\nmethod should return {item}, but the return value was {r}')

    @points('8.item_suitcase_hold_part5')
    def test10_matkasuitcase_heaviest_item_2(self):
        from src.code import Item
        from src.code import Suitcase
        code = """
suitcase = Suitcase(25)
item1 = Item("ABC Book", 2)
suitcase.add_item(item1)
item2 = Item("Hammer", 10)
suitcase.add_item(item2)
item3 = Item("Rock", 3)
suitcase.add_item(item3)
suitcase.heaviest_item()
"""

        suitcase = Suitcase(25)
        item1 = Item("ABC Book", 2)
        suitcase.add_item(item1)
        item2 = Item("Hammer", 10)
        suitcase.add_item(item2)
        item3 = Item("Rock", 3)
        suitcase.add_item(item3)
        try:
            r = suitcase.heaviest_item()
        except:
            self.fail(f"Make sure, that executing following code works\n{code}")

        self.assertTrue(r.name() == "Hammer", f'When executing the following code\n{code}\nmethod should return {item2}, but the return value was {r}')

if __name__ == '__main__':
    unittest.main()
