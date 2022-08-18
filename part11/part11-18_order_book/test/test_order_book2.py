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

@points('11.order_book_part3')
class OrderBookPart3Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'en')

    def test_1_mark_finished(self):
        reload_module(self.module)
        from src.order_book import OrderBook, Task
        code = """
t = OrderBook()
t.add_order("program web store", "Andy", 10)
t.mark_finished(1)
"""
        t = OrderBook()
        t.add_order("program web store", "Andy", 10)

        til = t.all_orders()
        id = til[0].id
        code += f"\n"
        
        try:
            t.mark_finished(id)
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method mark_finished(self, id: int) defined?')
        
        code = """
t = OrderBook()
t.add_order("program web store", "Andy", 10)
t.mark_finished(1)
t.all_orders()
"""

        val = t.all_orders()

        t1 = ("program web store", "Andy", 10, True) 
        all_ok = ook(val, [t1])

        expected = s([tt(t1)])

        self.assertTrue(all_ok, f"When executing the following code {code}\nmethod should return a list containing following tasks\n{expected}\nnow return was\n{ss(val)}")

        code = """
t = OrderBook()
t.add_order("program web store", "Andy", 10)
t.add_order("program mobile gane", "Eric", 5)
t.mark_finished(1)
t.mark_finished(2)
t.all_orders()
"""

        t.add_order("program mobile gane", "Eric", 5)
        til = t.all_orders()
        id1 = til[0].id
        id2 = til[1].id

        try:
            t.mark_finished(id1)
            t.mark_finished(id2)
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method mark_finished(self, id: int) defined?')
        
        val = t.all_orders()

        t2 = ("program mobile gane", "Eric", 5, True)
        all_ok = ook(val, [t1, t2])

        expected = s([tt(t1), tt(t2)])

        self.assertTrue(all_ok, f"When executing the following code {code}\nmethod should return a list containing following tasks\n{expected}\nnow return was\n{ss(val)}")

    def test_2_mark_finished_exception(self):
        reload_module(self.module)
        from src.order_book import OrderBook, Task
        code = """
t = OrderBook()
t.add_order("program web store", "Andy", 10)
t.mark_finished(999)
"""
        t = OrderBook()
        t.add_order("program web store", "Andy", 10)

        til = t.all_orders()
        id = til[0].id + 1
        code += f"\n"
        
        ok = False
        try:
            t.mark_finished(id)
        except ValueError:
            ok = True
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method mark_finished(self, id: int) defined?')
        self.assertTrue(ok, f'Executing the following code {code}should raise ValueError exception')

    def test_3_unfinished(self):
        from src.order_book import OrderBook, Task

        code = """
t = OrderBook()
t.unfinished_orders()
"""
        t = OrderBook()
        try:
            t.unfinished_orders()
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method unfinished_orders(self) defined?')

        code = """
t = OrderBook()
t.add_order("program web store", "Andy", 10)
t.unfinished_orders()
"""
        t = OrderBook()
        t.add_order("program web store", "Andy", 10)
        try:
            val = t.unfinished_orders()
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method unfinished_orders(self) defined?')

        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == type([]), f"When executing the following code{code}type of return value should be list, now it is of type {taip}")
        expected = 1
        self.assertTrue(len(val)==expected, f"When executing the following code{code}\nmethod should return a list, which length is {expected}, length of list was {len(val)}")
        
        ttt = Task("code hello world", "Eric", 3)
        taip = str(type(val[0])).replace("<class '","").replace("'>","")
        self.assertTrue(type(val[0]) == type(ttt), f"When executing the following code {code}type of first item in list returned should be Task, now it is of type {taip}")

        expected = 1
        self.assertTrue(len(val)==expected, f"When executing the following code{code}\nmethod should return a list, which length is {expected}, length of list was {len(val)}")

        t1 = ("program web store", "Andy", 10, False) 
        all_ok = ook(val, [t1])

        expected = s([tt(t1)])

        self.assertTrue(all_ok, f"When executing the following code {code}\nmethod should return a list containing following tasks\n{expected}\nnow return was\n{ss(val)}")

        code = """
t = OrderBook()
t.add_order("program web store", "Andy", 10)
t.add_order("program mobile gane", "Eric", 5)
t.add_order("code better facebook", "Jonas", 5000)
t.unfinished_orders()
"""

        t.add_order("program mobile gane", "Eric", 5)
        t.add_order("code better facebook", "Jonas", 5000)
        t2 = ("program mobile gane", "Eric", 5, False)
        t3 = ("code better facebook", "Jonas", 5000, False)
        try:
            val = t.unfinished_orders()
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method unfinished_orders(self) defined?')

        expected = 3
        self.assertTrue(len(val)==expected, f"When executing the following code{code}\nmethod should return a list, which length is {expected}, length of list was {len(val)}")

        all_ok = ook(val, [t1, t2, t3])

        expected = s([tt(t1), tt(t2),  tt(t3)])

        self.assertTrue(all_ok, f"When executing the following code {code}\nmethod should return a list containing following tasks\n{expected}\nnow return was\n{ss(val)}")

        code = """
t = OrderBook()
t.add_order("program web store", "Andy", 10)
t.add_order("program mobile gane", "Eric", 5)
t.add_order("code better facebook", "Jonas", 5000)
t.mark_finished(1)
t.mark_finished(2)
t.unfinished_orders()
"""

        til = t.all_orders()
        id1 = til[0].id
        id2 = til[1].id

        try:
            t.mark_finished(id1)
            t.mark_finished(id2)
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method mark_finished(self, id: int) defined?')
       
        try:
            val = t.unfinished_orders()
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method unfinished_orders(self) defined?')

        expected = 1
        self.assertTrue(len(val)==expected, f"When executing the following code{code}\nmethod should return a list, which length is {expected}, length of list was {len(val)}")

        all_ok = ook(val, [t3])

        expected = s([tt(t3)])

        self.assertTrue(all_ok, f"When executing the following code {code}\nmethod should return a list containing following tasks\n{expected}\nnow return was\n{ss(val)}")


    def test_4_finished(self):
        reload_module(self.module)
        from src.order_book import OrderBook, Task

        code = """
t = OrderBook()
t.finished_orders()
"""
        t = OrderBook()
        try:
            t.finished_orders()
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method finished_orders(self) defined?')

        code = """
t = OrderBook()
t.add_order("program web store", "Andy", 10)
t.mark_finished(1)
t.finished_orders()
"""
        t = OrderBook()
        t.add_order("program web store", "Andy", 10)

        til = t.all_orders()
        id1 = til[0].id

        try:
            t.mark_finished(id1)
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method mark_finished(self, id: int) defined?')
       
        try:
            val = t.finished_orders()
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method unfinished_orders(self) defined?')

        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == type([]), f"When executing the following code{code}type of return value should be list, now it is of type {taip}")
        expected = 1
        self.assertTrue(len(val)==expected, f"When executing the following code{code}\nmethod should return a list, which length is {expected}, length of list was {len(val)}")
        
        ttt = Task("code hello world", "Eric", 3)
        taip = str(type(val[0])).replace("<class '","").replace("'>","")
        self.assertTrue(type(val[0]) == type(ttt), f"When executing the following code {code}type of first item in list returned should be Task, now it is of type {taip}")

        expected = 1
        self.assertTrue(len(val)==expected, f"When executing the following code{code}\nmethod should return a list, which length is {expected}, length of list was {len(val)}")

        t1 = ("program web store", "Andy", 10, True) 
        all_ok = ook(val, [t1])

        expected = s([tt(t1)])

        self.assertTrue(all_ok, f"When executing the following code {code}\nmethod should return a list containing following tasks\n{expected}\nnow return was\n{ss(val)}")

        code = """
t = OrderBook()
t.add_order("program web store", "Andy", 10)
t.add_order("program mobile gane", "Eric", 5)
t.add_order("code better facebook", "Jonas", 5000)
t.mark_finished(1)
t.mark_finished(2)
t.finished_orders()
"""
        t = OrderBook()
        t.add_order("program web store", "Andy", 10)
        t.add_order("program mobile gane", "Eric", 5)
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
            val = t.finished_orders()
        except Exception as e:
            self.fail(f'Executing the following code {code}threw an error\n{e}\nIs method unfinished_orders(self) defined?')

        expected = 2
        self.assertTrue(len(val)==expected, f"When executing the following code{code}\nmethod should return a list, which length is {expected}, length of list was {len(val)}")
        
        t1 = ("program web store", "Andy", 10, True) 
        t2 = ("program mobile gane", "Eric", 5, True) 

        all_ok = ook(val, [t1, t2])

        expected = s([tt(t1), tt(t1)])

        self.assertTrue(all_ok, f"When executing the following code {code}\nmethod should return a list containing following tasks\n{expected}\nnow return was\n{ss(val)}")

if __name__ == '__main__':
    unittest.main()