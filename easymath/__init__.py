"""
EasyMath - Natural Mathematical Expressions for Python

A user-friendly package that allows natural mathematical notation
for people with no coding experience.

Features:
- Write math expressions naturally (4n + 1 instead of 4*n + 1)
- Built-in mathematical functions and constants
- Define reusable formulas
- Helpful error messages
- No programming knowledge required

Basic Usage:
    from easymath import EasyMath
    
    calc = EasyMath()
    result = calc.eval("4n + 1", n=5)  # Returns 21
    
    # Define reusable functions
    calc.define("area_circle", "π * r^2")
    area = calc.calculate("area_circle", r=5)

Quick Usage:
    from easymath import calculate
    
    result = calculate("2x^2 + 3x - 1", x=4)  # Returns 43
"""

from .core import EasyMath, calculate, solve_quadratic
from .exceptions import EasyMathError, ExpressionError, VariableError

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"
__license__ = "MIT"

__all__ = [
    "EasyMath",
    "calculate", 
    "solve_quadratic",
    "EasyMathError",
    "ExpressionError", 
    "VariableError"
]

# Package metadata
__title__ = "EasyMath"
__description__ = "Natural mathematical expressions for non-programmers"
__url__ = "https://github.com/yourusername/easymath"

def get_version():
    """Return the current version of EasyMath."""
    return __version__

def quick_help():
    """Display quick help for EasyMath usage."""
    help_text = """
EasyMath Quick Help
==================

Basic usage:
  from easymath import EasyMath
  calc = EasyMath()
  result = calc.eval("4n + 1", n=5)

Quick calculations:
  from easymath import calculate
  result = calculate("x^2 + 2x + 1", x=3)

Common examples:
  calc.eval("π * r^2", r=5)           # Circle area
  calc.eval("sqrt(a^2 + b^2)", a=3, b=4)  # Pythagorean theorem
  calc.eval("sin(π/2)")               # Trigonometry

For more help: calc.help()
"""
    print(help_text)

# Optional: Auto-create a default calculator instance
default_calc = EasyMath()

def eval_expression(expression, **variables):
    """Quick evaluation using the default calculator instance."""
    return default_calc.eval(expression, **variables)