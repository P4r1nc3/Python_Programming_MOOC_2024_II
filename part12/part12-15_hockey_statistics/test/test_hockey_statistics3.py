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

@points('12.hockey_statistics_part3')
class HockeyStatistics3Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["partial.json", "0"]):
           cls.module = load_module(exercise, 'en')

    def test_01_most_points_1(self):
        input_values = ["partial.json", "6" , "2", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check thath the program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your code does not output anything. Check that it is not inside if __name__ == "__main__" block.')

            exp = """Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Your program should output line\n{line}\nwhen the program is executed with input\n{s(input_values)}\nNow the output was\n{output}")   
            
            not_expected = "John Klingberg       DAL   6 + 26 =  32"
            self.assertFalse(not_expected in output, f"Program output must NOT contain\n{not_expected}\nwith input\n{s(input_values)}\nThe output was\n{output}")
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"When the program is executed with input\n{s(input_values)}\noutput \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"When the program is executed with input\n{s(input_values)}\noutput \n{output}\nis not in correct order, it should be\n{exp}")  

    def test_02_most_points_2(self):
        input_values = ["partial.json", "6" , "4", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check thath the program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your program does not output anything. Check that it is not insde if __name__ == "__main__" block!')

            exp = """Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35
John Klingberg       DAL   6 + 26 =  32
Travis Zajac         NJD   9 + 16 =  25"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Your program should contain line{rivi}\nWhen the program is executed with input\n{s(input_values)}\nThe output was\n{output}")   
            
            not_expected = "Conor Sheary         BUF  10 + 13 =  23"
            self.assertFalse(not_expected in output, f"Program output must NOT contain\n{not_expected}\nwith input\n{s(input_values)}\nThe output was\n{output}\nEttei vaan ohjelmasi tulosta liian monta pelaajaa?")
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"When the program is executed with input\n{s(input_values)}\noutput \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"When the program is executed with input\n{s(input_values)}\noutput \n{output}\nis not in correct order, it should be\n{exp}")  

    def test_03_most_points_big_input_values(self):
        input_values = ["all.json", "6" , "4", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check thath the program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your program does not output anything. Check that it is not insde if __name__ == "__main__" block!')

            exp = """Leon Draisaitl       EDM  43 + 67 = 110
Connor McDavid       EDM  34 + 63 =  97
Artemi Panarin       NYR  32 + 63 =  95
David Pastrnak       BOS  48 + 47 =  95"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Your program should contain line{rivi}\nWhen the program is executed with input\n{s(input_values)}\nThe output was\n{output}")   
            
            not_expected = "Nathan MacKinnon     COL  35 + 58 =  933"
            self.assertFalse(not_expected in output, f"Program output must NOT contain\n{not_expected}\nwith input\n{s(input_values)}\nThe output was\n{output}\nEttei vaan ohjelmasi tulosta liian monta pelaajaa?")
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(2):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"When the program is executed with input\n{s(input_values)}\noutput \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"When the program is executed with input\n{s(input_values)}\noutput \n{output}\nis not in correct order, it should be\n{exp}")  


    def test_04_most_goals1(self):
        input_values = ["partial.json", "7" , "3", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check thath the program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your program does not output anything. Check that it is not insde if __name__ == "__main__" block!')

            exp = """Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35
Conor Sheary         BUF  10 + 13 =  23"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Your program should contain line{rivi}\nWhen the program is executed with input\n{s(input_values)}\nThe output was\n{output}")   
            
            not_expected = "Travis Zajac         NJD   9 + 16 =  25"
            self.assertFalse(not_expected in output, f"Program output must NOT contain\n{not_expected}\nwith input\n{s(input_values)}\nThe output was\n{output}\nEttei vaan ohjelmasi tulosta liian monta pelaajaa?")
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"When the program is executed with input\n{s(input_values)}\noutput \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"When the program is executed with input\n{s(input_values)}\noutput \n{output}\nis not in correct order, it should be\n{exp}")  

    def test_05_most_goals2(self):
        input_values = ["partial.json", "7" , "7", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check thath the program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your program does not output anything. Check that it is not insde if __name__ == "__main__" block!')

            exp = """Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35
Conor Sheary         BUF  10 + 13 =  23
Travis Zajac         NJD   9 + 16 =  25
John Klingberg       DAL   6 + 26 =  32
Mark Jankowski       CGY   5 +  2 =   7
Adam Lowry           WPG   4 +  6 =  10"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Your program should contain line{rivi}\nWhen the program is executed with input\n{s(input_values)}\nThe output was\n{output}")   
            
            not_expected = "Drake Batherson      OTT   3 +  7 =  10"
            self.assertFalse(not_expected in output, f"Program output must NOT contain\n{not_expected}\nwith input\n{s(input_values)}\nThe output was\n{output}\nEttei vaan ohjelmasi tulosta liian monta pelaajaa?")
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"When the program is executed with input\n{s(input_values)}\noutput \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"When the program is executed with input\n{s(input_values)}\noutput \n{output}\nis not in correct order, it should be\n{exp}")  
    
    def test_05_most_goalsbig_input_values_1(self):
        input_values = ["all.json", "7" , "3", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check thath the program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your program does not output anything. Check that it is not insde if __name__ == "__main__" block!')

            exp = """Alex Ovechkin        WSH  48 + 19 =  67
David Pastrnak       BOS  48 + 47 =  95
Auston Matthews      TOR  47 + 33 =  80"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Your program should contain line{rivi}\nWhen the program is executed with input\n{s(input_values)}\nThe output was\n{output}")   
            
            not_expected = "Leon Draisaitl       EDM  43 + 67 = 110"
            self.assertFalse(not_expected in output, f"Program output must NOT contain\n{not_expected}\nwith input\n{s(input_values)}\nThe output was\n{output}\nEttei vaan ohjelmasi tulosta liian monta pelaajaa?")
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"When the program is executed with input\n{s(input_values)}\noutput \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"When the program is executed with input\n{s(input_values)}\noutput \n{output}\nis not in correct order, it should be\n{exp}. Jos maalimäärä on tasan, ratkaisee se kummalla on vähemmän otteluita")  

    def test_06_most_goalsbig_input_values_2(self):
        input_values = ["all.json", "7" , "9", "0"]
        with patch('builtins.input', side_effect=input_values):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Check thath the program works with input\n{s(input_values)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Your program does not output anything. Check that it is not insde if __name__ == "__main__" block!')

            exp = """Alex Ovechkin        WSH  48 + 19 =  67
David Pastrnak       BOS  48 + 47 =  95
Auston Matthews      TOR  47 + 33 =  80
Leon Draisaitl       EDM  43 + 67 = 110
Mika Zibanejad       NYR  41 + 34 =  75
Sebastian Aho        CAR  38 + 28 =  66
Kyle Connor          WPG  38 + 35 =  73
Jack Eichel          BUF  36 + 42 =  78
Nathan MacKinnon     COL  35 + 58 =  93"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Your program should contain line{rivi}\nWhen the program is executed with input\n{s(input_values)}\nThe output was\n{output}")   
            
            not_expected = "Connor McDavid       EDM  34 + 63 =  97"
            self.assertFalse(not_expected in output, f"Program output must NOT contain\n{not_expected}\nwith input\n{s(input_values)}\nThe output was\n{output}\nEttei vaan ohjelmasi tulosta liian monta pelaajaa?")
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"When the program is executed with input\n{s(input_values)}\noutput \n{output}\nis not in correct order, it should be\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"When the program is executed with input\n{s(input_values)}\noutput \n{output}\nis not in correct order, it should be\n{exp}")  


if __name__ == '__main__':
    unittest.main()