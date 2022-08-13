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

exercise = 'src.pet'
function = "new_pet"

def f(attr: list):
    return ",".join(attr)


@points('8.pet')
class PetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_ok(self):
        ok, line = check_source(self.module)
        message = """All code testing the functions must be inside the
if __name__ == "__main__":
block. The following line must be moved:
"""
        self.assertTrue(ok, message+line)

    def test_0b_constructor(self):
        try:
            from src.pet import Pet
            fluffy = Pet("Fluffy","Dog",2014)
        except Exception as e:
            self.fail(f'Calling constructor Pet("Fluffy","Dog",2014) threw an error \n{e}')


    def test1_function_exists(self):
        try:
            from src.pet import new_pet
        except:
            self.fail("Your program should contain a function " + 
                " new_pet(name: str, species: str, year_of_birth: int)")

    def test2_return_type(self):
        try:
            from src.pet import new_pet
            val = new_pet("Fluffy","Dog",2014)
        except Exception as e:
            self.fail('Function threw an error when called like this: new_pet("Fluffy","Dog",2014)')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue("Pet" in str(type(val)), f"Function new_pet should return a value of type Pet," +  
            f' now it returns {val} which is of type {taip}\nwhen it is called as new_pet("Fluffy","Dog",2014)')
        


    def test3_test_attributes(self):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
            reload_module(self.module)
            new_pet = load(exercise, function, 'en')

            attributes = ("name", "species", "year_of_birth")

            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(new_pet("Fluffy","Dog",2014))

                self.assertTrue(ref.has_attribute(attr), f"The Pet object should have an attribute {attr}," +  
                    f'\nnow the attributes are\n{f(ref.list_attributes(True))}\nwhen function was called as new_pet("Fluffy","Dog",2014)')
    
    def test4_test_attribute_types(self):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
            reload_module(self.module)
            new_pet = load(exercise, function, 'en')

            attributes = (("name", str), ("species", str), ("year_of_birth", int))

            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(new_pet("Fluffy","Dog",2014))
                name,taip = attr

                taip2 = str(type(ref.get_attribute(name))).replace("<class '","").replace("'>","")

                self.assertTrue(type(ref.get_attribute(name)) == taip, f"The type of the attribute {name} should be {taip}, now it is {taip2}")

    def test5_test_attribute_values(self):
         test_cases = [("Fluffy","dog",1970), ("Garfield","cat",1986), ("Chip","chipmonk",1999),("Dumbo","elephant",1963)]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
                reload_module(self.module)
                new_pet = load(exercise, function, 'en')

                val = new_pet(test_case[0], test_case[1], test_case[2])
                
                attributes = ("name", "species", "year_of_birth")
                ref = reflect.Reflect()
                ref.set_object(val)

                for i in range(len(attributes)):
                    value = ref.get_attribute(attributes[i])
                    self.assertEqual(value, test_case[i], 
                        f'The value of attribute {attributes[i]} should be {test_case[i]}, now it is {value},\nwhen the arguments were {test_case}')
if __name__ == '__main__':
    unittest.main()
