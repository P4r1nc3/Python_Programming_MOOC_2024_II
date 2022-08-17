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

exercise = 'src.word_game'

def f(attr: list):
    return "\n".join([str(x) for x in attr]) 


class WordGameTest(unittest.TestCase):
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

    @points('10.word_game_part1')
    def test_00b_class_word_game_exists(self):
        try:
            from src.word_game import WordGame
            a = WordGame(1)
        except Exception as e:
            self.fail(f'Calling constructor WordGame(1) threw an error \n{e}\n' + 
            'Check that you have not changed the definition!')

    @points('10.word_game_part1')
    def test_01_class_longest_exists(self):
        try:
            from src.word_game import LongestWord
            a = LongestWord(1)
        except Exception as e:
            self.fail(f'Calling constructor LongestWord(0) threw an error \n{e}\n' + 
            'Check that the class is defined!')

    @points('10.word_game_part1')
    def test_02_longest_inheritance(self):
        from src.word_game import WordGame, LongestWord
        self.assertTrue(issubclass(LongestWord,WordGame), f"Class LongestWord should " +
            'inherit class WordGame!')

    @points('10.word_game_part1')
    def test_03_longest_method_redefined(self):
        from src.word_game import WordGame, LongestWord
        self.assertTrue(WordGame.round_winner is not LongestWord.round_winner, 
            f'Method round_winner must be redefined in the class ' + 
            'LongestWord!')

    @points('10.word_game_part1')
    def test_04_longest_play_not_changed(self):
        from src.word_game import WordGame, LongestWord
        self.assertTrue(WordGame.play is LongestWord.play, 
            f'Method play() should not be redefined in class ' + 
            'LongestWord!')

    @points('10.word_game_part1')
    def test_05_longest_works(self):
        test_cases = [("thefirst","two","third","4.",2,0), 
            ("fox","bunny","hound","rabbit","bear","elephant",0,3), 
            ("cat","dog","mickey","donald",0,0),
            ("car","boar","chopper","plane","train","boxcar",1,2)]
        for test_case in test_cases:
            from src.word_game import LongestWord
            with patch('builtins.input', side_effect=list(test_case[:-2])):
                game = LongestWord(len(test_case)//2 - 1)
                game.play()

                output = get_stdout()
                val = [x.strip() for x in output.split("\n") if len(x.strip()) > 0][-2:]
                corr = [f"player 1: {test_case[-2]}", f"player 2: {test_case[-1]}"]

                val_str = "\n".join(val)
                corr_str = "\n".join(corr)
                test_str = "\n".join(test_case[:-2])

                self.assertEqual(val, corr, f'The game should output\n{corr_str}\n' + 
                    f'Not it outputs\n{val_str}\nwhen input was \n{test_str}')   

    @points('10.word_game_part2')
    def test_06_class_vowels_exists(self):
        try:
            from src.word_game import MostVowels
            a = MostVowels(1)
        except Exception as e:
            self.fail(f'Calling constructor MostVowels(0) threw an error \n{e}\n' + 
            'Check that the class is defined.')

    @points('10.word_game_part2')
    def test_07_vowels_inheritance(self):
        from src.word_game import WordGame, MostVowels
        self.assertTrue(issubclass(MostVowels,WordGame), f"Class MostVowels should " +
            'inherit class WordGame!')

    @points('10.word_game_part2')
    def test_08_vowels_method_redefined(self):
        from src.word_game import WordGame, MostVowels
        self.assertTrue(WordGame.round_winner is not MostVowels.round_winner, 
            f'Method round_winner must be redefined in class' + 
            'MostVowels!')

    @points('10.word_game_part2')
    def test_09_vowels_play_not_changed(self):
        from src.word_game import WordGame, MostVowels
        self.assertTrue(WordGame.play is MostVowels.play, 
            f'Method play() must not be redefined in class ' + 
            'MostVowels!')

    @points('10.word_game_part3')
    def test_11_vowels_workds(self):
        test_cases = [("aaaa!","what","aeiou","que",2,0), 
            ("cat","tiger","lamas","restructure","grrrrrr","help",0,3), 
            ("cat","dog","hello","caller",0,0),
            ("boat","bike","chopper","planetarium","motorcycle","bike",1,1)]
        for test_case in test_cases:
            from src.word_game import MostVowels
            with patch('builtins.input', side_effect=list(test_case[:-2])):
                game = MostVowels(len(test_case)//2 - 1)
                game.play()

                output = get_stdout()
                val = [x.strip() for x in output.split("\n") if len(x.strip()) > 0][-2:]
                corr = [f"player 1: {test_case[-2]}", f"player 2: {test_case[-1]}"]

                val_str = "\n".join(val)
                corr_str = "\n".join(corr)
                test_str = "\n".join(test_case[:-2])

                self.assertEqual(val, corr, f'The game should output\n{corr_str}\n' + 
                    f'Not it outputs\n{val_str}\nwhen input was \n{test_str}')             
    
    @points('10.word_game_part3')
    def test_12_class_rps_exists(self):
        try:
            from src.word_game import RockPaperScissors
            a = RockPaperScissors(1)
        except Exception as e:
            self.fail(f'Calling constructor RockPaperScissors(0) threw an error \n{e}\n' + 
            'Check that the class is defined!')

    @points('10.word_game_part3')
    def test_13_rps_inheritance(self):
        from src.word_game import WordGame, RockPaperScissors
        self.assertTrue(issubclass(RockPaperScissors,WordGame), f"Class RockPaperScissors should " +
            'inherit class WordGame!')

    @points('10.word_game_part3')
    def test_14_rps_method_redefined(self):
        from src.word_game import WordGame, RockPaperScissors
        self.assertTrue(WordGame.round_winner is not RockPaperScissors.round_winner, 
            f'Method round_winner must be redefined in class ' + 
            'RockPaperScissors!')

    @points('10.word_game_part3')
    def test_15_rps_play_not_changed(self):
        from src.word_game import WordGame, RockPaperScissors
        self.assertTrue(WordGame.play is RockPaperScissors.play, 
            f'Method play() must not be redefined in class ' + 
            'RockPaperScissors!')

    @points('10.word_game_part3')
    def test_16_rps_works(self):
        test_cases = [("rock","scissors","paper","rock","scissors","paper",3,0), 
            ("paper","scissors","rock","paper",0,2), 
            ("rock","rock","paper","paper","scissors","scissors",0,0),
            ("rock","boat","dynamite","scissors","car","bike",1,1)]
        for test_case in test_cases:
            from src.word_game import RockPaperScissors
            with patch('builtins.input', side_effect=list(test_case[:-2])):
                game = RockPaperScissors(len(test_case)//2 - 1)
                game.play()

                output = get_stdout()
                val = [x.strip() for x in output.split("\n") if len(x.strip()) > 0][-2:]
                corr = [f"player 1: {test_case[-2]}", f"player 2: {test_case[-1]}"]

                val_str = "\n".join(val)
                corr_str = "\n".join(corr)
                test_str = "\n".join(test_case[:-2])

                self.assertEqual(val, corr, f'The game should output\n{corr_str}\n' + 
                    f'Not it outputs\n{val_str}\nwhen input was \n{test_str}')    
    
if __name__ == '__main__':
    unittest.main()
