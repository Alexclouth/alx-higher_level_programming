import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertAlmostEqual(calculator.add(5, 10), 5 + 10)

if __name__ == "__main__":
    unittest.main()
