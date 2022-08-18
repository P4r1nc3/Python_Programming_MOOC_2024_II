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

exercise = 'src.order_book'

def f(attr: list):
    return ",".join(attr)

def s(l: list):
    return "\n".join(l)

def ss(l: list):
    return "\n".join([f'{s}' for s in l])

def tt(x):
    status = "NOT FINISHED" if not x[3] else "FINISHED"
    return f"{x[0]} ({x[1]} hours), programmer {x[2]} {status}"

def ook(val, tt):
    if len(val) != len(tt):
        return False
    for v in val:
        ouk = False
        for t in tt:
            if ok(v, t[0], t[1], t[2], t[3]):
                ouk = True
        if not ouk:
            return False
    
    return True
        
def ok(task, description, programmer, workload, status=False):
    return task.description == description and task.programmer == programmer and task.workload == workload and task.is_finished() == status

@points('11.order_book_part4')
class OrderBookPart4Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'en')

    def test_1_status_of_programmer(self):
        reload_module(self.module)
        from src.order_book import OrderBook, Task
        code = """
t = OrderBook()
t.add_order("program webstore", "Andy", 10)
t.status_of_programmer("Andy")
"""
        t = OrderBook()
        t.add_order("program webstore", "Andy", 10)
        try:
            val = t.status_of_programmer("Andy")
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method status_of_programmer(self, programmer: str) defined?')
        
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == type(()), f"When executing the following code{code}type of return value should be tuple, now it is of type {taip}")

        expected = 4
        self.assertTrue(len(val)==expected, f"When executing the following code{code}\nmethod should return a tuple, which length is {expected}, length of list was {len(val)}")
        valx = val
        for i in [0,1,2,3]:
            val = valx[i]
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == type(1), f"When executing the following code{code}palautetun tuplen pitäisi sisältää kokonaislukuja, nyt mukana on arvo, jonka tyyppi on {taip}. Palautettu tuple on {valx}")    
        
        val = valx
        expected = (0, 1, 0, 10)
        self.assertTrue(val==expected, f"When executing the following code {code}\nexpected return is {expected}, now return was {val}")

    def test_2_status_of_programmer(self):
        reload_module(self.module)
        from src.order_book import OrderBook, Task
        code = """
t = OrderBook()
t.add_order("program webstore", "Andy", 10)
t.add_order("program mobile app", "Andy", 5)
t.add_order("program something with pygame", "Andy", 50)
t.add_order("code better facebook", "Jonas", 5000)
t.mark_finished(1)
t.mark_finished(2)
t.status_of_programmer("Andy")
"""
        t = OrderBook()
        t.add_order("program webstore", "Andy", 10)
        t.add_order("program mobile app", "Andy", 5)
        t.add_order("program something with pygame", "Andy", 50)
        t.add_order("code better facebook", "Jonas", 5000)

        til = t.all_orders()
        id1 = til[0].id
        id2 = til[1].id

        try:
            t.mark_finished(id1)
            t.mark_finished(id2)
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method mark_finished(self, id: int) defined?')
       
        try:
            val = t.status_of_programmer("Andy")
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method status_of_programmer(self, programmer: str) defined?')
        
        expected =  (2, 1, 15, 50)
        self.assertTrue(val==expected, f"When executing the following code {code}\nexpected return is {expected}, now return was {val}")

    def test_4_status_of_programmer_raise_expection(self):
        reload_module(self.module)
        from src.order_book import OrderBook, Task
        code = """
t = OrderBook()
t.add_order("program webstore", "Andy", 10)
t.status_of_programmer("JohnDoe")
"""
        t = OrderBook()
        t.add_order("program webstore", "Andy", 10)
        ok = False
        try:
            val = t.status_of_programmer("JohnDoe")
        except ValueError:
            ok = True
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}')
        self.assertTrue(ok, f'Executing the following code {code}should raise ValueError exception')

if __name__ == '__main__':
    unittest.main()