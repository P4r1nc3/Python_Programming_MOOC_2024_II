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

@points('11.order_book_part2')
class OrderBookPart2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'en')

    def test_1_order_book_exists(self):
        reload_module(self.module)
        try:
            from src.order_book import OrderBook
        except:
            self.assertTrue(False, "Your program should contain class named OrderBook")
        try:
            OrderBook()
        except Exception as e:
            self.assertTrue(False, 'Calling constructor OrderBook()' +
                f' threw an error: {e}\nMake sure, that constructor is defined properly')
        
    def test_2_add_order_and_all_orders_exists(self):
        reload_module(self.module)
        from src.order_book import OrderBook,  Task
        code = """
t = OrderBook()
t.add_order("program web store", "Andy", 10)
"""
        t = OrderBook()
        try:
            t.add_order("program web store", "Andy", 10)
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method add_order(self, kuvaus, koodari, tyomaara) defined?')
        
        code = """
t = OrderBook()
t.all_orders()
"""
        t = OrderBook()
        try:
            t.all_orders()
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method all_orders(self) defined?')

        code = """
t = OrderBook()
t.add_order("program web store", "Andy", 10)
t.all_orders()
"""
        t = OrderBook()
        t.add_order("program web store", "Andy", 10)
        try:
            val = t.all_orders()
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method all_orders(self) defined?')

        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == type([]), f"When executing the following code {code}type of return value should be list, now it is of type {taip}")
        expected = 1
        self.assertTrue(len(val)==expected, f"When executing the following code{code}\nmethod should return a list, which length is {expected}, length of list was {len(val)}")
        
        ttt = Task("code hello world", "Eric", 3)
        taip = str(type(val[0])).replace("<class '","").replace("'>","")
        self.assertTrue(type(val[0]) == type(ttt), f"When executing the following code {code}type of first item in list returned should be Task, now it is of type {taip}")

    def test_3_add_order_and_all_orders_works(self):
        reload_module(self.module)
        from src.order_book import OrderBook, Task
        code = """
t = OrderBook()
t.add_order("program web store", "Andy", 10)
t.add_order("program mobile game", "Eric", 5)
t.all_orders()
"""
        t = OrderBook()
        t.add_order("program web store", "Andy", 10)
        t.add_order("program mobile game", "Eric", 5)
        try:
            val = t.all_orders()
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method all_orders(self) defined?')
        expected = 2
        self.assertTrue(len(val)==expected, f"When executing the following code{code}\nmethod should return a list, which length is {expected}, length of list was {len(val)}")

        t1 = ("program web store", "Andy", 10, False) 
        t2 = ("program mobile game", "Eric", 5, False) 
        all_ok = ook(val, [t1, t2])

        expected = s([tt(t1), tt(t2)])

        self.assertTrue(all_ok, f"When executing the following code{code}\nmethod should return a list containing following tasks\n{expected}\nnow list was{ss(val)}")

        code = """
t = OrderBook()
t.add_order("program web store", "Andy", 10)
t.add_order("program mobile game", "Eric", 5)
t.add_order("program better facebook", "Jonas", 5000)
t.all_orders()
"""

        
        t.add_order("program better facebook", "Jonas", 5000)
        try:
            val = t.all_orders()
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method all_orders(self) defined?')
        expected = 3
        self.assertTrue(len(val)==expected, f"When executing the following code{code}\nmethod should return a list, which length is {expected}, length of list was {len(val)}")

        t3 = ("program better facebook", "Jonas", 5000, False)
        all_ok = ook(val, [t1, t2, t3])

        expected = s([tt(t1), tt(t2),  tt(t3)])

        self.assertTrue(all_ok, f"When executing the following code{code}\nmethod should return a list containing following tasks\n{expected}\nnow list was{ss(val)}")

    def test_3_programmers_exists(self):
        reload_module(self.module)
        from src.order_book import OrderBook,  Task
        code = """
t = OrderBook()
t.programmers()
"""
        t = OrderBook()
        try:
            val = t.programmers()
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method programmers(self) defined?')
        
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == type([]), f"When executing the following code {code}type of return value should be list, now it is of type {taip}")
        expected = 0
        self.assertTrue(len(val)==expected, f"When executing the following code{code}\nmethod should return a list, which length is {expected}, length of list was {len(val)}")

    def test_3_programmers_works(self):
        from src.order_book import OrderBook,  Task

        code = """
t = OrderBook()
t.add_order("program web store", "Andy", 10)
t.add_order("program mobile game", "Eric", 5)
t.programmers()
"""   
        t = OrderBook()
        t.add_order("program web store", "Andy", 10)
        t.add_order("program mobile game", "Eric", 5)
        try:
            val = t.programmers()
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method programmers(self) defined?')
        
        expected = 2
        self.assertTrue(len(val)==expected, f"When executing the following code{code}\nmethod should return a list, which length is {expected}, length of list was {len(val)}")

        taip = str(type(val[0])).replace("<class '","").replace("'>","")
        self.assertTrue(type(val[0]) == type(""), f"When executing the following code {code}type of first item in list returned should be Task, now it is of type {taip}")
    
        expected = ["Andy", "Eric"]
        self.assertTrue(sorted(val)==expected, f"When executing the following code{code}\nmethod should return a list, which content is {expected} now return was {val}")   

        code = """
t = OrderBook()
t.add_order("program web store", "Andy", 10)
t.add_order("program mobile game", "Eric", 5)
t.add_order("code hello world", "Andy", 1)
t.programmers()
"""   

        t.add_order("code hello world", "Andy", 1)
        try:
            val = t.programmers()
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method programmers(self) defined?')
        
        expected = 2
        self.assertTrue(len(val)==expected, f"When executing the following code{code}\nmethod should return a list, which length is {expected}, length of list was {len(val)}. The returned list was\n{s(val)}")

        expected = ["Andy", "Eric"]
        self.assertTrue(sorted(val)==expected, f"When executing the following code{code}\nmethod should return a list, which content is {expected} now return was {val}")   

if __name__ == '__main__':
    unittest.main()
