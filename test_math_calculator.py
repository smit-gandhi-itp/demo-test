#!/usr/bin/env python3
"""
Unit Tests for Math Calculator Module

Comprehensive test suite for the MathCalculator class.
"""

import unittest
import math
from math_calculator import MathCalculator


class TestBasicArithmetic(unittest.TestCase):
    """Test basic arithmetic operations."""

    def test_add(self):
        self.assertEqual(MathCalculator.add(5, 3, 2), 10)
        self.assertEqual(MathCalculator.add(10), 10)
        self.assertEqual(MathCalculator.add(-5, 5), 0)

    def test_subtract(self):
        self.assertEqual(MathCalculator.subtract(10, 3), 7)
        self.assertEqual(MathCalculator.subtract(5, 10), -5)
        self.assertEqual(MathCalculator.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(MathCalculator.multiply(5, 3, 2), 30)
        self.assertEqual(MathCalculator.multiply(10), 10)
        self.assertEqual(MathCalculator.multiply(5, 0), 0)

    def test_divide(self):
        self.assertEqual(MathCalculator.divide(10, 2), 5.0)
        self.assertEqual(MathCalculator.divide(7, 2), 3.5)
        with self.assertRaises(ZeroDivisionError):
            MathCalculator.divide(10, 0)

    def test_modulo(self):
        self.assertEqual(MathCalculator.modulo(10, 3), 1)
        self.assertEqual(MathCalculator.modulo(10, 5), 0)
        with self.assertRaises(ZeroDivisionError):
            MathCalculator.modulo(10, 0)

    def test_floor_divide(self):
        self.assertEqual(MathCalculator.floor_divide(10, 3), 3)
        self.assertEqual(MathCalculator.floor_divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            MathCalculator.floor_divide(10, 0)


class TestPowerAndRoot(unittest.TestCase):
    """Test power and root operations."""

    def test_power(self):
        self.assertEqual(MathCalculator.power(2, 3), 8)
        self.assertEqual(MathCalculator.power(5, 0), 1)
        self.assertEqual(MathCalculator.power(10, 2), 100)

    def test_square(self):
        self.assertEqual(MathCalculator.square(5), 25)
        self.assertEqual(MathCalculator.square(0), 0)
        self.assertEqual(MathCalculator.square(-3), 9)

    def test_cube(self):
        self.assertEqual(MathCalculator.cube(3), 27)
        self.assertEqual(MathCalculator.cube(0), 0)
        self.assertEqual(MathCalculator.cube(-2), -8)

    def test_square_root(self):
        self.assertEqual(MathCalculator.square_root(16), 4.0)
        self.assertEqual(MathCalculator.square_root(0), 0.0)
        with self.assertRaises(ValueError):
            MathCalculator.square_root(-1)

    def test_nth_root(self):
        self.assertAlmostEqual(MathCalculator.nth_root(27, 3), 3.0)
        self.assertAlmostEqual(MathCalculator.nth_root(16, 4), 2.0)


class TestTrigonometric(unittest.TestCase):
    """Test trigonometric functions."""

    def test_sin(self):
        self.assertAlmostEqual(MathCalculator.sin(90, degrees=True), 1.0)
        self.assertAlmostEqual(MathCalculator.sin(0, degrees=True), 0.0)
        self.assertAlmostEqual(MathCalculator.sin(math.pi / 2), 1.0)

    def test_cos(self):
        self.assertAlmostEqual(MathCalculator.cos(0, degrees=True), 1.0)
        self.assertAlmostEqual(MathCalculator.cos(90, degrees=True), 0.0, places=5)
        self.assertAlmostEqual(MathCalculator.cos(0), 1.0)

    def test_tan(self):
        self.assertAlmostEqual(MathCalculator.tan(45, degrees=True), 1.0)
        self.assertAlmostEqual(MathCalculator.tan(0, degrees=True), 0.0)


class TestLogarithmic(unittest.TestCase):
    """Test logarithmic functions."""

    def test_log(self):
        self.assertAlmostEqual(MathCalculator.log(100, 10), 2.0)
        self.assertAlmostEqual(MathCalculator.log(8, 2), 3.0)
        with self.assertRaises(ValueError):
            MathCalculator.log(0)
        with self.assertRaises(ValueError):
            MathCalculator.log(-1)

    def test_log10(self):
        self.assertAlmostEqual(MathCalculator.log10(1000), 3.0)
        self.assertAlmostEqual(MathCalculator.log10(100), 2.0)
        with self.assertRaises(ValueError):
            MathCalculator.log10(0)

    def test_ln(self):
        self.assertAlmostEqual(MathCalculator.ln(math.e), 1.0)
        self.assertAlmostEqual(MathCalculator.ln(1), 0.0)
        with self.assertRaises(ValueError):
            MathCalculator.ln(0)


class TestStatistical(unittest.TestCase):
    """Test statistical functions."""

    def test_mean(self):
        self.assertEqual(MathCalculator.mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(MathCalculator.mean([10]), 10.0)
        with self.assertRaises(ValueError):
            MathCalculator.mean([])

    def test_median(self):
        self.assertEqual(MathCalculator.median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(MathCalculator.median([1, 2, 3, 4]), 2.5)
        self.assertEqual(MathCalculator.median([5]), 5)
        with self.assertRaises(ValueError):
            MathCalculator.median([])

    def test_mode(self):
        self.assertEqual(MathCalculator.mode([1, 2, 2, 3, 4]), 2)
        self.assertEqual(MathCalculator.mode([5, 5, 5, 1, 2]), 5)
        with self.assertRaises(ValueError):
            MathCalculator.mode([])

    def test_variance(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(MathCalculator.variance(numbers), 2.5)
        with self.assertRaises(ValueError):
            MathCalculator.variance([])

    def test_standard_deviation(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(MathCalculator.standard_deviation(numbers), 1.5811, places=4)
        with self.assertRaises(ValueError):
            MathCalculator.standard_deviation([])


class TestSpecialFunctions(unittest.TestCase):
    """Test special mathematical functions."""

    def test_factorial(self):
        self.assertEqual(MathCalculator.factorial(5), 120)
        self.assertEqual(MathCalculator.factorial(0), 1)
        with self.assertRaises(ValueError):
            MathCalculator.factorial(-1)

    def test_gcd(self):
        self.assertEqual(MathCalculator.gcd(12, 18, 24), 6)
        self.assertEqual(MathCalculator.gcd(10, 15), 5)
        self.assertEqual(MathCalculator.gcd(7, 13), 1)

    def test_lcm(self):
        self.assertEqual(MathCalculator.lcm(4, 6, 8), 24)
        self.assertEqual(MathCalculator.lcm(3, 5), 15)

    def test_absolute(self):
        self.assertEqual(MathCalculator.absolute(-5), 5)
        self.assertEqual(MathCalculator.absolute(5), 5)
        self.assertEqual(MathCalculator.absolute(0), 0)

    def test_ceiling(self):
        self.assertEqual(MathCalculator.ceiling(4.3), 5)
        self.assertEqual(MathCalculator.ceiling(4.0), 4)
        self.assertEqual(MathCalculator.ceiling(-4.3), -4)

    def test_floor(self):
        self.assertEqual(MathCalculator.floor(4.7), 4)
        self.assertEqual(MathCalculator.floor(4.0), 4)
        self.assertEqual(MathCalculator.floor(-4.7), -5)

    def test_round_number(self):
        self.assertEqual(MathCalculator.round_number(3.14159, 2), 3.14)
        self.assertEqual(MathCalculator.round_number(3.5), 4)


class TestPercentage(unittest.TestCase):
    """Test percentage calculations."""

    def test_percentage(self):
        self.assertEqual(MathCalculator.percentage(25, 100), 25.0)
        self.assertEqual(MathCalculator.percentage(50, 200), 25.0)
        with self.assertRaises(ZeroDivisionError):
            MathCalculator.percentage(10, 0)

    def test_percentage_of(self):
        self.assertEqual(MathCalculator.percentage_of(20, 100), 20.0)
        self.assertEqual(MathCalculator.percentage_of(50, 80), 40.0)

    def test_percentage_change(self):
        self.assertEqual(MathCalculator.percentage_change(100, 120), 20.0)
        self.assertEqual(MathCalculator.percentage_change(100, 80), -20.0)
        with self.assertRaises(ZeroDivisionError):
            MathCalculator.percentage_change(0, 10)


if __name__ == "__main__":
    unittest.main()
