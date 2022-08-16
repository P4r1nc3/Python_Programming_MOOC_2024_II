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

exercise = 'src.shortest_in_room'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 


class ShortestInRoomTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected.")]):
           cls.module = load_module(exercise, 'en')

    @points('9.shortest_in_room_part1')
    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    @points('9.shortest_in_room_part1')
    def test_1_classes_exists(self):
        try:
            from src.shortest_in_room import Person
            r = Person("Ken",150)
        except Exception as e:
            self.fail(f'Calling constructor Person("Ken",150) threw an error \n{e}\n' +
                'Have you changed the implementation of Person class?')

        try:
            from src.shortest_in_room import Room
            r = Room()
        except Exception as e:
            self.fail(f'Calling constructor Room() threw an error \n{e}\n' +
                'Make sure, that class exists.')

    @points('9.shortest_in_room_part1')
    def test_2_room_methods_exists1(self):
        from src.shortest_in_room import Room, Person
        room = Room()
        try:
            room.add(Person("Ken", 150))
        except Exception as e:
            self.fail(f'Method call add(Person("Ken", 150)) threw an error\n{e}')

        try:
            val = room.is_empty()
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == bool, f'Method is_empty() should return a value, ' + 
                f'which is of type bool, now it returns a value {val}, which is of type {taip}.')
        except Exception as e:
            self.fail(f'Method call is_empty threw an error\n{e}')

        try:
            room.print_contents()
        except Exception as e:
            self.fail(f'Method call print_contents threw an error\n{e}\nwhen the room is empty')


    @points('9.shortest_in_room_part1')
    def test_3_add_person_print_contents(self):
        from src.shortest_in_room import Room, Person
        room = Room()
        self.assertTrue(room.is_empty(), f'Method is_empty() should return True, when not a single person has been added in the room ' + 
            'Now it returned False.')

        test_cases = [("Grace", 180), ("Jan", 175), ("Lisa", 150), ("Paul", 204), ("Jana", 171), ("Ruth", 149)]
        persons = ""
        tested = []
        for test_case in test_cases:
            tested.append(test_case)
            room.add(Person(test_case[0], test_case[1]))
            persons += f"\n{test_case[0]} ({test_case[1]} cm)"

            self.assertFalse(room.is_empty(), f'"Method is_empty() should return False, when there have been added persons in the room ' +
                f'- now it returned True.' + 
                f'\nwhen the following persons has been added in the room:\n{persons}\n')

            room.print_contents()
            output = get_stdout()

            for t in tested:
                self.assertTrue(t[0] in output and str(t[1]) in output, f'The following strings should be found out from the printout\n' +
                    f'{t[0]} and {t[1]}\nwhen the following persons has been added in the room:\n{persons}\n' + 
                    f'now the print out is\n{output}')
            


    @points('9.shortest_in_room_part2')
    def test_4_method_shortest_exists(self):
        from src.shortest_in_room import Room, Person
        room = Room()
        try:
            val = room.shortest()
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(val is None, f'Method shortest should return a value None, ' + 
                f'when the room is empty, now it returns a value {val}, which is of type {taip}.')
        except Exception as e:
            self.fail('Method call shortest threw an error\n{e}\n' + 
                'when the room is empty.')
        
        try:
            room.add(Person("Ann",120))
            room.add(Person("Tim",150))
            val = room.shortest()
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue("Person" in str(type(val)), f'Method shortest should return a value, ' + 
                f'which is of type Person, now it returns a value {val}, which is of type {taip}.' + 
                f'when the following persons has been added in the room:\n' +
                'Person("Ann",120)\n' +
                'Person("Tim",150)')
        except Exception as e:
            self.fail(f'Method call shortest threw an error\n{e}\n'+ 
                f'when the following persons has been added in the room:\n' +
                'Person("Ann",120)\n' +
                'Person("Tim",150)')

    @points('9.shortest_in_room_part2')
    def test_5_test_shortest(self):
        from src.shortest_in_room import Room, Person
        room = Room()
        test_cases = [("Grace", 180), ("Jan", 175), ("Lisa", 150), ("Paul", 204), ("Jana", 171), ("Ruth", 149)]

        persons = ""
        tested = []
        for test_case in test_cases:
            tested.append(test_case)
            room.add(Person(test_case[0], test_case[1]))
            persons += f"\n{test_case[0]} ({test_case[1]} cm)"

            shortest = room.shortest()
            taip = str(type(shortest)).replace("<class '","").replace("'>","")
            self.assertTrue("Person" in str(type(shortest)), f'Method shortest should return a value, ' + 
                f'which is of type Person, now it returns a value {shortest}, which is of type {taip}.' + 
                f'when the following persons has been added in the room:\n{persons}')

            try:
                val = shortest.name
            except:
                self.fail(f'Method shortest() should return Person object\nNow it returns ' + 
                f'returns {shortest}, which is of type {type(shortest)} when the following persons has been added:{persons}.')                

            corr = min(tested, key = lambda x : x[1])[0]

            self.assertEqual(val, corr, f'Method shortest() should return a person, whose name is {corr}. \nNow it ' + 
                f'returns a person, whose name is {val}, when the following persons has been added:{persons}.')

    @points('9.shortest_in_room_part3')
    def test_6_method_remove_shortest_exists(self):
        from src.shortest_in_room import Room, Person
        room = Room()
        try:
            val = room.remove_shortest()
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(val is None, f'Method remove_shortest should return a value None, ' + 
                f'when the room is empty, now it returns a value {val}, which is of type {taip}.')
        except Exception as e:
            self.fail('Method call remove_shortest threw an error\n{e}' + 
                'when the room is empty.')
        
        try:
            room.add(Person("Ann",120))
            room.add(Person("Tim",150))
            val = room.remove_shortest()
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue("Person" in str(type(val)), f'Method remove_shortest should return a value, ' + 
                f'which is of type Person, now it returns a value {val}, which is of type {taip}.' + 
                f'when the following persons has been added in the room:\n' +
                'Person("Ann",120)\n' +
                'Person("Tim",150)')
        except Exception as e:
            self.fail('Method call remove_shortest threw an error\n{e}\n'+ 
                f'when the following persons has been added in the room:\n' +
                'Person("Ann",120)\n' +
                'Person("Tim",150)')

    @points('9.shortest_in_room_part3')
    def test_7_test_remove_shortest(self):
        from src.shortest_in_room import Room, Person
        room = Room()
        test_cases = [("Grace", 180), ("Jan", 175), ("Lisa", 150), ("Paul", 204), ("Jana", 171), ("Ruth", 149)]

        tested = []
        persons = ""
        for test_case in test_cases:
            room.add(Person(test_case[0], test_case[1]))
            persons += f"\n{test_case[0]} ({test_case[1]} cm)"
            tested.append(test_case)
        
        prev_output = ""
        for i in range(len(test_cases)):
            val = room.remove_shortest()
            corr = min(tested, key = lambda x : x[1])
            
            self.assertEqual(val.name, corr[0], f'Method remove_shortest() should return a person, whose name is {corr[0]}. \nNow it' + 
                f'returns a person, whose name is {val.name}, when the following persons were in the room {tested}.')
            
            tested.remove(corr)

            room.print_contents()
            output = get_stdout().replace(prev_output, "")
            prev_output += output
            output_list = [x for x in output.split("\n") if len(x.strip()) > 0 and not x.startswith("There are")]

            self.assertEqual(len(output_list), len(tested), f'In the room should be now {len(tested)} persons, when the following persons were added to the room:' +
                f'{persons}\nand method remove_shortest have been called {i + 1} times.\nNow, however the method print_contents prints out\n{output}')
            
if __name__ == '__main__':
    unittest.main()
