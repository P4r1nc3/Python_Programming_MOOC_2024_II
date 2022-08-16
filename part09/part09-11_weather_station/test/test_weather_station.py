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

exercise = 'src.weather_station'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('9.weather_station')
class WeatherStationTest(unittest.TestCase):
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

    def test_1_class_exists(self):
        try:
            from src.weather_station import WeatherStation
            a = WeatherStation("Kumpula")
        except Exception as e:
            self.fail(f'Calling constructor WeatherStation("Kumpula") threw an error \n{e}\n' + 
            'Make sure, that class is defined.')

    def test_2_methods_exists(self):
        from src.weather_station import WeatherStation
        a = WeatherStation("Kumpula")
        try:
             val = a.number_of_observations()
             taip = str(type(val)).replace("<class '","").replace("'>","")
             self.assertTrue(type(val) == int, f'Method call number_of_observations() should return an integer. ' +
                f'Now it returns a value {val} which is of type {taip}.')
        except Exception as e:
            self.fail(f'Program\na=WeatherStation("Kumpula")\nm=a.number_of_observations() threw an error \n{e}')

        try:
             val = a.latest_observation()
             taip = str(type(val)).replace("<class '","").replace("'>","")
             self.assertTrue(type(val) == str, f'Method latest_observation should return a string. ' +
                f'Now it returns a value {val} which is of type {taip}.')
        except Exception as e:
            self.fail(f'Program\na=WeatherStation("Kumpula")\nm=a.latest_observation() threw an error \n{e}')

        try:
             a.add_observation("x")
        except Exception as e:
            self.fail(f'Program\na=WeatherStation("Kumpula")\nm=a.add_observation("x") threw an error \n{e}')

    def test3_test_attributes(self):
        from src.weather_station import WeatherStation
        a = WeatherStation("Kumpula")
        ref = reflect.Reflect()
        ref.set_object(a)

        att_list = ["number_of_observations", "latest_observation", "add_observation"]
        for attribute in att_list:
            self.assertTrue(ref.has_attribute(attribute), f'Class WeatherStation should have attribubte ' + 
                f'{attribute}.')

        att = ref.list_public_members()
        att.remove("number_of_observations")
        att.remove("latest_observation")
        att.remove("add_observation")

        self.assertEqual(len(att), 0, f'Class WeatherStation should not have other public members than ' +
            f'methods number_of_observations, latest_observation and add_observation.' +  
            f'\nNow, however, it have following public members:\n'+ f(att))

    def test4_test_functionality(self):     
        from src.weather_station import WeatherStation
        a = WeatherStation("Kumpula")

        test_cases = ["Raining","Thunderstom","Raining snow", "Sun is shining", "Raining"]
        tests = ""
        n = 0
        for test_case in test_cases:
            n += 1
            a.add_observation(test_case)
            tests += f"\nadd_observation({test_case})"

            self.assertEqual(n, a.number_of_observations(), f'Method number_of_observations should return {n} ' + 
                f'wen following methdo calls has been after initializing the object:{tests}\n' + 
                f'Now method returns {a.number_of_observations()}')

            self.assertEqual(test_case, a.latest_observation(), f'Method latest_observation should return {test_case} ' + 
                f'wen following methdo calls has been after initializing the object:{tests}\n' + 
                f'Now method returns {a.latest_observation()}')
                
    def test5_test_str(self):
        from src.weather_station import WeatherStation

        for nimi in ["Kumpula", "Turku", "Iisalmi"]:
            a = WeatherStation(nimi)
            test_cases = ["Raining","Thunderstom","Raining snow", "Sun is shining", "Raining"]
            tests = ""
            n = 0
            for test_case in test_cases:
                n += 1
                a.add_observation(test_case)
                tests += f"\nadd_observation({test_case})"
                corr = f"{nimi}, {n} observations"
                var = str(a)

                self.assertEqual(var, corr, f'The printout of the object should be {corr} ' + 
                    f'wen following methdo calls has been after initializing the object:{tests}\n' + 
                    f'Now method __str__ returns {var}')

if __name__ == '__main__':
    unittest.main()
