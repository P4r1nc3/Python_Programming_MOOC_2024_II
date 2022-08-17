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

exercise = 'src.secret_magic_potion'

def f(attr: list):
    return "\n".join([str(x) for x in attr]) 

@points('10.secret_magic_potion')
class MagicPotionTest(unittest.TestCase):
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

    def test_1_class_magic_potion_exists(self):
        try:
            from src.secret_magic_potion import MagicPotion
            a = MagicPotion("Soda")
        except Exception as e:
            self.fail(f'Calling constructor MagicPotion("Soda") threw an error \n{e}\n' + 
            'Check that you have not changed the class definition!')

    def test_2_class_secret_magic_potion_exists(self):
        try:
            from src.secret_magic_potion import SecretMagicPotion
            a = SecretMagicPotion("Super soda", "abc")
        except Exception as e:
            self.fail(f'Calling constructor SecretMagicPotion("Super soda", "abc") threw an error \n{e}\n' + 
            'Check that the class exists and that an object can be created.')

    def test_3_inheritance(self):
        from src.secret_magic_potion import MagicPotion, SecretMagicPotion
        self.assertTrue(issubclass(SecretMagicPotion, MagicPotion), 
            f"Class SecretMagicPotion should " +
            'inherit the class MagicPotion!')

    def test_4_redefine(self):
        from src.secret_magic_potion import MagicPotion, SecretMagicPotion
        self.assertTrue(MagicPotion.add_ingredient is not SecretMagicPotion.add_ingredient, 
            "Method add_ingredient must be redefined in class SecretMagicPotion!")
        self.assertTrue(MagicPotion.print_recipe is not SecretMagicPotion.print_recipe, 
            "Method print_recipe must be redefined in class SecretMagicPotion!")


    def test_5_add_print_works_1(self):
        from src.secret_magic_potion import SecretMagicPotion
        test_cases = [("Eucalyptus",4),("Mints",24),("Magic dust",4.5)]
        name = "Breathus refreshus"
        pword = "pocushocus"
        potion = SecretMagicPotion(name, pword)
        corr = name + ":"
        test_str = ""
        for test_case in test_cases:
            potion.add_ingredient(test_case[0], test_case[1], pword)
            corr += f"\n{test_case[0]} {test_case[1]} grams"

        potion.print_recipe(pword)
        output = "\n".join([x.strip() for x in get_stdout().split("\n") if len(x.strip()) > 0])
        test_str = "\n".join([str(x) for x in test_cases])

        self.assertEqual(output, corr, f'Method print_recipe() should output\n' + 
            f'{corr}\nNow it outpus\n{output}\nwhen following ingredients were added:\n' +
            test_str)


    def test_6_add_print_works_2(self):
        from src.secret_magic_potion import SecretMagicPotion
        test_cases = [("Coriander",6),("Ink",14),("Mushroom",3.5)]
        name = "Nausius maximus"
        pword = "abraka-abraka"
        potion = SecretMagicPotion(name, pword)
        corr = name + ":"
        test_str = ""
        for test_case in test_cases:
            potion.add_ingredient(test_case[0], test_case[1], pword)
            corr += f"\n{test_case[0]} {test_case[1]} grams"

        potion.print_recipe(pword)
        output = "\n".join([x.strip() for x in get_stdout().split("\n") if len(x.strip()) > 0])
        test_str = "\n".join([str(x) for x in test_cases])

        self.assertEqual(output, corr, f'Method print_recipe() should output\n' + 
            f'{corr}\nNow it outpus\n{output}\nwhen following ingredients were added:\n' +
            test_str)

    def test_7_add_wrong_password(self):
        from src.secret_magic_potion import SecretMagicPotion
        name = "Testius Maximus"
        pword = "testi123"
        potion = SecretMagicPotion(name, pword)
        try:
            potion.add_ingredient("Fly agaric", 1.0, "test321")
            self.fail(f"Method add_ingredient() should throw a ValueError " +
                f'when class was initialized as:\n' +
                f'potion = SecretMagicPotion("{name}", "{pword}")\n' +
                f'and method was called as:\n' + 
                'potion.add_ingredient("Fly agaric", 1.0, "test321")')
        except ValueError:
            pass

    def test_8_print_wrong_password(self):
        from src.secret_magic_potion import SecretMagicPotion
        name = "Testius Maksimus"
        pword = "pocus hocus"
        potion = SecretMagicPotion(name, pword)
        potion.add_ingredient("Fly agaric", 1.0, "pocus hocus")
        try:
            potion.print_recipe("hocus pocus")
            self.fail(f"Method print_recipe() should throw a ValueError " +
                f'when class was initialized as:\n' +
                f'potion = SecretMagicPotion("{name}", "{pword}")\n' +
                f'and one ingredient was added:\n' + 
                'potion.add_ingredient("Fly agaric", 1.0, "pocus hocus")\n' +
                'Method was called as\n'
                'potion.print_recipe("hocus pocus")')
        except ValueError:
            pass


    
    
if __name__ == '__main__':
    unittest.main()
