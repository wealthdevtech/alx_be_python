import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(8, 3), 11)
        self.assertEqual(self.calc.add(0, 1), 1)
        self.assertEqual(self.calc.add(0, -3), -3)
        self.assertEqual(self.calc.add(-2, -3), -5)
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(8, 3), 5)
        self.assertEqual(self.calc.subtract(0, 1), -1)
        self.assertEqual(self.calc.subtract(0, -3), -3)
        self.assertEqual(self.calc.subtract(-2, -3), -5)
        
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(8, 3), 24)
        self.assertEqual(self.calc.multiply(0, 1), 0)
        self.assertEqual(self.calc.multiply(0, -3), 0)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        
    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 3), 0.66)
        self.assertEqual(self.calc.divide(8, 3), 2.66)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(0, -3), 0)
        self.assertEqual(self.calc.divide(1, 0), None)
        self.assertEqual(self.calc.divide(-3, 0), None)
        self.assertEqual(self.calc.divide(-3, -1), 3)
        self.assertEqual(self.calc.divide(-3, 1), -3)
        