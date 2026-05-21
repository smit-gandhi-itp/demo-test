#!/usr/bin/env python3
"""
Math Calculator Module

A comprehensive Python module that provides various mathematical calculation functions
including basic arithmetic, advanced operations, trigonometry, statistics, and more.
"""

import math
from typing import List, Union


class MathCalculator:
    """A comprehensive calculator class with various mathematical operations."""

    # ==================== BASIC ARITHMETIC ====================

    @staticmethod
    def add(*args: Union[int, float]) -> Union[int, float]:
        """Add multiple numbers together.
        
        Args:
            *args: Variable number of numeric arguments
            
        Returns:
            Sum of all arguments
            
        Example:
            >>> MathCalculator.add(5, 3, 2)
            10
        """
        return sum(args)

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a.
        
        Args:
            a: First number (minuend)
            b: Second number (subtrahend)
            
        Returns:
            Difference (a - b)
            
        Example:
            >>> MathCalculator.subtract(10, 3)
            7
        """
        return a - b

    @staticmethod
    def multiply(*args: Union[int, float]) -> Union[int, float]:
        """Multiply multiple numbers together.
        
        Args:
            *args: Variable number of numeric arguments
            
        Returns:
            Product of all arguments
            
        Example:
            >>> MathCalculator.multiply(5, 3, 2)
            30
        """
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> float:
        """Divide a by b.
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            Quotient (a / b)
            
        Raises:
            ZeroDivisionError: If b is zero
            
        Example:
            >>> MathCalculator.divide(10, 2)
            5.0
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    @staticmethod
    def modulo(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Calculate remainder of a divided by b.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Remainder (a % b)
            
        Example:
            >>> MathCalculator.modulo(10, 3)
            1
        """
        if b == 0:
            raise ZeroDivisionError("Cannot calculate modulo with zero divisor")
        return a % b

    @staticmethod
    def floor_divide(a: Union[int, float], b: Union[int, float]) -> int:
        """Floor division of a by b.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Floor quotient (a // b)
            
        Example:
            >>> MathCalculator.floor_divide(10, 3)
            3
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a // b

    # ==================== POWER & ROOT OPERATIONS ====================

    @staticmethod
    def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Calculate base raised to the power of exponent.
        
        Args:
            base: Base number
            exponent: Exponent
            
        Returns:
            base ** exponent
            
        Example:
            >>> MathCalculator.power(2, 3)
            8
        """
        return base ** exponent

    @staticmethod
    def square(n: Union[int, float]) -> Union[int, float]:
        """Calculate square of a number.
        
        Args:
            n: Number to square
            
        Returns:
            n squared
            
        Example:
            >>> MathCalculator.square(5)
            25
        """
        return n ** 2

    @staticmethod
    def cube(n: Union[int, float]) -> Union[int, float]:
        """Calculate cube of a number.
        
        Args:
            n: Number to cube
            
        Returns:
            n cubed
            
        Example:
            >>> MathCalculator.cube(3)
            27
        """
        return n ** 3

    @staticmethod
    def square_root(n: Union[int, float]) -> float:
        """Calculate square root of a number.
        
        Args:
            n: Number (must be non-negative)
            
        Returns:
            Square root of n
            
        Raises:
            ValueError: If n is negative
            
        Example:
            >>> MathCalculator.square_root(16)
            4.0
        """
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(n)

    @staticmethod
    def nth_root(n: Union[int, float], root: Union[int, float]) -> float:
        """Calculate nth root of a number.
        
        Args:
            n: Number
            root: Root degree
            
        Returns:
            nth root of n
            
        Example:
            >>> MathCalculator.nth_root(27, 3)
            3.0
        """
        return n ** (1 / root)

    # ==================== TRIGONOMETRIC FUNCTIONS ====================

    @staticmethod
    def sin(angle: Union[int, float], degrees: bool = False) -> float:
        """Calculate sine of an angle.
        
        Args:
            angle: Angle value
            degrees: If True, angle is in degrees; otherwise radians
            
        Returns:
            Sine of the angle
            
        Example:
            >>> MathCalculator.sin(90, degrees=True)
            1.0
        """
        if degrees:
            angle = math.radians(angle)
        return math.sin(angle)

    @staticmethod
    def cos(angle: Union[int, float], degrees: bool = False) -> float:
        """Calculate cosine of an angle.
        
        Args:
            angle: Angle value
            degrees: If True, angle is in degrees; otherwise radians
            
        Returns:
            Cosine of the angle
            
        Example:
            >>> MathCalculator.cos(0, degrees=True)
            1.0
        """
        if degrees:
            angle = math.radians(angle)
        return math.cos(angle)

    @staticmethod
    def tan(angle: Union[int, float], degrees: bool = False) -> float:
        """Calculate tangent of an angle.
        
        Args:
            angle: Angle value
            degrees: If True, angle is in degrees; otherwise radians
            
        Returns:
            Tangent of the angle
            
        Example:
            >>> MathCalculator.tan(45, degrees=True)
            1.0
        """
        if degrees:
            angle = math.radians(angle)
        return math.tan(angle)

    # ==================== LOGARITHMIC FUNCTIONS ====================

    @staticmethod
    def log(n: Union[int, float], base: Union[int, float] = math.e) -> float:
        """Calculate logarithm of n with given base.
        
        Args:
            n: Number (must be positive)
            base: Logarithm base (default: e for natural log)
            
        Returns:
            Logarithm of n with given base
            
        Raises:
            ValueError: If n is not positive
            
        Example:
            >>> MathCalculator.log(100, 10)
            2.0
        """
        if n <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers")
        return math.log(n, base)

    @staticmethod
    def log10(n: Union[int, float]) -> float:
        """Calculate base-10 logarithm.
        
        Args:
            n: Number (must be positive)
            
        Returns:
            Base-10 logarithm of n
            
        Example:
            >>> MathCalculator.log10(1000)
            3.0
        """
        if n <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers")
        return math.log10(n)

    @staticmethod
    def ln(n: Union[int, float]) -> float:
        """Calculate natural logarithm (base e).
        
        Args:
            n: Number (must be positive)
            
        Returns:
            Natural logarithm of n
            
        Example:
            >>> MathCalculator.ln(math.e)
            1.0
        """
        if n <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers")
        return math.log(n)

    # ==================== STATISTICAL FUNCTIONS ====================

    @staticmethod
    def mean(numbers: List[Union[int, float]]) -> float:
        """Calculate arithmetic mean (average).
        
        Args:
            numbers: List of numbers
            
        Returns:
            Mean of the numbers
            
        Raises:
            ValueError: If list is empty
            
        Example:
            >>> MathCalculator.mean([1, 2, 3, 4, 5])
            3.0
        """
        if not numbers:
            raise ValueError("Cannot calculate mean of empty list")
        return sum(numbers) / len(numbers)

    @staticmethod
    def median(numbers: List[Union[int, float]]) -> float:
        """Calculate median value.
        
        Args:
            numbers: List of numbers
            
        Returns:
            Median of the numbers
            
        Raises:
            ValueError: If list is empty
            
        Example:
            >>> MathCalculator.median([1, 2, 3, 4, 5])
            3
        """
        if not numbers:
            raise ValueError("Cannot calculate median of empty list")
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        return sorted_numbers[mid]

    @staticmethod
    def mode(numbers: List[Union[int, float]]) -> Union[int, float]:
        """Calculate mode (most frequent value).
        
        Args:
            numbers: List of numbers
            
        Returns:
            Mode of the numbers
            
        Raises:
            ValueError: If list is empty
            
        Example:
            >>> MathCalculator.mode([1, 2, 2, 3, 4])
            2
        """
        if not numbers:
            raise ValueError("Cannot calculate mode of empty list")
        frequency = {}
        for num in numbers:
            frequency[num] = frequency.get(num, 0) + 1
        return max(frequency, key=frequency.get)

    @staticmethod
    def variance(numbers: List[Union[int, float]], sample: bool = True) -> float:
        """Calculate variance.
        
        Args:
            numbers: List of numbers
            sample: If True, calculate sample variance; otherwise population variance
            
        Returns:
            Variance of the numbers
            
        Example:
            >>> MathCalculator.variance([1, 2, 3, 4, 5])
            2.5
        """
        if not numbers:
            raise ValueError("Cannot calculate variance of empty list")
        avg = MathCalculator.mean(numbers)
        squared_diffs = [(x - avg) ** 2 for x in numbers]
        divisor = len(numbers) - 1 if sample else len(numbers)
        return sum(squared_diffs) / divisor

    @staticmethod
    def standard_deviation(numbers: List[Union[int, float]], sample: bool = True) -> float:
        """Calculate standard deviation.
        
        Args:
            numbers: List of numbers
            sample: If True, calculate sample std dev; otherwise population std dev
            
        Returns:
            Standard deviation of the numbers
            
        Example:
            >>> MathCalculator.standard_deviation([1, 2, 3, 4, 5])
            1.58...
        """
        return math.sqrt(MathCalculator.variance(numbers, sample))

    # ==================== SPECIAL FUNCTIONS ====================

    @staticmethod
    def factorial(n: int) -> int:
        """Calculate factorial of n.
        
        Args:
            n: Non-negative integer
            
        Returns:
            n! (factorial of n)
            
        Raises:
            ValueError: If n is negative
            
        Example:
            >>> MathCalculator.factorial(5)
            120
        """
        if n < 0:
            raise ValueError("Factorial undefined for negative numbers")
        return math.factorial(n)

    @staticmethod
    def gcd(*args: int) -> int:
        """Calculate greatest common divisor of multiple numbers.
        
        Args:
            *args: Variable number of integers
            
        Returns:
            GCD of all arguments
            
        Example:
            >>> MathCalculator.gcd(12, 18, 24)
            6
        """
        if not args:
            return 0
        result = args[0]
        for num in args[1:]:
            result = math.gcd(result, num)
        return result

    @staticmethod
    def lcm(*args: int) -> int:
        """Calculate least common multiple of multiple numbers.
        
        Args:
            *args: Variable number of integers
            
        Returns:
            LCM of all arguments
            
        Example:
            >>> MathCalculator.lcm(4, 6, 8)
            24
        """
        if not args:
            return 0
        result = args[0]
        for num in args[1:]:
            result = abs(result * num) // math.gcd(result, num)
        return result

    @staticmethod
    def absolute(n: Union[int, float]) -> Union[int, float]:
        """Calculate absolute value.
        
        Args:
            n: Number
            
        Returns:
            Absolute value of n
            
        Example:
            >>> MathCalculator.absolute(-5)
            5
        """
        return abs(n)

    @staticmethod
    def ceiling(n: Union[int, float]) -> int:
        """Round up to nearest integer.
        
        Args:
            n: Number
            
        Returns:
            Smallest integer >= n
            
        Example:
            >>> MathCalculator.ceiling(4.3)
            5
        """
        return math.ceil(n)

    @staticmethod
    def floor(n: Union[int, float]) -> int:
        """Round down to nearest integer.
        
        Args:
            n: Number
            
        Returns:
            Largest integer <= n
            
        Example:
            >>> MathCalculator.floor(4.7)
            4
        """
        return math.floor(n)

    @staticmethod
    def round_number(n: Union[int, float], decimals: int = 0) -> Union[int, float]:
        """Round to specified decimal places.
        
        Args:
            n: Number to round
            decimals: Number of decimal places
            
        Returns:
            Rounded number
            
        Example:
            >>> MathCalculator.round_number(3.14159, 2)
            3.14
        """
        return round(n, decimals)

    # ==================== PERCENTAGE CALCULATIONS ====================

    @staticmethod
    def percentage(part: Union[int, float], whole: Union[int, float]) -> float:
        """Calculate what percentage 'part' is of 'whole'.
        
        Args:
            part: Part value
            whole: Whole value
            
        Returns:
            Percentage
            
        Example:
            >>> MathCalculator.percentage(25, 100)
            25.0
        """
        if whole == 0:
            raise ZeroDivisionError("Cannot calculate percentage with zero whole")
        return (part / whole) * 100

    @staticmethod
    def percentage_of(percentage: Union[int, float], whole: Union[int, float]) -> float:
        """Calculate what value is 'percentage' percent of 'whole'.
        
        Args:
            percentage: Percentage value
            whole: Whole value
            
        Returns:
            Calculated value
            
        Example:
            >>> MathCalculator.percentage_of(20, 100)
            20.0
        """
        return (percentage / 100) * whole

    @staticmethod
    def percentage_change(old_value: Union[int, float], new_value: Union[int, float]) -> float:
        """Calculate percentage change from old to new value.
        
        Args:
            old_value: Original value
            new_value: New value
            
        Returns:
            Percentage change (positive for increase, negative for decrease)
            
        Example:
            >>> MathCalculator.percentage_change(100, 120)
            20.0
        """
        if old_value == 0:
            raise ZeroDivisionError("Cannot calculate percentage change from zero")
        return ((new_value - old_value) / old_value) * 100


def main():
    """Demonstration of MathCalculator functionality."""
    print("=" * 60)
    print("Math Calculator - Comprehensive Demonstration")
    print("=" * 60)

    # Basic Arithmetic
    print("\n[BASIC ARITHMETIC]")
    print(f"Add (5, 3, 2): {MathCalculator.add(5, 3, 2)}")
    print(f"Subtract (10, 3): {MathCalculator.subtract(10, 3)}")
    print(f"Multiply (5, 3, 2): {MathCalculator.multiply(5, 3, 2)}")
    print(f"Divide (10, 2): {MathCalculator.divide(10, 2)}")
    print(f"Modulo (10, 3): {MathCalculator.modulo(10, 3)}")
    print(f"Floor Divide (10, 3): {MathCalculator.floor_divide(10, 3)}")

    # Power & Root Operations
    print("\n[POWER & ROOT OPERATIONS]")
    print(f"Power (2, 3): {MathCalculator.power(2, 3)}")
    print(f"Square (5): {MathCalculator.square(5)}")
    print(f"Cube (3): {MathCalculator.cube(3)}")
    print(f"Square Root (16): {MathCalculator.square_root(16)}")
    print(f"Nth Root (27, 3): {MathCalculator.nth_root(27, 3)}")

    # Trigonometric Functions
    print("\n[TRIGONOMETRIC FUNCTIONS]")
    print(f"Sin (90°): {MathCalculator.sin(90, degrees=True):.4f}")
    print(f"Cos (0°): {MathCalculator.cos(0, degrees=True):.4f}")
    print(f"Tan (45°): {MathCalculator.tan(45, degrees=True):.4f}")

    # Logarithmic Functions
    print("\n[LOGARITHMIC FUNCTIONS]")
    print(f"Log (100, base 10): {MathCalculator.log(100, 10)}")
    print(f"Log10 (1000): {MathCalculator.log10(1000)}")
    print(f"Natural Log (e): {MathCalculator.ln(math.e):.4f}")

    # Statistical Functions
    print("\n[STATISTICAL FUNCTIONS]")
    numbers = [1, 2, 3, 4, 5]
    print(f"Numbers: {numbers}")
    print(f"Mean: {MathCalculator.mean(numbers)}")
    print(f"Median: {MathCalculator.median(numbers)}")
    print(f"Variance: {MathCalculator.variance(numbers):.2f}")
    print(f"Standard Deviation: {MathCalculator.standard_deviation(numbers):.2f}")

    # Special Functions
    print("\n[SPECIAL FUNCTIONS]")
    print(f"Factorial (5): {MathCalculator.factorial(5)}")
    print(f"GCD (12, 18, 24): {MathCalculator.gcd(12, 18, 24)}")
    print(f"LCM (4, 6, 8): {MathCalculator.lcm(4, 6, 8)}")
    print(f"Absolute (-5): {MathCalculator.absolute(-5)}")
    print(f"Ceiling (4.3): {MathCalculator.ceiling(4.3)}")
    print(f"Floor (4.7): {MathCalculator.floor(4.7)}")
    print(f"Round (3.14159, 2 decimals): {MathCalculator.round_number(3.14159, 2)}")

    # Percentage Calculations
    print("\n[PERCENTAGE CALCULATIONS]")
    print(f"Percentage (25 of 100): {MathCalculator.percentage(25, 100)}%")
    print(f"20% of 100: {MathCalculator.percentage_of(20, 100)}")
    print(f"Percentage Change (100 to 120): {MathCalculator.percentage_change(100, 120)}%")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
