import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source

@points('13.clock')
class Part13Test(unittest.TestCase):
    def test_1_pygame(self):
        pass

if __name__ == '__main__':
    unittest.main()
