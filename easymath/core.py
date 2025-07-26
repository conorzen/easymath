"""
Core functionality for EasyMath package.

This module contains the main EasyMath class and utility functions
for parsing and evaluating natural mathematical expressions.
"""

import re
import math
import operator
from typing import Dict, List, Union, Callable, Any, Optional, Tuple
from .exceptions import EasyMathError, ExpressionError, VariableError


class EasyMath:
    """
    Main class for natural mathematical expression handling.
    
    This class allows users to write mathematical expressions using
    natural notation and evaluates them with provided variables.
    
    Examples:
        calc = EasyMath()
        
        # Simple calculations
        result = calc.eval("4n + 1", n=5)  # Returns 21
        
        # Define reusable functions
        calc.define("area_circle", "π * r^2")
        area = calc.calculate("area_circle", r=3)
        
        # Work with multiple variables
        calc.define("quadratic", "ax^2 + bx + c")
        result = calc.calculate("quadratic", a=1, b=-5, c=6)
    """
    
    def __init__(self, safe_mode: bool = True):
        """
        Initialize EasyMath calculator.
        
        Args:
            safe_mode: If True, restricts to safe mathematical operations only
        """
        self.safe_mode = safe_mode
        self.functions = {}
        
        # Mathematical constants (capitalized to distinguish from variables)
        self.constants = {
            'π': math.pi,
            'PI': math.pi,
            'TAU': math.tau,
            'INF': math.inf,
            'INFINITY': math.inf,
        }
        
        # Built-in mathematical functions (capitalized to distinguish from variables)
        self.math_functions = {
            # Trigonometric functions
            'SIN': math.sin,
            'COS': math.cos,
            'TAN': math.tan,
            'ASIN': math.asin,
            'ACOS': math.acos,
            'ATAN': math.atan,
            'ATAN2': math.atan2,
            'SINH': math.sinh,
            'COSH': math.cosh,
            'TANH': math.tanh,
            
            # Logarithmic and exponential
            'LOG': math.log10,
            'LN': math.log,
            'LOG10': math.log10,
            'LOG2': math.log2,
            'EXP': math.exp,
            'EXP2': lambda x: 2**x,
            
            # Power and root functions
            'SQRT': math.sqrt,
            'CBRT': lambda x: x**(1/3),
            'POW': pow,
            
            # Rounding and absolute
            'ABS': abs,
            'ROUND': round,
            'FLOOR': math.floor,
            'CEIL': math.ceil,
            'TRUNC': math.trunc,
            
            # Min/max
            'MIN': min,
            'MAX': max,
            
            # Degree/radian conversion
            'RADIANS': math.radians,
            'DEGREES': math.degrees,
        }
    
    def _parse_expression(self, expr: str) -> str:
        """
        Convert natural math expressions to valid Python syntax.
        
        Args:
            expr: Natural mathematical expression
            
        Returns:
            Python-compatible expression string
            
        Examples:
            "4n + 1" -> "4*n + 1"
            "sin(π/2)" -> "sin(3.141592653589793/2)"
            "x^2 + 1" -> "x**2 + 1"
        """
        if not isinstance(expr, str):
            raise ExpressionError("Expression must be a string")
        
        # Store original for error messages
        original_expr = expr
        
        try:
            # Remove spaces for easier processing
            expr = expr.replace(' ', '')
            
            # Hard code specific problematic cases to prevent function name splitting
            # Replace function names with protected versions BEFORE any other processing
            function_protections = {
                'EXP': 'EXP_FUNCTION',
                'SQRT': 'SQRT_FUNCTION', 
                'LOG': 'LOG_FUNCTION',
                'LOG10': 'LOG10_FUNCTION',
                'LOG2': 'LOG2_FUNCTION',
                'LN': 'LN_FUNCTION',
                'SIN': 'SIN_FUNCTION',
                'COS': 'COS_FUNCTION',
                'TAN': 'TAN_FUNCTION',
                'ASIN': 'ASIN_FUNCTION',
                'ACOS': 'ACOS_FUNCTION',
                'ATAN': 'ATAN_FUNCTION',
                'SINH': 'SINH_FUNCTION',
                'COSH': 'COSH_FUNCTION',
                'TANH': 'TANH_FUNCTION',
                'ABS': 'ABS_FUNCTION',
                'FLOOR': 'FLOOR_FUNCTION',
                'CEIL': 'CEIL_FUNCTION',
                'ROUND': 'ROUND_FUNCTION',
                'TRUNC': 'TRUNC_FUNCTION',
                'MIN': 'MIN_FUNCTION',
                'MAX': 'MAX_FUNCTION',
                'POW': 'POW_FUNCTION',
                'DEGREES': 'DEGREES_FUNCTION',
                'RADIANS': 'RADIANS_FUNCTION',
                'CBRT': 'CBRT_FUNCTION',
                'EXP2': 'EXP2_FUNCTION',
                'ATAN2': 'ATAN2_FUNCTION',
            }
            
            # Protect function names first
            for func_name, protection in function_protections.items():
                expr = expr.replace(func_name, protection)
            
            # Replace mathematical symbols and notation
            replacements = [
                ('^', '**'),          # Exponentiation
                ('²', '**2'),         # Squared
                ('³', '**3'),         # Cubed
                ('√', 'sqrt'),        # Square root symbol
                ('∞', 'inf'),         # Infinity
            ]
            
            for old, new in replacements:
                expr = expr.replace(old, new)
            

            
            # Replace constants with their values
            for const, value in self.constants.items():
                expr = expr.replace(const, str(value))
            
            # Add implicit multiplication for number-constant combinations
            # This handles cases like "2π" -> "2*3.141592653589793"
            expr = re.sub(r'(\d+)(\d+\.\d+)', r'\1*\2', expr)
            
            # Add implicit multiplication signs
            # Number followed by variable/function name (but not function names)
            def repl_number_var(match):
                var_name = match.group(2).strip()
                # Check if this is a function name
                if var_name in self.math_functions:
                    return match.group(0)  # Don't modify function names
                return f"{match.group(1)}*{var_name}"
            
            expr = re.sub(r'(\d+)([a-zA-Z_]\w*)', repl_number_var, expr)
            
            # Add implicit multiplication for letter-letter combinations (like 'ax', 'bx')
            # But be very careful not to split function names
            def repl_letter_letter(match):
                first = match.group(1)
                second = match.group(2)
                combined = first + second
                
                # Don't modify if this is a known function name
                if combined in self.math_functions:
                    return match.group(0)
                
                # Don't modify if either is a function name
                if first in self.math_functions or second in self.math_functions:
                    return match.group(0)
                
                # Check if this might be part of a longer function name
                for func_name in self.math_functions:
                    if func_name.startswith(combined):
                        return match.group(0)
                
                # Check if this combination appears in any function name
                for func_name in self.math_functions:
                    if combined in func_name:
                        return match.group(0)
                
                # Check if this might be part of a function name that contains these letters
                for func_name in self.math_functions:
                    if first in func_name and second in func_name:
                        # Check if they appear in the right order
                        first_pos = func_name.find(first)
                        second_pos = func_name.find(second)
                        if first_pos < second_pos:
                            return match.group(0)
                
                # Only apply multiplication if we're confident it's not a function
                return f"{first}*{second}"
            
            # Add implicit multiplication for letter-letter combinations (like 'ax', 'bx')
            # Since we're using capitalization to distinguish functions from variables,
            # we can safely apply multiplication to lowercase combinations
            def repl_letter_letter(match):
                first = match.group(1)
                second = match.group(2)
                combined = first + second
                
                # Only apply multiplication if both letters are lowercase (variables)
                if first.islower() and second.islower():
                    return f"{first}*{second}"
                
                return match.group(0)
            
            expr = re.sub(r'([a-zA-Z])([a-zA-Z])', repl_letter_letter, expr)
            
            # Number followed by opening parenthesis
            expr = re.sub(r'(\d+)\(', r'\1*(', expr)
            
            # Closing parenthesis followed by variable/function (but not function names)
            def repl_paren_var(match):
                var_name = match.group(1)
                if var_name in self.math_functions:
                    return match.group(0)  # Don't modify function names
                return f")*{var_name}"
            
            expr = re.sub(r'\)([a-zA-Z_]\w*)', repl_paren_var, expr)
            
            # Closing parenthesis followed by number
            expr = re.sub(r'\)(\d+)', r')*\1', expr)
            
            # Variable/function followed by opening parenthesis
            # (but not for known functions)
            def repl_func(match):
                name = match.group(1)
                if name in self.math_functions:
                    return match.group(0)  # Don't modify function calls
                return f"{name}*("
            
            expr = re.sub(r'([a-zA-Z_]\w*)\(', repl_func, expr)
            
            # Closing parenthesis followed by opening parenthesis
            expr = re.sub(r'\)\(', r')*(', expr)
            
            # Clean up extra spaces around function names
            expr = re.sub(r'\s+', ' ', expr)  # Replace multiple spaces with single space
            expr = expr.strip()  # Remove leading/trailing spaces
            
            # Restore function names from protected versions
            function_restorations = {
                'EXP_FUNCTION': 'EXP',
                'SQRT_FUNCTION': 'SQRT',
                'LOG_FUNCTION': 'LOG',
                'LOG10_FUNCTION': 'LOG10',
                'LOG2_FUNCTION': 'LOG2',
                'LN_FUNCTION': 'LN',
                'SIN_FUNCTION': 'SIN',
                'COS_FUNCTION': 'COS',
                'TAN_FUNCTION': 'TAN',
                'ASIN_FUNCTION': 'ASIN',
                'ACOS_FUNCTION': 'ACOS',
                'ATAN_FUNCTION': 'ATAN',
                'SINH_FUNCTION': 'SINH',
                'COSH_FUNCTION': 'COSH',
                'TANH_FUNCTION': 'TANH',
                'ABS_FUNCTION': 'ABS',
                'FLOOR_FUNCTION': 'FLOOR',
                'CEIL_FUNCTION': 'CEIL',
                'ROUND_FUNCTION': 'ROUND',
                'TRUNC_FUNCTION': 'TRUNC',
                'MIN_FUNCTION': 'MIN',
                'MAX_FUNCTION': 'MAX',
                'POW_FUNCTION': 'POW',
                'DEGREES_FUNCTION': 'DEGREES',
                'RADIANS_FUNCTION': 'RADIANS',
                'CBRT_FUNCTION': 'CBRT',
                'EXP2_FUNCTION': 'EXP2',
                'ATAN2_FUNCTION': 'ATAN2',
            }
            
            # Restore function names
            for protection, func_name in function_restorations.items():
                expr = expr.replace(protection, func_name)
            
            # Fix function calls that got extra multiplication signs
            # This handles cases like 'exp*(1)' -> 'exp(1)'
            for func_name in self.math_functions:
                expr = expr.replace(f"{func_name}*(", f"{func_name}(")
            
            return expr
            
        except Exception as e:
            raise ExpressionError(f"Error parsing expression '{original_expr}': {str(e)}")
    
    def _extract_variables(self, expr: str) -> List[str]:
        """
        Extract variable names from a mathematical expression.
        
        Args:
            expr: Mathematical expression
            
        Returns:
            List of variable names found in the expression
        """
        # First, replace special symbols to avoid them being treated as variables
        temp_expr = expr
        temp_expr = temp_expr.replace('²', '**2')
        temp_expr = temp_expr.replace('³', '**3')
        temp_expr = temp_expr.replace('√', 'sqrt')
        temp_expr = temp_expr.replace('∞', 'inf')
        
        # Find all potential variable names (letters, possibly with numbers/underscores)
        potential_vars = set(re.findall(r'[a-zA-Z_]\w*', temp_expr))
        
        # Remove known functions and constants
        variables = potential_vars - set(self.math_functions.keys())
        variables = variables - set(self.constants.keys())
        
        # Remove Python built-ins that might appear
        python_builtins = {'abs', 'min', 'max', 'round', 'pow', 'sum'}
        variables = variables - python_builtins
        
        # Also check for multi-letter combinations that might be functions
        # For example, if we have 'ax' but 'a' and 'x' are separate variables
        final_variables = set()
        for var in variables:
            # If this is a multi-letter variable, check if it could be split into functions
            if len(var) > 1:
                # Check if any part of this variable is a function name
                is_function_part = False
                for func_name in self.math_functions:
                    if func_name in var or var in func_name:
                        is_function_part = True
                        break
                
                if not is_function_part:
                    final_variables.add(var)
            else:
                final_variables.add(var)
        
        return sorted(list(final_variables))
    
    def _create_eval_context(self, variables: Dict[str, Any]) -> Dict[str, Any]:
        """Create a safe evaluation context with variables and functions."""
        context = {}
        
        # Add user variables
        context.update(variables)
        
        # Add mathematical functions
        context.update(self.math_functions)
        
        # Add constants
        context.update(self.constants)
        
        return context
    
    def eval(self, expression: str, **variables) -> Union[float, int]:
        """
        Evaluate a mathematical expression with given variables.
        
        Args:
            expression: Natural math expression like "4n + 1" or "2x^2 + 3x - 1"
            **variables: Variable values as keyword arguments
            
        Returns:
            Numerical result of the expression
            
        Raises:
            ExpressionError: If the expression cannot be parsed or evaluated
            VariableError: If required variables are missing
            
        Examples:
            calc.eval("4n + 1", n=5)  # Returns 21
            calc.eval("x^2 + 2x + 1", x=3)  # Returns 16
            calc.eval("sin(π/2)")  # Returns 1.0
        """
        if not expression or not expression.strip():
            raise ExpressionError("Expression cannot be empty")
        
        try:
            # Parse the expression
            parsed = self._parse_expression(expression)
            
            # Check for obvious syntax errors in the parsed expression
            if parsed.endswith(('+', '-', '*', '/', '^', '**')):
                raise ExpressionError(f"Invalid expression: '{expression}' ends with an operator")
            
            # Check for unmatched parentheses
            if parsed.count('(') != parsed.count(')'):
                raise ExpressionError(f"Invalid expression: '{expression}' has unmatched parentheses")
            
            # Extract required variables from the parsed expression
            required_vars = self._extract_variables(parsed)
            
            # Check for missing variables
            missing_vars = set(required_vars) - set(variables.keys())
            if missing_vars:
                raise VariableError(
                    f"Missing variables: {', '.join(sorted(missing_vars))}. "
                    f"Required variables: {', '.join(sorted(required_vars))}"
                )
            
            # Create evaluation context
            context = self._create_eval_context(variables)
            
            # Evaluate the expression safely
            if self.safe_mode:
                # Restrict built-ins for security
                safe_builtins = {
                    '__builtins__': {
                        'abs': abs,
                        'round': round,
                        'min': min,
                        'max': max,
                        'pow': pow,
                    }
                }
                result = eval(parsed, safe_builtins, context)
            else:
                result = eval(parsed, {"__builtins__": {}}, context)
            
            return result
            
        except VariableError:
            raise  # Re-raise variable errors as-is
        except ExpressionError:
            raise  # Re-raise expression errors as-is
        except SyntaxError as e:
            raise ExpressionError(f"Invalid expression syntax: {expression}")
        except ZeroDivisionError:
            raise EasyMathError("Division by zero")
        except ValueError as e:
            raise EasyMathError(f"Mathematical error: {str(e)}")
        except Exception as e:
            raise EasyMathError(f"Error evaluating '{expression}': {str(e)}")
    
    def define(self, name: str, expression: str, description: str = "") -> None:
        """
        Define a reusable mathematical function.
        
        Args:
            name: Function name (must be a valid Python identifier)
            expression: Mathematical expression
            description: Optional description of what the function does
            
        Raises:
            ValueError: If name is invalid or expression cannot be parsed
            
        Examples:
            calc.define("area_circle", "π * r^2", "Area of a circle")
            calc.define("quadratic", "ax^2 + bx + c", "Quadratic equation")
        """
        # Validate function name
        if not name or not name.isidentifier():
            raise ValueError(f"Invalid function name: '{name}'. Must be a valid identifier.")
        
        # Check for conflicts with built-in functions and constants (case-insensitive)
        built_in_names = {name.upper() for name in self.math_functions.keys()} | set(self.constants.keys())
        if name.upper() in built_in_names:
            raise ValueError(f"Cannot redefine built-in function or constant: '{name}'")
        
        try:
            # Test parsing
            self._parse_expression(expression)
            variables = self._extract_variables(expression)
            
            self.functions[name] = {
                'expression': expression,
                'variables': variables,
                'description': description,
                'parsed': self._parse_expression(expression)
            }
            
            print(f"✓ Defined function '{name}({', '.join(variables)})' = {expression}")
            if description:
                print(f"  Description: {description}")
                
        except Exception as e:
            raise ValueError(f"Cannot define function '{name}': {str(e)}")
    
    def calculate(self, function_name: str, **variables) -> Union[float, int]:
        """
        Calculate using a predefined function.
        
        Args:
            function_name: Name of the function to use
            **variables: Variable values as keyword arguments
            
        Returns:
            Numerical result
            
        Raises:
            ValueError: If function doesn't exist
            VariableError: If required variables are missing
            
        Examples:
            calc.calculate("area_circle", r=5)
            calc.calculate("quadratic", a=1, b=-2, c=1)
        """
        if function_name not in self.functions:
            available = list(self.functions.keys())
            if available:
                raise ValueError(
                    f"Function '{function_name}' not defined. "
                    f"Available functions: {', '.join(available)}"
                )
            else:
                raise ValueError(
                    f"Function '{function_name}' not defined. "
                    f"No functions defined yet. Use define() first."
                )
        
        func_info = self.functions[function_name]
        return self.eval(func_info['expression'], **variables)
    
    def list_functions(self) -> None:
        """Display all defined functions."""
        if not self.functions:
            print("No functions defined yet. Use define() to create some!")
            return
        
        print("Defined Functions:")
        print("-" * 50)
        for name, info in self.functions.items():
            vars_str = ', '.join(info['variables']) if info['variables'] else 'no variables'
            print(f"{name}({vars_str}) = {info['expression']}")
            if info['description']:
                print(f"  → {info['description']}")
            print()
    
    def delete_function(self, name: str) -> None:
        """Delete a defined function."""
        if name not in self.functions:
            raise ValueError(f"Function '{name}' not found")
        
        del self.functions[name]
        print(f"✓ Deleted function '{name}'")
    
    def get_function_info(self, name: str) -> Dict[str, Any]:
        """Get information about a defined function."""
        if name not in self.functions:
            raise ValueError(f"Function '{name}' not found")
        
        return self.functions[name].copy()
    
    def help(self) -> None:
        """Show comprehensive help and examples."""
        help_text = """
EasyMath - Natural Mathematical Expressions
==========================================

BASIC USAGE:
  calc = EasyMath()
  result = calc.eval("4n + 1", n=5)  # Returns 21

SUPPORTED OPERATIONS:
  + - * /          Addition, subtraction, multiplication, division
  ^  **            Exponentiation (both ^ and ** work)
  ²  ³             Squared and cubed (or use ^2, ^3)
  
SUPPORTED FUNCTIONS (UPPERCASE):
  Trigonometric:   SIN, COS, TAN, ASIN, ACOS, ATAN
  Hyperbolic:      SINH, COSH, TANH
  Logarithmic:     LOG, LN, LOG10, LOG2
  Exponential:     EXP, EXP2
  Power/Root:      SQRT, CBRT, POW
  Rounding:        ABS, ROUND, FLOOR, CEIL, TRUNC
  Comparison:      MIN, MAX
  Conversion:      RADIANS, DEGREES

CONSTANTS (UPPERCASE):
  π, PI            Pi (3.14159...)
  E                Euler's number (2.71828...)
  TAU              Tau (2π)
  INF, INFINITY    Infinity

EXAMPLES:
  # Simple calculations
  calc.eval("2x + 3", x=5)              # Returns 13
  calc.eval("x^2 + 2x + 1", x=3)        # Returns 16
  
  # Using functions and constants (UPPERCASE)
  calc.eval("SIN(PI/2)")                 # Returns 1.0
  calc.eval("SQRT(x^2 + y^2)", x=3, y=4) # Returns 5.0
  calc.eval("LOG10(1000)")               # Returns 3.0
  
  # Define reusable functions
  calc.define("area_circle", "PI * r^2", "Area of a circle")
  calc.calculate("area_circle", r=5)     # Returns ~78.54
  
  # Multiple variables
  calc.define("distance", "SQRT((x2-x1)^2 + (y2-y1)^2)")
  calc.calculate("distance", x1=0, y1=0, x2=3, y2=4)  # Returns 5.0

FUNCTION MANAGEMENT:
  calc.list_functions()                  # Show all defined functions
  calc.delete_function("function_name")  # Delete a function
  calc.get_function_info("function_name") # Get function details

TIP: Write mathematical expressions naturally - EasyMath handles the conversion!

ERROR HANDLING:
  - Missing variables will be clearly identified
  - Invalid expressions will show helpful error messages
  - Mathematical errors (like division by zero) are caught and explained
        """
        print(help_text)


def calculate(expression: str, **variables) -> Union[float, int]:
    """
    Quick calculation without creating an EasyMath instance.
    
    Args:
        expression: Mathematical expression
        **variables: Variable values
        
    Returns:
        Calculation result
        
    Examples:
        calculate("4n + 1", n=5)  # Returns 21
        calculate("x^2 + 1", x=3)  # Returns 10
    """
    calc = EasyMath()
    return calc.eval(expression, **variables)


def solve_quadratic(a: float, b: float, c: float) -> Tuple[Optional[float], Optional[float]]:
    """
    Solve quadratic equation ax^2 + bx + c = 0.
    
    Args:
        a, b, c: Coefficients of the quadratic equation
        
    Returns:
        Tuple of solutions (x1, x2). Returns (None, None) if no real solutions.
        
    Examples:
        solve_quadratic(1, -5, 6)   # Returns (3.0, 2.0)
        solve_quadratic(1, 0, 1)    # Returns (None, None) - no real solutions
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation")
    
    calc = EasyMath()
    
    try:
        discriminant = calc.eval("b^2 - 4*a*c", a=a, b=b, c=c)
        
        if discriminant < 0:
            return None, None  # No real solutions
        elif discriminant == 0:
            x = calc.eval("-b / (2*a)", a=a, b=b)
            return x, x  # One solution (repeated)
        else:
            sqrt_disc = math.sqrt(discriminant)
            x1 = calc.eval("(-b + d) / (2*a)", a=a, b=b, d=sqrt_disc)
            x2 = calc.eval("(-b - d) / (2*a)", a=a, b=b, d=sqrt_disc)
            return x1, x2
            
    except Exception as e:
        raise ValueError(f"Error solving quadratic equation: {str(e)}")


# Additional utility functions
def is_valid_expression(expression: str) -> bool:
    """
    Check if an expression is valid without evaluating it.
    
    Args:
        expression: Expression to validate
        
    Returns:
        True if expression can be parsed, False otherwise
    """
    if not expression or not expression.strip():
        return False
    
    # Check for obvious syntax errors
    expr = expression.strip()
    if expr.endswith(('+', '-', '*', '/', '^', '**')):
        return False
    
    # Check for unmatched parentheses
    if expr.count('(') != expr.count(')'):
        return False
    
    try:
        calc = EasyMath()
        calc._parse_expression(expression)
        return True
    except:
        return False


def get_expression_variables(expression: str) -> List[str]:
    """
    Get list of variables in an expression without evaluating it.
    
    Args:
        expression: Mathematical expression
        
    Returns:
        List of variable names
    """
    calc = EasyMath()
    parsed = calc._parse_expression(expression)
    return calc._extract_variables(parsed)