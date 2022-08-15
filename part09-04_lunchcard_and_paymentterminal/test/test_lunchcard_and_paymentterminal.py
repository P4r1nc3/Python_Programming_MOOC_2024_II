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

exercise = 'src.lunchcard_and_paymentterminal'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 


class LunchCardJaPaymentTerminalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected.")]):
           cls.module = load_module(exercise, 'en')

    @points('9.lunchcard_and_paymentterminal_part1')
    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    @points('9.lunchcard_and_paymentterminal_part1')
    def test_1_luokka_LunchCard_olemassa(self):
        try:
            from src.lunchcard_and_paymentterminal import LunchCard
            h = LunchCard(1.0)
        except Exception as e:
            self.fail(f'Calling constructor LunchCard(1.0) threw an error \n{e}')
        try:
            h.deposit_money(1)
        except Exception as e:
            self.fail(f'Calling method deposit_money(1) threw an error \n{e}')
         

    @points('9.lunchcard_and_paymentterminal_part1')
    def test_2_stupid_card(self):
        test_cases = [(100,50), (100, 150), (200, 50, 100), (1000, 500, 600), 
            (500, 100, 200, 200, 100), (10, 2, 3, 2, 1, 3)]
        for test_case in test_cases:
            from src.lunchcard_and_paymentterminal import LunchCard
            card = LunchCard(test_case[0])
            corr_bool = []
            corr_saldo = [] 
            val_bool = [] 
            val_saldo = []
            saldo = test_case[0]

            for n in test_case[1:]:
                val_bool.append(str(card.subtract_from_balance(n)))
                val_saldo.append(str(card.balance))
                
                if saldo >= n:
                    saldo -= n
                    corr_bool.append(str(True))
                else:
                    corr_bool.append(str(False))
                corr_saldo.append(str(saldo))

            self.assertEqual(corr_bool, val_bool, f'Card was created with call LunchCard({test_case[0]}).\n'+
                f'After that method subtract_from_balance was called with value(s) {f(test_case[1:])}\n' +
                f'Method was expected to return {",".join(corr_bool)}\n' +
                f'but it returned {",".join(val_bool)}')

            self.assertEqual(corr_saldo, val_saldo, f'Card was created with call LunchCard({test_case[0]}).\n'+
                f'After that method subtract_from_balance was called with value(s) {f(test_case[1:])}\n' +
                f'Balance was expected to be {",".join(corr_saldo)}\n' +
                f'but it was {",".join(val_saldo)}')


    @points('9.lunchcard_and_paymentterminal_part2')
    def test_3a_class_PaymentTerminal_exists(self):
        try:
            from src.lunchcard_and_paymentterminal import PaymentTerminal
            h = PaymentTerminal()
        except Exception as e:
            self.fail(f'Calling constructor PaymentTerminal() threw an error \n{e}')

    @points('9.lunchcard_and_paymentterminal_part2')
    def test_3b_cash_payment(self):
        test_cases = [(10, True), (10,False), (50, True), (30, False), (100, True), (1, True), (1.50, False)]
        from src.lunchcard_and_paymentterminal import PaymentTerminal
        terminal = PaymentTerminal()
        
        op = "" 
        se = 0 
        sm = 0
        for test_case in test_cases:
            if test_case[1]:
                val = terminal.eat_lunch(test_case[0])
                corr = test_case[0]
                if test_case[0] >= 2.50:
                    corr -= 2.50
                    op += "\n" + "eat_lunch()"
                    se += 1
                self.assertEqual(corr,val,f'Method eat_lunch() is expected to return {corr}, ' +
                    f'when it is called with the parameter {test_case[0]}.\n' +
                    f'Now method did return {val}.')
            else:
                val = terminal.eat_special(test_case[0])
                corr = test_case[0]
                if test_case[0] >= 4.30:
                    corr -= 4.30
                    op += "\n" + "eat_special()"
                    sm += 1
                self.assertEqual(corr,val,f'Method eat_special() is expected to return {corr}, ' +
                    f'when it is called with the parameter {test_case[0]}.\n' +
                    f'Now method did return {val}.')

        self.assertEqual(terminal.lunches, se, f'Value of attribute lunches shold be {se}\n' +
            f'when methods were called as follows:{op}\nNow its value is {terminal.lunches}')
        
        self.assertEqual(terminal.specials, sm, f'Value of attribute specials shold be {sm}\n' +
            f'when methods were called as follows:{op}\nNow its value is {terminal.specials}')    

    @points('9.lunchcard_and_paymentterminal_part2')
    def test_3c_cash_payment_random(self):
        test_cases = []
        for i in range(randint(10,15)):
            test_cases.append((randint(1,9), randint(1,2) == 1))
        from src.lunchcard_and_paymentterminal import PaymentTerminal
        terminal = PaymentTerminal()
        
        op = "" 
        se = 0 
        sm = 0
        for test_case in test_cases:
            if test_case[1]:
                val = terminal.eat_lunch(test_case[0])
                corr = test_case[0]
                if test_case[0] >= 2.50:
                    corr -= 2.50
                    op += "\n" + "eat_lunch()"
                    se += 1
                self.assertEqual(corr,val,f'Method eat_lunch() is expected to return {corr}, ' +
                    f'when it is called with the parameter {test_case[0]}.\n' +
                    f'Now method did return {val}.')
            else:
                val = terminal.eat_special(test_case[0])
                corr = test_case[0]
                if test_case[0] >= 4.30:
                    corr -= 4.30
                    op += "\n" + "eat_special()"
                    sm += 1
                self.assertEqual(corr,val,f'Method eat_special() should return {corr}, ' +
                    f'when it is called with the parameter {test_case[0]}.\n' +
                    f'Now method did return {val}.')

        self.assertEqual(terminal.lunches, se, f'Value of attribute lunches shold be {se}\n' +
            f'when methods were called as follows:{op}\nNow its value is {terminal.lunches}')
        
        self.assertEqual(terminal.specials, sm, f'Value of attribute specials shold be {sm}\n' +
            f'when methods were called as follows:{op}\nNow its value is {terminal.specials}')   


    @points('9.lunchcard_and_paymentterminal_part3')
    def test_4_card_payments(self):
        test_cases = [(10, True), (20, False), (10, True, True), (10, False, False),
        (30, False, False, False, True, True), (5, True, True, True), (10, False, False, False),
        (20, False, True, False, True, True, True, False)]

        for test_case in test_cases:
            from src.lunchcard_and_paymentterminal import PaymentTerminal, LunchCard
            terminal = PaymentTerminal()
            card = LunchCard(test_case[0])
            saldo = test_case[0]
            op = f"LunchCard({test_case[0]})"
            se = 0 
            sm = 0

            for event in test_case[1:]:
                orig_saldo = saldo
                if event:
                    terminal.eat_lunch_lunchcard(card)
                    if saldo >= 2.50:
                        saldo -= 2.50
                        op += "\neat_lunch_lunchcard()"
                        se += 1
                    self.assertEqual(saldo, card.balance, f'Balance of the card should be {saldo}, when it was {orig_saldo},' + 
                        f' and method eat_lunch_lunchcard was called. But balance is now {card.balance}')
                else:
                    terminal.eat_special_lunchcard(card)
                    if saldo >= 4.30:
                        saldo -= 4.30
                        op += "\neat_special_lunchcard()"
                        sm += 1
                    self.assertEqual(saldo, card.balance, f'Balance of the card should be {saldo}, when it was {orig_saldo},' + 
                        f' and method eat_lunch_lunchcard was called. But balance is now {card.balance}') 
            
            self.assertEqual(terminal.lunches, se, f'Value of attribute lunches shold be {se}\n' +
            f'when methods were called as follows:{op}\nNow its value is {terminal.lunches}')
        
        self.assertEqual(terminal.specials, sm, f'Value of attribute specials shold be {sm}\n' +
            f'when methods were called as follows:{op}\nNow its value is {terminal.specials}')  

    @points('9.lunchcard_and_paymentterminal_part4')
    def test_5_deposit_money(self):
        test_cases = [(0, 10), (10, 30), (100, 100), (10, 2000), (5, 5.50), (2.50, 172.25)]
        for test_case in test_cases:
            from src.lunchcard_and_paymentterminal import PaymentTerminal, LunchCard
            terminal = PaymentTerminal()
            card = LunchCard(test_case[0])
            terminal.deposit_money_on_card(card, test_case[1])
            corr = sum(test_case)
            val = card.balance

            self.assertEqual(val, corr, f'Balance of the card should be {corr}, when in the beginning it was {test_case[0]}\n' + 
                f'and method deposit_money_on_card({test_case[1]}) was called.\n' +
                f'But balance is now {val}.')
                
if __name__ == '__main__':
    unittest.main()
