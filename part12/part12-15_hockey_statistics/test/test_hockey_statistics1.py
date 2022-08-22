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

def f(attr: list):
    return ",".join(attr)

def s(l: list):
    return "\n".join(l)

@points('12.hockey_statistics_part1')
class HockeyStatistics1Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["partial.json", "0"]):
           cls.module = load_module(exercise, 'en')

    def test_01_stops(self):
        input_values = ["partial.json", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

    def test_02_amount_and_instructions_outpu(self):
        input_values = ["partial.json", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your code does not output anything. Check that it is not inside if __name__ == "__main__" block.')

            exp = """read the data of 14 players
commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals
"""
            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"The program should output\n{line}\nwhen the program is executed as\n{s(input_values)}\nNow the output was\n{output}")   
            
            eiodotettu = "added!"
            self.assertFalse(eiodotettu in output, f"The program output should not contain\n{eiodotettu}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   

    def test_03_amount_and_instructions_output_2(self):
        input_values = ["all.json", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

            output = get_stdout()

            exp = """read the data of 964 players
commands:
"""
            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"The program should output\n{line}\nwhen the program is executed as\n{s(input_values)}\nNow the output was\n{output}")   
            
            eiodotettu = "added!"
            self.assertFalse(eiodotettu in output, f"The program output should not contain\n{eiodotettu}\nwith input\n{s(input_values)}\nNow the output was\n{output}")   

    def test_04_search_playesr(self):
        input_values = ["partial.json", "1", "John Klingberg" ,"0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your code does not output anything. Check that it is not inside if __name__ == "__main__" block.')

            exp = """John Klingberg       DAL   6 + 26 =  32"""
            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"The program should output\n{line}\nwhen the program is executed as\n{s(input_values)}\nNow the output was\n{output}")   

    def test_05_search_teams(self):
        input_values = ["partial.json", "2" ,"0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your code does not output anything. Check that it is not inside if __name__ == "__main__" block.')

            exp = """BUF
CGY
DAL
NJD
NYI
OTT
PIT
WPG
WSH"""
            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"The program should output\n{line}\nwhen the program is executed as\n{s(input_values)}\nNow the output was\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"when the program is executed as\n{s(input_values)}\Output \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"when the program is executed as\n{s(input_values)}\Output \n{output}\nis not in correct order, it should be\n{exp}")  

    def test_06_search_for_countries(self):
        input_values = ["partial.json", "3" ,"0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your code does not output anything. Check that it is not inside if __name__ == "__main__" block.')

            exp = """CAN
CHE
CZE
SWE
USA"""
            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"The program should output\n{line}\nwhen the program is executed as\n{s(input_values)}\nNow the output was\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"when the program is executed as\n{s(input_values)}\Output \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"when the program is executed as\n{s(input_values)}\Output \n{output}\nis not in correct order, it should be\n{exp}")  


    def test_07_search_player_input_values_1(self):
        input_values = ["all.json", "1", "Mikko Koivu" ,"0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your code does not output anything. Check that it is not inside if __name__ == "__main__" block.')

            exp = """Mikko Koivu          MIN   4 + 17 =  21"""
            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"The program should output\n{line}\nwhen the program is executed as\n{s(input_values)}\nNow the output was\n{output}")   

    def test_08_search_player_input_values_2(self):
        input_values = ["all.json", "1", "Alex Ovechkin" ,"0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your code does not output anything. Check that it is not inside if __name__ == "__main__" block.')

            exp = """Alex Ovechkin        WSH  48 + 19 =  67"""
            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"The program should output\n{line}\nwhen the program is executed as\n{s(input_values)}\nNow the output was\n{output}")   



    def test_09_search_teams_big_input(self):
        input_values = ["all.json", "2" ,"0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your code does not output anything. Check that it is not inside if __name__ == "__main__" block.')

            exp = """ANA
ARI
BOS
BUF
CAR
CBJ
CGY
CHI
COL
DAL
DET
EDM
FLA
LAK
MIN
MTL
NJD
NSH
NYI
NYR
OTT
PHI
PIT
SJS
STL
TBL
TOR
VAN
VGK
WPG
WSH"""
            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"The program should output\n{line}\nwhen the program is executed as\n{s(input_values)}\nNow the output was\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"when the program is executed as\n{s(input_values)}\Output \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"when the program is executed as\n{s(input_values)}\Output \n{output}\nis not in correct order, it should be\n{exp}")  

    def test_10_search_for_countries_iso_input_values(self):
        input_values = ["all.json", "3" ,"0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check that your program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your code does not output anything. Check that it is not inside if __name__ == "__main__" block.')

            exp = """AUS
AUT
CAN
CHE
CZE
DEU
DNK
FIN
FRA
GBR
LVA
NLD
NOR
RUS
SVK
SVN
SWE
UKR
USA"""
            for line in exp.split("\n"):
                if not line in output:
                    self.fail(f"The program should output\n{line}\nwhen the program is executed as\n{s(input_values)}\nNow the output was\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"when the program is executed as\n{s(input_values)}\Output \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"when the program is executed as\n{s(input_values)}\Output \n{output}\nis not in correct order, it should be\n{exp}")  


if __name__ == '__main__':
    unittest.main()