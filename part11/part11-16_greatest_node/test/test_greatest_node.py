import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re

exercise = 'src.greatest_node'

@points('11.greatest_node')
class GreatestNodeTest(unittest.TestCase):
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
    
    def test_1_function_exists(self):
        try:
            from src.greatest_node import greatest_node
        except Exception as e:
            self.fail(f'Your program should contain function greatest_node.')

    def test_2_type_of_return_value(self):
        try:
            from src.greatest_node import greatest_node, Node
            val = greatest_node(Node(1))
        except Exception as e:
            self.assertTrue(False, f"Function threw an error when it was called follows:" + 
                f'\ngreatest_node(Node(1))\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == int, f"Function greatest_node is expected to return a value, which is of type int," +  
            f" now it returns a value {val} which is of type {taip}\n when it is called as follows\n" +  
            'greatest_node(Node(1))')
        

    def test_3_is_recursive(self):
        from src.greatest_node import greatest_node, Node
        self.assertTrue(reflect.test_recursion(greatest_node, Node(1, Node(2))), 
            f'"Function greatest_node should call itself recursively.\n' + 
            f'Now calling greatest_node, Node(1, Node(2))) does not lead to new calls of function greatest_node.')

    def test_4_test_with_values_1(self):
        from src.greatest_node import greatest_node, Node
        root = Node(3)
        left = Node(5,Node(7),Node(10,Node(3),Node(13)))
        right = Node(6,None, Node(11))
        test_case = "3, 5, 7, 10, 3, 13, 6, ja 11"
        root.left_child = left
        root.right_child = right

        val = greatest_node(root)
        corr = 13

        self.assertEqual(val, corr, f'Function should return a value\n{corr}\n' + 
            f'when tree contains values\n{test_case}\nnow function returns\n' + 
            f'{val}')

    def test_4_test_with_values_2(self):
        from src.greatest_node import greatest_node, Node
        root = Node(13)
        left = Node(15,Node(17, Node(24)),Node(24,Node(14),Node(9)))
        right = Node(8,Node(29))
        test_case = "13, 15, 17, 24, 14, 9, 8 ja 29"
        root.left_child = left
        root.right_child = right

        val = greatest_node(root)
        corr = 29

        self.assertEqual(val, corr, f'Function should return a value\n{corr}\n' + 
            f'when tree contains values\n{test_case}\nnow function returns\n' + 
            f'{val}')
        
if __name__ == '__main__':
    unittest.main()
