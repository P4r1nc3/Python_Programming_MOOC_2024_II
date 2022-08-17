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

exercise = 'src.game_museum'

def f(attr: list):
    return "\n".join([str(x) for x in attr]) 

@points('10.game_museum')
class GameMuseumTest(unittest.TestCase):
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

    def test_1_classes_exist(self):
        try:
            from src.game_museum import ComputerGame
            a = ComputerGame("Pacman", "Namco", 1980)
        except Exception as e:
            self.fail(f'Calling constructor ComputerGame("Pacman", "Namco", 1980) threw an error \n{e}\n' + 
            'Check that you have not changed the class ComputerGame!')

        try:
            from src.game_museum import GameWarehouse
            a = GameWarehouse()
        except Exception as e:
            self.fail(f'Calling constructor GameWarehouse() threw an error \n{e}\n' + 
            'Check that you have not changed the class GameWarehouse!')

        try:
            from src.game_museum import GameMuseum
            a = GameMuseum()
        except Exception as e:
            self.fail(f'Calling constructor GameMuseum() threw an error \n{e}\n' + 
            'Check that the class is defined!')

    def test_2_inheritance(self):
        from src.game_museum import ComputerGame, GameWarehouse, GameMuseum
        a = GameMuseum()
        self.assertTrue(isinstance(a, GameWarehouse), f"Class GameMuseum should" +
            'inherit the class GameWarehouse!')

    def test_3_method_redefined(self):
        from src.game_museum import ComputerGame, GameWarehouse, GameMuseum
        self.assertTrue(GameMuseum.list_games is not GameWarehouse.list_games, 
            f'Method list_games needs to be redefined in the class GameWarehouse!')

    def test_4_method_works_1(self):
        test_cases = [("Commando","Capcom",1985), ("Super Mario Bros","Nintendo",1985), ("IK+", "System 3", 1987), 
            ("Elite", "Firebird", 1985), ("Star Fox", "Nintendo", 1993)]
        shuffle(test_cases)
        from src.game_museum import ComputerGame, GameWarehouse, GameMuseum
        museum = GameMuseum()
        for test_case in test_cases:
            museum.add_game(ComputerGame(test_case[0], test_case[1], test_case[2]))
        
        corr = sorted([x[0] for x in test_cases if x[2] < 1990])
        val = sorted([p.name for p in museum.list_games()])

        test_cases_str = ", ".join([f'ComputerGame("{t[0]}","{t[1]}",{t[2]})' for t in test_cases]) 

        self.assertEqual(corr, val, f'Method list_games() should return the following games:\n' + 
            f'{f(corr)}\nbut now it returns these games:\n{f(val)}\nwhen the method was called with ' + 
            f'this list:\n{test_cases_str}')

    def test_5_metodi_toimii_2(self):
        test_cases = [("IK+", "System 3", 1987), ("Pool of Radiance", "SSI", 1988), ("Great Giana Sisters", "Rainbow Arts", 1987), 
            ("Doom", "ID Software", 1993), ("Sim City 2000", "Maxis", 1993), ("Final Fantasy VII", "Square", 1997)]
        shuffle(test_cases)
        from src.game_museum import ComputerGame, GameWarehouse, GameMuseum
        museum = GameMuseum()
        for test_case in test_cases:
            museum.add_game(ComputerGame(test_case[0], test_case[1], test_case[2]))
        
        corr = sorted([x[0] for x in test_cases if x[2] < 1990])
        val = sorted([p.name for p in museum.list_games()])

        test_cases_str = ", ".join([f'ComputerGame("{t[0]}","{t[1]}",{t[2]})' for t in test_cases]) 

        self.assertEqual(corr, val, f'Method list_games() should return the following games:\n' + 
            f'{f(corr)}\nbut now it returns these games:\n{f(val)}\nwhen the method was called with ' + 
            f'this list:\n{test_cases_str}')
    


        

    
if __name__ == '__main__':
    unittest.main()
