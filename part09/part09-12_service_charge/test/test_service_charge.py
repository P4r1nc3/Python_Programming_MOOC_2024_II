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

exercise = 'src.service_charge'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('9.service_charge')
class ServiceChargeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected.")]):
           cls.module = load_module(exercise, 'en')

    
    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_1_class_exists(self):
        try:
            from src.service_charge import BankAccount
            a = BankAccount("Test","12345",1.0)
        except Exception as e:
            self.fail(f'Calling constructor BankAccount("Test","12345",1.0) threw an error \n{e}\n' + 
            'Make sure, that class is defined.')

    def test_2_methods_exists(self):
        from src.service_charge import BankAccount
        a = BankAccount("Test","12345",1.0)
        try:
             val = a.balance
             taip = str(type(val)).replace("<class '","").replace("'>","")
             self.assertTrue(type(val) == float, f'Getter method balance should return an integer. ' +
                f'Now it returns a value {val} which is of type {taip}.')
        except Exception as e:
            self.fail(f'Program\nBankAccount("Test","12345",1.0)\ns = a.balance\n threw an error \n{e}')
        try:
             a.deposit(1.0)       
        except Exception as e:
            self.fail(f'Program\nBankAccount("Test","12345",1.0)\na.deposit(1.0)\n threw an error \n{e}')

        try:
             a.withdraw(1.0)       
        except Exception as e:
            self.fail(f'Program\nBankAccount("Test","12345",1.0)\na.withdraw(1.0)\n threw an error \n{e}')

    def test3_test_attributes(self):
        from src.service_charge import BankAccount
        a = BankAccount("Test","12345",1.0)
        ref = reflect.Reflect()
        ref.set_object(a)

        att_list = ["balance","deposit","withdraw"]
        for attribute in att_list:
            self.assertTrue(ref.has_attribute(attribute), f'Class BankAccount should have attribute ' + 
                f'{attribute}.')

        att = ref.list_public_members()
        att.remove("balance")
        att.remove("deposit")
        att.remove("withdraw")

        self.assertEqual(len(att), 0, f'Class BankAccount should not have other public members than ' +
            f'methods balance, deposit and withdraw.' +  
            f'\nNow, however, it have following public members:'+ f(att))

        self.assertTrue(ref.has_attribute("_BankAccount__service_charge"), f'Class should have private method ' +
            f'__service_charge(self)')

    def test4_test_deposit(self):
        from src.service_charge import BankAccount
        a = BankAccount("Test","12345",0)
        test_cases = [10, 10, 20]
        tests = ""
        corr = 0
        for test_case in test_cases:
            a.deposit(test_case)
            corr += test_case
            corr *= 0.99
            tests += f"\ndeposit({test_case})"

            self.assertAlmostEqual(a.balance, corr, 2, f'Balance should be {corr} when the class has been initialized as follows:\n' +
                f'BankAccount("Test","12345",0)' + 
                f'\nand method deposit has been called ' + 
                f'as follows:\n{tests}\nNow balance is {a.balance}')

    def test5_test_withdraw(self):
        from src.service_charge import BankAccount
        a = BankAccount("Test","12345",100)
        test_cases = [5, 10, 10]
        tests = ""
        corr = 100
        for test_case in test_cases:
            a.withdraw(test_case)
            corr -= test_case
            corr *= 0.99
            tests += f"\nwithdraw({test_case})"

            self.assertAlmostEqual(a.balance, corr, 2, f'Balance should be {corr} when the class has been initialized as follows:\n' +
                f'BankAccount("Test","12345",0)' + 
                f'\nand method withdraw has been called' + 
                f'as follows:\n{tests}\nNow balance is {a.balance}')

if __name__ == '__main__':
    unittest.main()
