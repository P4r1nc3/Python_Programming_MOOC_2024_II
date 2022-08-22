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

exercise = 'src.hockey_statistics'

def s(l: list):
    return "\n".join(l)

@points('12.hockey_statistics2')
class HockeyStatistics2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["partial.json", "0"]):
           cls.module = load_module(exercise, 'en')

    def test_01_team_players_1(self):
        input_values = ["partial.json", "4" , "WSH", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your code does not output anything. Check that it is not inside if __name__ == "__main__" block.')

            exp = """Jakub Vrana          WSH  25 + 27 =  52
Jonas Siegenthaler   WSH   2 +  7 =   9"""

            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"Your program should output line\n{line}\nwhen the program is executed with input\n{s(input_values)}\nNow the output was\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"when the program is executed with input\n{s(input_values)}\nOutput \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"when the program is executed with input\n{s(input_values)}\nOutput \n{output}\nis not in correct order, it should be\n{exp}")  

    def test_02_team_players_2(self):
        input_values = ["partial.json", "4" , "DAL", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

            output = get_stdout()

            exp = """John Klingberg       DAL   6 + 26 =  32
Taylor Fedun         DAL   2 +  7 =   9"""

            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"Your program should output line\n{line}\nwhen the program is executed with input\n{s(input_values)}\nNow the output was\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"when the program is executed with input\n{s(input_values)}\nOutput \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"when the program is executed with input\n{s(input_values)}\nOutput \n{output}\nis not in correct order, it should be\n{exp}")  

    def test_03_country_players_1(self):
        input_values = ["partial.json", "5" , "CAN", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

            output = get_stdout()

            exp = """Jared McCann         PIT  14 + 21 =  35
Travis Zajac         NJD   9 + 16 =  25
Taylor Fedun         DAL   2 +  7 =   9
Mark Jankowski       CGY   5 +  2 =   7
Logan Shaw           WPG   3 +  2 =   5"""

            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"Your program should output line\n{line}\nwhen the program is executed with input\n{s(input_values)}\nNow the output was\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"when the program is executed with input\n{s(input_values)}\nOutput \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"when the program is executed with input\n{s(input_values)}\nOutput \n{output}\nis not in correct order, it should be\n{exp}")  

    def test_04_country_players_2(self):
        input_values = ["partial.json", "5" , "SWE", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

            output = get_stdout()

            exp = """John Klingberg       DAL   6 + 26 =  32
Jonathan Davidsson   OTT   0 +  1 =   1"""

            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"Your program should output line\n{line}\nwhen the program is executed with input\n{s(input_values)}\nNow the output was\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"when the program is executed with input\n{s(input_values)}\nOutput \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"when the program is executed with input\n{s(input_values)}\nOutput \n{output}\nis not in correct order, it should be\n{exp}")  
    
    def test_05_country_players_big_file_1(self):
        input_values = ["all.json", "5" , "AUS", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

            output = get_stdout()

            exp = """Nathan Walker        STL   1 +  1 =   2"""

            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"Your program should output line\n{line}\nwhen the program is executed with input\n{s(input_values)}\nNow the output was\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"when the program is executed with input\n{s(input_values)}\nOutput \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"when the program is executed with input\n{s(input_values)}\nOutput \n{output}\nis not in correct order, it should be\n{exp}")  

    def test_06_country_players_big_file_2(self):
        input_values = ["all.json", "5" , "AUT", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

            output = get_stdout()

            exp = """Michael Raffl        PHI   8 + 12 =  20
Michael Grabner      ARI   8 +  3 =  11"""

            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"Your program should output line\n{line}\nwhen the program is executed with input\n{s(input_values)}\nNow the output was\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"when the program is executed with input\n{s(input_values)}\nOutput \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"when the program is executed with input\n{s(input_values)}\nOutput \n{output}\nis not in correct order, it should be\n{exp}")  

if __name__ == '__main__':
    unittest.main()