import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re
from random import choice, randint, shuffle

exercise = 'src.ballplayers'

def source_rows(function: callable):
    src = inspect.getsource(function)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)


class BallPlayersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_ok(self):
        ok, line = check_source(self.module)
        message = """Code testing the functions must be located after the
if __name__ == "__main__":
block. The following line must be moved:
"""
        self.assertTrue(ok, message+line)
    
    @points('12.ballplayers_part1')
    def test1_class_exists(self):
        try:
            from src.ballplayers import BallPlayer 
        except Exception as e:
            self.fail('Program should contain a class BallPlayer - check that you have not changed it')
    
    @points('12.ballplayers_part1')
    def test_2a_function_exists(self):
        try:
            from src.ballplayers import most_goals
        except Exception as e:
            self.fail(f'Your program should have a function called most_goals.')

    @points('12.ballplayers_part1')
    def test_2b_return_type(self):
        try:
            from src.ballplayers import most_goals, BallPlayer
            val = most_goals([BallPlayer("a",2,2,2,2), BallPlayer("b",1,1,1,1)])
        except Exception as e:
            self.fail(f"Function threw an error when called like this:\n"  + 
            'most_goals([BallPlayer("a",2,2,2,2), BallPlayer("b",1,1,1,1)])\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == str, f"Function most_goals should return value with type str," +  
            f" now it returns {val} which is of type {taip}\n when it is called with parameter\n" +  
            'most_goals([BallPlayer("a",2,2,2,2), BallPlayer("b",1,1,1,1)])')
        
    @points('12.ballplayers_part1')
    def test_2c_test_with_values1(self):
        from src.ballplayers import most_goals, BallPlayer
    
        tdata = [("Pete",4,12,6,900), ("Arnold",6,14,3,885), ("John",9,19,2,840), ("Kim", 3,11,9,1034)]
        test_case = [BallPlayer(tc[0],tc[1],tc[2],tc[3],tc[4]) for tc in tdata]
        shuffle(test_case)
        test_case_2 = test_case[:]
        corr = max(tdata, key=lambda t:t[2])[0]
        val = most_goals(test_case)

        self.assertEqual(val, corr, f'Function most_goals should return string\n{corr}\n' + 
            f'when it is called with parameter\n{test_case}\nNow the function returns\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Function most_goals cannot change the original list!\n" + 
            f'The list was\n{test_case_2}\nnow it is\n{test_case}.')

    @points('12.ballplayers_part1')
    def test_2d_test_with_values2(self):
        from src.ballplayers import most_goals, BallPlayer
    
        tdata = [("Pete",4,1,6,900), ("Arnold",6,4,3,885), ("John",9,9,2,840), ("Kim", 3,13,9,1034)]
        test_case = [BallPlayer(tc[0],tc[1],tc[2],tc[3],tc[4]) for tc in tdata]
        shuffle(test_case)
        test_case_2 = test_case[:]
        corr = max(tdata, key=lambda t:t[2])[0]
        val = most_goals(test_case)

        self.assertEqual(val, corr, f'Function most_goals should return string\n{corr}\n' + 
            f'when it is called with parameter\n{test_case}\nNow the function returns\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Function most_goals cannot change the original list!\n" + 
            f'The list was\n{test_case_2}\nnow it is\n{test_case}.')

    @points('12.ballplayers_part2')
    def test_3a_function_exists(self):
        try:
            from src.ballplayers import most_points
        except Exception as e:
            self.fail(f'Your program should have a function called most_points.')

    @points('12.ballplayers_part2')
    def test_3b_return_type(self):
        try:
            from src.ballplayers import most_points, BallPlayer
            val = most_points([BallPlayer("a",2,2,2,2), BallPlayer("b",1,1,1,1)])
        except Exception as e:
            self.fail(f"Function threw an error when called like this:\n"  + 
            'most_points([BallPlayer("a",2,2,2,2), BallPlayer("b",1,1,1,1)])\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == tuple, f"Function most_points should return value with type tuple," +  
            f" now it returns {val} which is of type {taip}\n when it is called with parameter\n" +  
            'most_points([BallPlayer("a",2,2,2,2), BallPlayer("b",1,1,1,1)])')
        
    @points('12.ballplayers_part2')
    def test_3c_test_with_values1(self):
        from src.ballplayers import most_points, BallPlayer
    
        tdata = [("Pete",4,12,6,900), ("Arnold",6,14,11,885), ("John",9,19,2,840), ("Kim", 3,11,9,1034)]
        test_case = [BallPlayer(tc[0],tc[1],tc[2],tc[3],tc[4]) for tc in tdata]
        shuffle(test_case)
        test_case_2 = test_case[:]
        c = max(tdata, key=lambda t:t[2]+t[3])
        corr = (c[0],c[1])
        val = most_points(test_case)

        self.assertEqual(val, corr, f'Function most_points should return string\n{corr}\n' + 
            f'when it is called with parameter\n{test_case}\nNow the function returns\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Function most_points cannot change the original list!\n" + 
            f'The list was\n{test_case_2}\nnow it is\n{test_case}.')

    @points('12.ballplayers_part2')
    def test_3d_test_with_values2(self):
        from src.ballplayers import most_points, BallPlayer
    
        tdata = [("Pete",4,1,3,900), ("Arnold",6,5,5,885), ("John",9,0,2,840), ("Kim", 3,9,0,1034)]
        test_case = [BallPlayer(tc[0],tc[1],tc[2],tc[3],tc[4]) for tc in tdata]
        shuffle(test_case)
        test_case_2 = test_case[:]
        c = max(tdata, key=lambda t:t[2]+t[3])
        corr = (c[0],c[1])
        val = most_points(test_case)

        self.assertEqual(val, corr, f'Function most_points should return string\n{corr}\n' + 
            f'when it is called with parameter\n{test_case}\nNow the function returns\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Function most_points cannot change the original list!\n" + 
            f'The list was\n{test_case_2}\nnow it is\n{test_case}.')

    @points('12.ballplayers_part3')
    def test_4a_function_exists(self):
        try:
            from src.ballplayers import least_minutes
        except Exception as e:
            self.fail(f'Your program should have a function called least_minutes.')

    @points('12.ballplayers_part3')
    def test_4b_return_type(self):
        try:
            from src.ballplayers import least_minutes, BallPlayer
            val = least_minutes([BallPlayer("a",2,2,2,2), BallPlayer("b",1,1,1,1)])
        except Exception as e:
            self.fail(f"Function threw an error when called like this:\n"  + 
            'least_minutes([BallPlayer("a",2,2,2,2), BallPlayer("b",1,1,1,1)])\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == BallPlayer, f"Function most_points should return value with type BallPlayer," +  
            f" now it returns {val} which is of type {taip}\n when it is called with parameter\n" +  
            'least_minutes([BallPlayer("a",2,2,2,2), BallPlayer("b",1,1,1,1)])')
        
    @points('12.ballplayers_part3')
    def test_4c_test_with_values1(self):
        from src.ballplayers import least_minutes, BallPlayer
    
        tdata = [("Pete",4,12,6,900), ("Arnold",6,14,11,885), ("John",9,19,2,840), ("Kim", 3,11,9,1034)]
        test_case = [BallPlayer(tc[0],tc[1],tc[2],tc[3],tc[4]) for tc in tdata]
        shuffle(test_case)
        test_case_2 = test_case[:]
        corr = min(test_case, key=lambda p:p.minutes)
        val = least_minutes(test_case)

        self.assertEqual(val, corr, f'Function least_minutes should return BallPlayer\n{corr}\n' + 
            f'when it is called with parameter\n{test_case}\nNow the function returns\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Function least_minutes cannot change the original list!\n" + 
            f'The list was\n{test_case_2}\nnow it is\n{test_case}.')

    @points('12.ballplayers_part3')
    def test_4d_test_with_values2(self):
        from src.ballplayers import least_minutes, BallPlayer
    
        tdata = [("Pete",4,12,6,90), ("Arnold",6,14,11,88), ("John",9,19,2,84), ("Kim", 3,11,9,134)]
        test_case = [BallPlayer(tc[0],tc[1],tc[2],tc[3],tc[4]) for tc in tdata]
        shuffle(test_case)
        test_case_2 = test_case[:]
        corr = min(test_case, key=lambda p:p.minutes)
        val = least_minutes(test_case)

        self.assertEqual(val, corr, f'Function least_minutes should return BallPlayer\n{corr}\n' + 
            f'when it is called with parameter\n{test_case}\nNow the function returns\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Function least_minutes cannot change the original list!\n" + 
            f'The list was\n{test_case_2}\nnow it is\n{test_case}.')

 
    
if __name__ == '__main__':
    unittest.main()
