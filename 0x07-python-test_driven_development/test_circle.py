import unittest
from circle import area
from math import pi

class TestCircle(unittest.TestCase):
    def test_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(area(1), pi) # The first argument is the output of that method and the 2nd argument is the actual answer
        self.assertAlmostEqual(area(0), 0)  # The python unittest framwork will compare this 2 values and if they are not equal Python register that the test_area() method failed
        self.assertAlmostEqual(area(2.1), pi * (2.1 ** 2))
    def test_value(self):
        self.assertRaises(ValueError, area, -2) # The first argument is the exception class that should be raised the 2nd is the function and the 3rd is arghument that pass to the function
    def test_type(self):
        self.assertRaises(TypeError, area, 5+ 6j)
        self.assertRaises(TypeError, area, "Radius")
        self.assertRaises(TypeError, area, True)
