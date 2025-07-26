"""
Custom exceptions for the EasyMath package.

This module defines specific exception classes to provide clear,
user-friendly error messages for different types of mathematical
and expression-related errors.
"""

import re


class EasyMathError(Exception):
    """
    Base exception class for all EasyMath-related errors.
    
    This serves as the parent class for all custom exceptions
    in the EasyMath package, allowing users to catch all
    EasyMath-specific errors with a single except clause.
    """
    
    def __init__(self, message: str, suggestion: str = ""):
        """
        Initialize EasyMathError.
        
        Args:
            message: Error description
            suggestion: Optional helpful suggestion for the user
        """
        self.message = message
        self.suggestion = suggestion
        
        full_message = message
        if suggestion:
            full_message += f"\n💡 Suggestion: {suggestion}"
            
        super().__init__(full_message)
    
    def __str__(self):
        return self.message


class ExpressionError(EasyMathError):
    """
    Raised when there's an error parsing or evaluating a mathematical expression.
    
    This includes syntax errors, invalid mathematical operations,
    and other expression-related problems.
    
    Examples of when this is raised:
    - Invalid syntax: "2x +"
    - Unknown functions: "invalidfunc(x)"
    - Malformed expressions: "((x+1)"
    """
    
    def __init__(self, message: str, expression: str = "", suggestion: str = ""):
        """
        Initialize ExpressionError.
        
        Args:
            message: Error description
            expression: The problematic expression (if available)
            suggestion: Helpful suggestion for fixing the expression
        """
        self.expression = expression
        
        if expression:
            full_message = f"Expression error in '{expression}': {message}"
        else:
            full_message = f"Expression error: {message}"
        
        # Provide helpful suggestions based on common errors
        if not suggestion:
            suggestion = self._get_suggestion(message, expression)
        
        super().__init__(full_message, suggestion)
    
    def _get_suggestion(self, message: str, expression: str) -> str:
        """Generate helpful suggestions based on the error and expression."""
        suggestions = []
        
        # Common syntax issues
        if "invalid syntax" in message.lower():
            suggestions.append("Check for missing operators or parentheses")
        
        if "unexpected" in message.lower():
            suggestions.append("Verify all parentheses are properly matched")
        
        # Mathematical issues
        if expression:
            if "^" in expression and "**" not in expression:
                suggestions.append("Use '^' for exponents (e.g., 'x^2' for x squared)")
            
            if any(char in expression for char in "()[]{}"):
                suggestions.append("Make sure all parentheses and brackets are balanced")
            
            # Check for implicit multiplication issues
            if re.search(r'\d[a-zA-Z]', expression.replace(' ', '')):
                suggestions.append("Implicit multiplication is supported (e.g., '2x' means '2*x')")
        
        return "; ".join(suggestions) if suggestions else "Double-check the mathematical expression syntax"


class VariableError(EasyMathError):
    """
    Raised when there are issues with variables in expressions.
    
    This includes missing variables, undefined variables,
    or type-related variable problems.
    
    Examples of when this is raised:
    - Missing variables: eval("x + y", x=1) - missing y
    - Wrong variable names: provided 'a' but expression uses 'alpha'
    """
    
    def __init__(self, message: str, missing_vars: list = None, 
                 provided_vars: list = None, suggestion: str = ""):
        """
        Initialize VariableError.
        
        Args:
            message: Error description
            missing_vars: List of missing variable names
            provided_vars: List of provided variable names
            suggestion: Helpful suggestion for the user
        """
        self.missing_vars = missing_vars or []
        self.provided_vars = provided_vars or []
        
        # Generate helpful suggestion if not provided
        if not suggestion:
            suggestion = self._get_suggestion()
        
        super().__init__(message, suggestion)
    
    def _get_suggestion(self) -> str:
        """Generate helpful suggestion based on missing/provided variables."""
        if self.missing_vars:
            if len(self.missing_vars) == 1:
                return f"Add the missing variable: {self.missing_vars[0]}=value"
            else:
                vars_str = ", ".join(f"{var}=value" for var in self.missing_vars)
                return f"Add the missing variables: {vars_str}"
        
        return "Check that all variable names match those used in the expression"


class FunctionError(EasyMathError):
    """
    Raised when there are issues with function definition or usage.
    
    This includes errors in defining custom functions, calling
    non-existent functions, or function-related problems.
    
    Examples of when this is raised:
    - Calling undefined function: calculate("my_func", x=1)
    - Invalid function name: define("2invalid", "x+1")
    - Function redefinition: trying to redefine built-in functions
    """
    
    def __init__(self, message: str, function_name: str = "", suggestion: str = ""):
        """
        Initialize FunctionError.
        
        Args:
            message: Error description
            function_name: Name of the problematic function
            suggestion: Helpful suggestion for the user
        """
        self.function_name = function_name
        
        if function_name:
            full_message = f"Function error with '{function_name}': {message}"
        else:
            full_message = f"Function error: {message}"
        
        if not suggestion:
            suggestion = self._get_suggestion(message, function_name)
        
        super().__init__(full_message, suggestion)
    
    def _get_suggestion(self, message: str, function_name: str) -> str:
        """Generate helpful suggestion based on the function error."""
        if "not defined" in message.lower():
            return f"Use calc.define('{function_name}', 'expression') to define it first"
        
        if "invalid" in message.lower() and "name" in message.lower():
            return "Function names must be valid Python identifiers (letters, numbers, underscores)"
        
        if "redefine" in message.lower():
            return "Choose a different name that doesn't conflict with built-in functions"
        
        return "Check the function name and definition"


class MathematicalError(EasyMathError):
    """
    Raised when there are mathematical errors during calculation.
    
    This includes domain errors, range errors, and other mathematical
    issues that occur during expression evaluation.
    
    Examples of when this is raised:
    - Division by zero: "1/0"
    - Invalid domain: "sqrt(-1)" (for real numbers)
    - Overflow: very large exponentials
    """
    
    def __init__(self, message: str, operation: str = "", suggestion: str = ""):
        """
        Initialize MathematicalError.
        
        Args:
            message: Error description
            operation: The mathematical operation that caused the error
            suggestion: Helpful suggestion for the user
        """
        self.operation = operation
        
        if operation:
            full_message = f"Mathematical error in '{operation}': {message}"
        else:
            full_message = f"Mathematical error: {message}"
        
        if not suggestion:
            suggestion = self._get_suggestion(message, operation)
        
        super().__init__(full_message, suggestion)
    
    def _get_suggestion(self, message: str, operation: str) -> str:
        """Generate helpful suggestion based on the mathematical error."""
        if "division by zero" in message.lower():
            return "Check that denominators are not zero"
        
        if "domain" in message.lower() or "negative" in message.lower():
            return "Check that function inputs are within valid domains (e.g., sqrt needs non-negative numbers)"
        
        if "overflow" in message.lower():
            return "Try using smaller numbers or different mathematical approaches"
        
        if "invalid" in message.lower():
            return "Verify that all mathematical operations are valid for the given inputs"
        
        return "Check the mathematical validity of the expression and input values"


# Convenience function for handling multiple exception types
def handle_easymath_error(func):
    """
    Decorator to provide consistent error handling for EasyMath functions.
    
    This decorator catches various types of exceptions and converts them
    to appropriate EasyMath exception types with helpful messages.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except EasyMathError:
            # Re-raise EasyMath errors as-is
            raise
        except SyntaxError as e:
            raise ExpressionError(f"Invalid syntax: {str(e)}")
        except NameError as e:
            var_name = str(e).split("'")[1] if "'" in str(e) else "unknown"
            raise VariableError(f"Undefined variable: {var_name}")
        except ZeroDivisionError:
            raise MathematicalError("Division by zero")
        except ValueError as e:
            raise MathematicalError(str(e))
        except TypeError as e:
            raise ExpressionError(f"Type error: {str(e)}")
        except Exception as e:
            raise EasyMathError(f"Unexpected error: {str(e)}")
    
    return wrapper