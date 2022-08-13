import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date

exercise = 'src.three_classes'

def f(attr: list):
    return ",".join(attr)

@points('8.three_classes')
class ThreeClassesTest(unittest.TestCase):
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

    def test1_classes_exist(self):
        try:
            from src.three_classes import Checklist
        except:
            self.fail("Your program should have a class called Checklist")

        try:
            from src.three_classes import Customer
        except:
            self.fail("Your program should have a class called Customer")

        try:
            from src.three_classes import Cable
        except:
            self.fail("Your program should have a class called Cable")

    def test2_costructors(self):
        try:
            from src.three_classes import Checklist
            val = Checklist("list", [])
        except Exception as e:
            self.assertTrue(False, 'Constructor call Checklist("list", [])' +
                f' threw an error: {e}')
        try:
            from src.three_classes import Customer
            val = Customer("Customer",1,1.0)
        except Exception as e:
            self.assertTrue(False, 'Constructor call Customer("Customer",1,1.0)' +
                f' threw an error: {e}')

        try:
            from src.three_classes import Cable
            val = Cable("Cable",1.0,1,True)
        except Exception as e:
            self.assertTrue(False, 'Constructor call Cable("Cable",1.0,1.True)' +
                f' threw an error: {e}')

    
    def test3_test_attributes(self):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
            reload_module(self.module)
            from src.three_classes import Checklist, Customer, Cable

            attributes = ("header","entries")
            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(Checklist("list",[]))

                self.assertTrue(ref.has_attribute(attr), f"The object should have an attribute {attr}," +  
                    f'\nnow attributes are\n{f(ref.list_attributes(True))}\nwhen constructor was called with' + 
                    f'Checklist("list",[])')

            attributes = ("id", "balance", "discount")
            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(Customer("customer", 1.0, 1))

                self.assertTrue(ref.has_attribute(attr), f"The object should have an attribute {attr}," +  
                    f'\nnow attributes are\n{f(ref.list_attributes(True))}\nwhen constructor was called with' + 
                    f'Customer("customer", 1.0, 1)')

            attributes = ("model", "length", "max_speed", "bidirectional")
            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(Cable("Cable",1.0,1,True))

                self.assertTrue(ref.has_attribute(attr), f"The object shoul have an attribute {attr}," +  
                    f'\nnow attributes are\n{f(ref.list_attributes(True))}\nwhen constructor was called with' + 
                    f'Cable("Cable",1.0,1,True')

    
    def test4_test_checklist(self):
         test_cases = [("Bills", ["Remember rent", "Remember phone bill"]), 
                       ("Shopping list", ["Milk", "Bread", "Juice", "Butter"])]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Input was not excpected")]):
                reload_module(self.module)
                from src.three_classes import Checklist

                clist = Checklist(test_case[0], test_case[1])
                
                attributes = ("header", "entries")
                ref = reflect.Reflect()
                ref.set_object(clist)

                for i in range(len(attributes)):
                    value = ref.get_attribute(attributes[i])
                    self.assertEqual(value, test_case[i], 
                        f'The value of attribute {attributes[i]} should be {test_case[i]}, now it is {value},\n when arguments were \n{test_case}')

    def test5_test_customer(self):
         test_cases = [("Caleb Customer", 1424.50, 10), ("Ibrahim Imagination", 550.0, 7), ("Mary Madeup", 240.25, 15)]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
                reload_module(self.module)
                from src.three_classes import Customer

                customer = Customer(test_case[0], test_case[1], test_case[2])
                
                attributes = ("id", "balance", "discount")
                ref = reflect.Reflect()
                ref.set_object(customer)

                for i in range(len(attributes)):
                    value = ref.get_attribute(attributes[i])
                    self.assertEqual(value, test_case[i], 
                        f'The value of attribute {attributes[i]} should be {test_case[i]}, now it is {value},\n when arguments were \n{test_case}')

    def test6_test_cable(self):
         test_cases = [("cat", 5.0, 128, True), ("USB2", 10.0, 24, True), ("BSU3", 25.0, 18, False)]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
                reload_module(self.module)
                from src.three_classes import Cable

                cable = Cable(test_case[0], test_case[1], test_case[2], test_case[3])
                
                attributes = ("model", "length", "max_speed", "bidirectional")
                ref = reflect.Reflect()
                ref.set_object(cable)

                for i in range(len(attributes)):
                    value = ref.get_attribute(attributes[i])
                    self.assertEqual(value, test_case[i], 
                        f'The value of attribute {attributes[i]} should be {test_case[i]}, now it is {value},\n when arguments were \n{test_case}')


if __name__ == '__main__':
    unittest.main()
