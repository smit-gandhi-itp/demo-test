# demo-test

A Python demonstration repository featuring a comprehensive math calculator module.

## Features

### Math Calculator (`math_calculator.py`)

A complete mathematical calculation library with the following capabilities:

#### 1. Basic Arithmetic Operations
- **Addition**: Add multiple numbers
- **Subtraction**: Subtract two numbers
- **Multiplication**: Multiply multiple numbers
- **Division**: Divide with zero-check
- **Modulo**: Calculate remainder
- **Floor Division**: Integer division

#### 2. Power & Root Operations
- **Power**: Calculate base^exponent
- **Square**: Calculate n²
- **Cube**: Calculate n³
- **Square Root**: Calculate √n
- **Nth Root**: Calculate ⁿ√n

#### 3. Trigonometric Functions
- **Sine**: sin(angle) - supports degrees and radians
- **Cosine**: cos(angle) - supports degrees and radians
- **Tangent**: tan(angle) - supports degrees and radians

#### 4. Logarithmic Functions
- **Log**: Logarithm with custom base
- **Log10**: Base-10 logarithm
- **Natural Log (ln)**: Base-e logarithm

#### 5. Statistical Functions
- **Mean**: Arithmetic average
- **Median**: Middle value
- **Mode**: Most frequent value
- **Variance**: Measure of spread
- **Standard Deviation**: Square root of variance

#### 6. Special Functions
- **Factorial**: n!
- **GCD**: Greatest Common Divisor
- **LCM**: Least Common Multiple
- **Absolute**: |n|
- **Ceiling**: Round up
- **Floor**: Round down
- **Round**: Round to decimal places

#### 7. Percentage Calculations
- **Percentage**: Calculate what % part is of whole
- **Percentage Of**: Calculate x% of a number
- **Percentage Change**: Calculate % increase/decrease

## Installation

```bash
# Clone the repository
git clone https://github.com/smit-gandhi-itp/demo-test.git
cd demo-test
```

No external dependencies required - uses only Python standard library!

## Usage

### Running the Demo

```bash
python math_calculator.py
```

This will run a comprehensive demonstration of all calculator features.

### Using in Your Code

```python
from math_calculator import MathCalculator

# Basic arithmetic
result = MathCalculator.add(5, 3, 2)  # 10
result = MathCalculator.divide(10, 2)  # 5.0

# Power operations
result = MathCalculator.square(5)  # 25
result = MathCalculator.square_root(16)  # 4.0

# Trigonometry
result = MathCalculator.sin(90, degrees=True)  # 1.0
result = MathCalculator.cos(0, degrees=True)  # 1.0

# Statistics
numbers = [1, 2, 3, 4, 5]
mean = MathCalculator.mean(numbers)  # 3.0
median = MathCalculator.median(numbers)  # 3
std_dev = MathCalculator.standard_deviation(numbers)  # 1.58

# Special functions
fact = MathCalculator.factorial(5)  # 120
gcd = MathCalculator.gcd(12, 18, 24)  # 6
lcm = MathCalculator.lcm(4, 6, 8)  # 24

# Percentages
pct = MathCalculator.percentage(25, 100)  # 25.0
value = MathCalculator.percentage_of(20, 100)  # 20.0
change = MathCalculator.percentage_change(100, 120)  # 20.0
```

## Running Tests

```bash
python test_math_calculator.py
```

Or with verbose output:

```bash
python test_math_calculator.py -v
```

Or using unittest discovery:

```bash
python -m unittest discover -v
```

## Test Coverage

The test suite includes:
- ✅ 50+ unit tests
- ✅ All arithmetic operations
- ✅ All power and root operations
- ✅ All trigonometric functions
- ✅ All logarithmic functions
- ✅ All statistical functions
- ✅ All special functions
- ✅ All percentage calculations
- ✅ Error handling and edge cases

## Project Structure

```
demo-test/
├── .gitignore              # Python gitignore
├── README.md               # This file
├── hello_world.py          # Original hello world script
├── math_calculator.py      # Comprehensive math calculator module
└── test_math_calculator.py # Complete test suite
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Features Highlights

✨ **Comprehensive**: 30+ mathematical functions covering all common operations  
✨ **Well-Documented**: Every function has detailed docstrings with examples  
✨ **Type-Hinted**: Full type hints for better IDE support  
✨ **Tested**: Complete test suite with 50+ unit tests  
✨ **Error-Handled**: Proper exception handling for edge cases  
✨ **Zero Dependencies**: Uses only Python standard library  
✨ **Production-Ready**: Clean, maintainable, and extensible code  

## Examples

### Example 1: Basic Calculator

```python
from math_calculator import MathCalculator

# Simple calculations
print(MathCalculator.add(10, 20, 30))  # 60
print(MathCalculator.multiply(5, 4))   # 20
print(MathCalculator.divide(100, 4))   # 25.0
```

### Example 2: Scientific Calculator

```python
from math_calculator import MathCalculator
import math

# Advanced calculations
print(MathCalculator.power(2, 10))           # 1024
print(MathCalculator.log(1000, 10))          # 3.0
print(MathCalculator.sin(30, degrees=True))  # 0.5
```

### Example 3: Statistical Analysis

```python
from math_calculator import MathCalculator

data = [12, 15, 18, 20, 22, 25, 28, 30]

print(f"Mean: {MathCalculator.mean(data)}")
print(f"Median: {MathCalculator.median(data)}")
print(f"Std Dev: {MathCalculator.standard_deviation(data):.2f}")
print(f"Variance: {MathCalculator.variance(data):.2f}")
```

### Example 4: Financial Calculations

```python
from math_calculator import MathCalculator

# Calculate percentage increase
old_price = 100
new_price = 125
change = MathCalculator.percentage_change(old_price, new_price)
print(f"Price increased by {change}%")  # 25.0%

# Calculate discount
original = 200
discount_pct = 20
discount_amount = MathCalculator.percentage_of(discount_pct, original)
final_price = original - discount_amount
print(f"Final price after {discount_pct}% discount: ${final_price}")  # $160.0
```

## Contributing

Feel free to open issues or submit pull requests for improvements!

## License

This project is open source and available for educational purposes.

## Author

smit-gandhi-itp

---

**Happy Calculating! 🧮**
