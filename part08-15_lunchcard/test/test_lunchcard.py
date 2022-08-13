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

exercise = 'src.lunchcard'
classname = "LunchCard"

def f(attr: list):
    return ",".join(attr)

class LunchCardTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_ok(self):
        with open("src/lunchcard.py") as t:
            if "if __name__" in t.read():
                self.fail('Main program must NOT be included inside if __name__ == "__main__": block')

    @points('8.lunchcard_part1')
    def test1_class_exists(self):
        try:
            from src.lunchcard import LunchCard
        except:
            self.fail("Your program should contain a class called LunchCard")

    @points('8.lunchcard_part1')
    def test2_constructor(self):
        try:
            from src.lunchcard import LunchCard
            card = LunchCard(100)
            self.assertTrue(True, "")
        except Exception as e:
            self.fail('Calling constructor LunchCard(100)' +
                f' threw an error: {e}\n')

    @points('8.lunchcard_part1')
    def test3_test_str(self):
        test_cases = (100, 25, 0, 10, 23)
        for test_case in test_cases:
            try:
                from src.lunchcard import LunchCard
                card = LunchCard(test_case)

                corr = f'The balance is {test_case:.1f} euros'
                val = str(card)

                self.assertEqual(corr, val, f"Method __str__ should return string\n{corr}\nwhen object was initialized as\n" + 
                    f"LunchCard({test_case})\nNow method returns\n{val}")

            except Exception as e:
                self.fail(f'Calling method __str__ threw an error: {e}\nwhen object was initializeds as\nLunchCard({test_case})')

    @points('8.lunchcard_part2')
    def test4_eat_lunch_exists(self):
        try:
            from src.lunchcard import LunchCard 
            code = """
card = LunchCard(10)
card.eat_lunch()"""

            card = LunchCard(10)
            card.eat_lunch()  

        except Exception as e:
            self.fail(f'Executing code\n{code}\nthrew an error\n{e}\nCheck that the method eat_lunch(self) is defined?')

    @points('8.lunchcard_part2')
    def test5_eat_lunch(self):
            from src.lunchcard import LunchCard
            money = 7
            code = """
card = LunchCard(7)
card.eat_lunch()
"""

            card = LunchCard(money)
            card.eat_lunch()

            money -= 2.6
            corr = f'The balance is {money:.1f} euros'
            val = str(card)

            self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwhen code executed is\n{code}\n" + 
                f"Now method returns\n{val}")

            card.eat_lunch()
            code += "card.eat_lunch()\n"
            money -= 2.6
            corr = f'The balance is {money:.1f} euros'
            val = str(card)
            self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwhen code executed is\n{code}\n" + 
                f"Now method returns\n{val}")
            
            card.eat_lunch()
            code += "card.eat_lunch()\n"
            corr = f'The balance is {money:.1f} euros'
            val = str(card)
            self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwhen code executed is\n{code}\n" + 
                f"Now method returns\n{val}")

    @points('8.lunchcard_part2')
    def test6_eat_special_exists(self):
        try:
            from src.lunchcard import LunchCard 
            code = """
card = LunchCard(10)
card.eat_special()"""

            card = LunchCard(10)
            card.eat_special()  

        except Exception as e:
            self.fail(f'Executing code\n{code}\nthrew an error\n{e}\nCheck that the method eat_special(self) is defined?')

    @points('8.lunchcard_part2')
    def test7_eat_special(self):
            from src.lunchcard import LunchCard
            money = 10
            code = """
card = LunchCard(10)
card.eat_special()
"""

            card = LunchCard(money)
            card.eat_special()

            money -= 4.6
            corr = f'The balance is {money:.1f} euros'
            val = str(card)

            self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwhen code executed is\n{code}\n" + 
                f"Now method returns\n{val}")
            
            card.eat_special()
            code += "card.eat_special()\n"
            money -= 4.6
            corr = f'The balance is {money:.1f} euros'
            val = str(card)
            self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwhen code executed is\n{code}\n" + 
                f"Now method returns\n{val}")
            
            card.eat_special()
            code += "card.eat_special()\n"
            corr = f'The balance is {money:.1f} euros'
            val = str(card)
            self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwhen code executed is\n{code}\n" + 
                f"Now method returns\n{val}")

    @points('8.lunchcard_part3')
    def test8_deposit_money_exists(self):
        try:
            from src.lunchcard import LunchCard 
            code = """
card = LunchCard(10)
card.deposit_money(5)"""

            card = LunchCard(10)
            card.deposit_money(5)  

        except Exception as e:
            self.fail(f'Executing code\n{code}\nthrew an error\n{e}\nCheck that the method deposit_money(self, money: int) is defined?')

    @points('8.lunchcard_part3')
    def test9_deposit_money(self):
            from src.lunchcard import LunchCard
            money = 10
            code = """
card = LunchCard(10)
card.deposit_money(5)
"""

            card = LunchCard(10)
            card.deposit_money(5)  

            money += 5
            corr = f'The balance is {money:.1f} euros'
            val = str(card)

            self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwhen code executed is\n{code}\n" + 
                f"Now method returns\n{val}")

            card.deposit_money(75)  
            code += "card.deposit_money(75)\n"
            money += 75
            corr = f'The balance is {money:.1f} euros'
            val = str(card)

            self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwhen code executed is\n{code}\n" + 
                f"Now method returns\n{val}")


            card.deposit_money(20)  
            code += "card.deposit_money(20)\n"
            money += 20
            corr = f'The balance is {money:.1f} euros'
            val = str(card)

            self.assertEqual(corr, val, f"Method __str__ should return a string\n{corr}\nwhen code executed is\n{code}\n" + 
                f"Now method returns\n{val}")

    @points('8.lunchcard_part3')
    def test10_deposit_money_negative(self):
            from src.lunchcard import LunchCard
            money = 10
            code = """
card = LunchCard(10)
card.deposit_money(-25)
"""

            ok = False
            card = LunchCard(10)
            try:
                card.deposit_money(-25)  
            except ValueError:
                money += 5
                ok = True
                
            self.assertTrue(ok, f"Executing code\n{code}\nshould throw a ValueError")

    @points('8.lunchcard_part4')
    def test11_main_program(self):
        try:
            reload_module(self.module)
            output_all = get_stdout()
        except:
            self.fail(f"Check that your program can be executed!")

        mssage = """\nNote, that in this exercise, NO CODE should be included inside
if __name__ == "__main__":
block
        """

        self.assertTrue(len(output_all)>0, f"Your program does not output anything!\n{mssage}")  
        output = [line.strip() for line in output_all.split("\n") if len(line) > 0]

        correct = [
            "Peter: The balance is 15.4 euros",
            "Grace: The balance is 27.4 euros",
            "Peter: The balance is 35.4 euros",
            "Grace: The balance is 22.8 euros",
            "Peter: The balance is 30.2 euros",
            "Grace: The balance is 72.8 euros"
        ]

        self.assertTrue(len(correct) == len(output),f"Your program should output {len(correct)} lines, now it outputs {len(output)} lines. Output was\n{output_all}")

        for i in range(0, len(correct)):
            t = output[i]
            o = correct[i]
            self.assertTrue(t == o,f"The output of your program at line {i+1} is incorrect. It should be\n{o}\nNow it is\n{t}\nThe whole output is\n{output_all}")               

    @points('8.lunchcard_part4')
    def test12_main_program_2(self):

        src_file = os.path.join('src', 'lunchcard.py')
        forbidden = [
            "Peter: The balance is 15.4 euros",
            "Grace: The balance is 27.4 euros",
            "Peter: The balance is 35.4 euros",
            "Grace: The balance is 22.8 euros",
            "Peter: The balance is 30.2 euros",
            "Grace: The balance is 72.8 euros"
        ]        
        with open(src_file) as f:
            for line in f:
                for k in forbidden:
                    if k in line:
                        self.fail(f"You must use LunchCard class in the exercise, the following line is forbidden:\n{line}")                

        required = [
            "LunchCard(20)",
            ".eat_lunch()",
            ".eat_special()",
            ".deposit_money(20)"
        ]
        lines = []
        with open(src_file) as f:
            for line in f:
                lines.append(line)
    
        for v in required:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"You must use LunchCard class in the exercise, the following line must be included:\n{v}")   

if __name__ == '__main__':
    unittest.main()

   
