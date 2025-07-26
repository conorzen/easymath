# RealMaths 🧮

**Natural mathematical expressions for everyone!**

RealMaths lets you write mathematical expressions the way you think about them, without needing to know programming syntax. Perfect for students, teachers, researchers, and anyone who wants to do math without learning to code.

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)](https://github.com/yourusername/easymath)

## ✨ Features

- **🎯 Natural notation**: Write `4n + 1` instead of `4*n + 1`
- **🚫 No coding required**: Perfect for non-programmers
- **🔧 Built-in functions**: SIN, COS, SQRT, LOG, and more (UPPERCASE)
- **💾 Reusable formulas**: Define once, use many times
- **❗ Helpful errors**: Clear messages when something goes wrong
- **📚 Comprehensive**: Works for basic math through advanced calculations
- **🔒 Safe**: Secure evaluation of mathematical expressions
- **🎨 Clear distinction**: UPPERCASE for functions/constants, lowercase for variables

## 🚀 Quick Start

### Installation

```bash
pip install realmaths
```
or for uv

```bash
uv pip install realmaths
```
### Basic Usage

```python
from realmaths import EasyMath

calc = EasyMath()

# Simple calculations
result = calc.eval("4n + 1", n=5)  # Returns 21
print(result)

# Use mathematical functions (UPPERCASE)
area = calc.eval("PI * r^2", r=3)  # Circle area
print(f"Circle area: {area:.2f}")

# Define your own formulas
calc.define("compound_interest", "P(1 + r)^t")
money = calc.calculate("compound_interest", P=1000, r=0.05, t=10)
print(f"Investment value: ${money:.2f}")
```

### Even Quicker

```python
from realmaths import calculate

# One-line calculations
result = calculate("2x^2 + 3x - 1", x=4)  # Returns 43
distance = calculate("SQRT((x2-x1)^2 + (y2-y1)^2)", x1=0, y1=0, x2=3, y2=4)  # Returns 5.0
```

## 📚 Examples

### Basic Mathematics
```python
calc = EasyMath()

# Arithmetic with variables
calc.eval("2x + 3", x=5)           # 13
calc.eval("x^2 + 2x + 1", x=3)     # 16

# Using constants and functions (UPPERCASE)
calc.eval("PI * r^2", r=5)          # ~78.54
calc.eval("SIN(PI/2)")              # 1.0
calc.eval("SQRT(x^2 + y^2)", x=3, y=4)  # 5.0
calc.eval("EXP(x)", x=2)              # ~7.39
```

### Science & Engineering
```python
# Physics: kinetic energy
calc.define("kinetic_energy", "0.5 * m * v^2")
energy = calc.calculate("kinetic_energy", m=10, v=25)  # 3125 J

# Chemistry: ideal gas law
calc.define("ideal_gas", "n * R * T / P")  # V = nRT/P
volume = calc.calculate("ideal_gas", n=2, R=8.314, T=298, P=101325)

# Engineering: stress calculation
calc.define("stress", "F / A")
stress = calc.calculate("stress", F=1000, A=0.01)  # 100,000 Pa
```

### Finance
```python
# Compound interest
calc.define("compound", "P * (1 + r/n)^(n*t)")
amount = calc.calculate("compound", P=1000, r=0.05, n=12, t=5)

# Loan payments
calc.define("payment", "P * (r*(1+r)^n) / ((1+r)^n - 1)")
monthly = calc.calculate("payment", P=200000, r=0.04/12, n=30*12)

# Investment growth
calc.define("cagr", "((FV/PV)^(1/n)) - 1")
growth = calc.calculate("cagr", FV=1500, PV=1000, n=5)

# advance compound interest
calc.define("compound", "p(1+r/n)^(nt)")

for i in range(1,12):
  amount = calc.calculate("compound", p=1000, r=0.05, n=12, t=i)
  print(f"Investment vale: {amount:.2f} at year: {i}")
```

### Education
```python
# Quadratic formula solver
from realmaths import solve_quadratic
x1, x2 = solve_quadratic(1, -5, 6)  # Solves x² - 5x + 6 = 0
print(f"Solutions: x₁={x1}, x₂={x2}")  # Solutions: x₁=3.0, x₂=2.0

# Distance formula
calc.define("distance", "SQRT((x2-x1)^2 + (y2-y1)^2)")
dist = calc.calculate("distance", x1=0, y1=0, x2=3, y2=4)  # 5.0

# Trigonometry
calc.eval("SIN(30 * PI/180)")       # sin(30°) = 0.5
calc.eval("COS(PI/3)")              # cos(60°) = 0.5
```

## 🎯 Perfect For

- **👨‍🎓 Students**: Write math naturally without syntax errors
- **👩‍🏫 Teachers**: Create interactive examples and problem solvers
- **🔬 Researchers**: Quick calculations without complex setup
- **📊 Analysts**: Financial and statistical calculations
- **🏗️ Engineers**: Formula-based calculations
- **💡 Anyone**: Who wants to do math without learning programming

## 📖 Documentation

### Capitalization Convention

RealMaths uses a clear capitalization system to distinguish between functions/constants and variables:

- **UPPERCASE**: Functions and constants (`SIN`, `COS`, `PI`, `E`, `SQRT`)
- **lowercase**: Variables (`x`, `y`, `a`, `b`, `c`)

This prevents ambiguity and makes expressions clear:
```python
# Functions and constants (UPPERCASE)
calc.eval("SIN(PI/2)")     # Function call
calc.eval("2PI")           # Constant (2 * π)

# Variables (lowercase)
calc.eval("ax^2 + bx + c", a=1, b=2, c=3, x=2)  # Variables
```

### Supported Operations
| Operation | Syntax | Example |
|-----------|--------|---------|
| Addition | `+` | `x + y` |
| Subtraction | `-` | `x - y` |
| Multiplication | `*` or implicit | `2*x` or `2x` |
| Division | `/` | `x / y` |
| Exponentiation | `^` or `**` | `x^2` or `x**2` |
| Square/Cube | `²` `³` | `x²` or `x³` |

### Built-in Functions (UPPERCASE)
| Category | Functions |
|----------|-----------|
| **Trigonometric** | `SIN`, `COS`, `TAN`, `ASIN`, `ACOS`, `ATAN` |
| **Hyperbolic** | `SINH`, `COSH`, `TANH` |
| **Logarithmic** | `LOG`, `LN`, `LOG10`, `LOG2` |
| **Exponential** | `EXP`, `EXP2` |
| **Power/Root** | `SQRT`, `CBRT`, `POW` |
| **Rounding** | `ABS`, `ROUND`, `FLOOR`, `CEIL` |
| **Comparison** | `MIN`, `MAX` |

### Constants (UPPERCASE)
| Constant | Value | Description |
|----------|-------|-------------|
| `π`, `PI` | 3.14159... | Pi |
| `E` | 2.71828... | Euler's number |
| `TAU` | 6.28318... | Tau (2π) |
| `INF` | ∞ | Infinity |

### Function Management
```python
# Define a reusable function
calc.define("function_name", "mathematical_expression", "optional description")

# Use the function
result = calc.calculate("function_name", variable1=value1, variable2=value2)

# Manage functions
calc.list_functions()                    # Show all defined functions
calc.delete_function("function_name")    # Delete a function
calc.get_function_info("function_name")  # Get function details
```

### Getting Help
```python
calc.help()           # Show comprehensive help
calc.list_functions() # Show your defined functions

# Quick help
from realmath import quick_help
quick_help()
```

## 🔧 Advanced Features

### Error Handling
RealMaths provides helpful error messages:

```python
# Missing variable
calc.eval("x + y", x=1)  # VariableError: Missing variables: y

# Invalid syntax  
calc.eval("2x +")        # ExpressionError: Invalid expression syntax

# Mathematical errors
calc.eval("1/0")         # MathematicalError: Division by zero
```

### Safe Mode
By default, RealMaths runs in safe mode to prevent code injection:

```python
calc = EasyMath(safe_mode=True)   # Default: safe evaluation
calc = EasyMath(safe_mode=False)  # Allow more Python features
```

### Validation
```python
from realmath import is_valid_expression, get_expression_variables

# Check if expression is valid
if is_valid_expression("2x + 3"):
    print("Valid expression!")

# Get variables in expression
vars_list = get_expression_variables("ax^2 + bx + c")
print(vars_list)  # ['a', 'b', 'c', 'x']
```

## 🧪 Examples by Domain

### Physics
```python
calc.define("kinetic_energy", "0.5 * m * v^2")
calc.define("potential_energy", "m * g * h") 
calc.define("wave_speed", "f * λ")
calc.define("ohms_law", "V / R")
```

### Chemistry  
```python
calc.define("ideal_gas", "n * R * T / P")
calc.define("ph_calculation", "-log10(H_concentration)")
calc.define("molarity", "moles / volume_L")
```

### Finance
```python
calc.define("compound_interest", "P * (1 + r/n)^(n*t)")
calc.define("present_value", "FV / (1 + r)^n")
calc.define("loan_payment", "P * (r*(1+r)^n) / ((1+r)^n - 1)")
```

### Statistics
```python
calc.define("mean", "sum_values / n")
calc.define("variance", "sum_squared_deviations / (n-1)")
calc.define("standard_deviation", "sqrt(variance)")
calc.define("z_score", "(x - μ) / σ")
```

### Geometry
```python
calc.define("circle_area", "π * r^2")
calc.define("sphere_volume", "(4/3) * π * r^3") 
calc.define("triangle_area", "0.5 * base * height")
calc.define("distance_2d", "sqrt((x2-x1)^2 + (y2-y1)^2)")
```

## 🛠️ Development

### Running Tests
```bash
pip install pytest
pytest tests/
```

### Development Installation
```bash
git clone https://github.com/yourusername/easymath.git
cd easymath
pip install -e .
```

### Running Examples
```bash
python -m easymath.examples
```

## 🤝 Contributing

We welcome contributions! RealMaths is designed to make math accessible to everyone.

1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

See `CONTRIBUTING.md` for detailed guidelines.

## 📋 Requirements

- Python 3.7+
- No external dependencies (uses only Python standard library)

## 📄 License

MIT License - feel free to use in your projects, educational materials, and research.

## 🙏 Acknowledgments

- Inspired by the need to make mathematics accessible to non-programmers
- Built for educators, students, and researchers worldwide
- Special thanks to the Python mathematics community

## 📞 Support

- 📚 [Documentation](https://github.com/yourusername/easymath#readme)
- 🐛 [Issue Tracker](https://github.com/yourusername/easymath/issues)
- 💬 [Discussions](https://github.com/yourusername/easymath/discussions)
- 📧 Email: your.email@example.com

---

**Made with ❤️ for the math community**

*RealMaths: Because mathematics should be about the math, not the syntax.*
