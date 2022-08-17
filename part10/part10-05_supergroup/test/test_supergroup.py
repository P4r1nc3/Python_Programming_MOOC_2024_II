import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint, shuffle
from datetime import date

exercise = 'src.supergroup'

def f(attr: list):
    return "\n".join([str(x) for x in attr]) 

@points('10.supergroup')
class SupergroupTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
           cls.module = load_module(exercise, 'en')

    
    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_1_luokka_superhero_exists(self):
        try:
            from src.supergroup import SuperHero
            a = SuperHero("Bulk","super strength")
        except Exception as e:
            self.fail(f'Calling constructor SuperHero("Bulk","super strength") threw an error \n{e}\n' + 
            'Check that class SuperHero is defined!')

    def test_2_class_supergroup_exists(self):
        try:
            from src.supergroup import SuperHero, SuperGroup
            a = SuperGroup("Group", "Helsinki")
        except Exception as e:
            self.fail(f'Calling constructor SuperGroup("Group", "Helsinki") threw an error \n{e}\n' + 
            'Check that the class exists and that an object can be created from the class.')

    def test_3_attributes_protected(self):
        from src.supergroup import SuperHero, SuperGroup
        ref = reflect.Reflect()
        group = SuperGroup("Group", "Helsinki")
        ref.set_object(group)
        group_attr = ref.list_attributes(True)

        attr_list = ("_name", "_location", "_members")
        for attr in attr_list:
            self.assertTrue(attr in group_attr, f'Class SuperGroup should have ' +
                f'a protected attribute {attr}.\nCheck that attribute is ' +
                'defined.')


    def test_4_getters(self):
        from src.supergroup import SuperHero, SuperGroup
        ref = reflect.Reflect()
        group = SuperGroup("Group", "Helsinki")
        ref.set_object(group)
        group_attr = ref.list_attributes(True)

        attr_list = ("name", "location")
        for attr in attr_list:
            self.assertTrue(attr in group_attr, f'Class SuperGroup should have ' +
                f'a getter (i.e. a property) {attr}!\nCheck that is is ' +
                'defined.')

    def test_5_add_print_1(self):
        from src.supergroup import SuperHero, SuperGroup
        test_cases = [("Bulk","Superstrength"), ("Flush", "Super flushing"), 
            ("Spam Man", "Spam mailing")]
        group = SuperGroup("Rough Riders", "Alabama")
        corr = "Rough Riders, Alabama\nMembers:"
        test_str = ""
        for test_case in test_cases:
            group.add_member(SuperHero(test_case[0], test_case[1]))
            corr += "\n" + test_case[0] + ", superpowers: " + test_case[1]
            test_str += f'SuperHero("{test_case[0]}", "{test_case[1]}")'

        group.print_group()
        output = "\n".join([x.strip() for x in get_stdout().split("\n") if len(x.strip()) > 0])

        self.assertEqual(output, corr, f'Method print_group() shoud output\n' + 
            f'{corr}\n. Instead, it outputs\n{output}\nwhen these members were added:\n' +
            test_str)

    def test_6_add_print2(self):
        from src.supergroup import SuperHero, SuperGroup
        test_cases = [("Super-Super","Metahero"), ("Green Bantern", "Bantering"), 
            ("Super Jam", "Makes excellent jam")]
        group = SuperGroup("Supery Supes", "Oslo")
        corr = "Supery Supes, Oslo\nMembers:"
        test_str = ""
        for test_case in test_cases:
            group.add_member(SuperHero(test_case[0], test_case[1]))
            corr += "\n" + test_case[0] + ", superpowers: " + test_case[1]
            test_str += f'SuperHero("{test_case[0]}", "{test_case[1]}")'

        group.print_group()
        output = "\n".join([x.strip() for x in get_stdout().split("\n") if len(x.strip()) > 0])

        self.assertEqual(output, corr, f'Method print_group() shoud output\n' + 
            f'{corr}\n. Instead, it outputs\n{output}\nwhen these members were added:\n' +
            test_str)



    
if __name__ == '__main__':
    unittest.main()
