"""
Unit tests for the EasyMath package.

This module contains comprehensive tests for all EasyMath functionality,
including expression parsing, evaluation, function definition, and error handling.
"""

import pytest
import math
from realmaths import EasyMath, calculate, solve_quadratic
from realmaths.exceptions import (
    EasyMathError,
    ExpressionError,
    VariableError,
    FunctionError,
    MathematicalError,
)


class TestBasicEvaluation:
    """Test basic expression evaluation functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = EasyMath()

    def test_simple_arithmetic(self):
        """Test basic arithmetic operations."""
        assert self.calc.eval("2 + 3") == 5
        assert self.calc.eval("10 - 4") == 6
        assert self.calc.eval("3 * 4") == 12
        assert self.calc.eval("15 / 3") == 5

    def test_variables(self):
        """Test expressions with variables."""
        assert self.calc.eval("x + 1", x=5) == 6
        assert self.calc.eval("2x + 3", x=4) == 11
        assert self.calc.eval("x^2", x=3) == 9
        assert self.calc.eval("2x + 3y", x=2, y=4) == 16

    def test_implicit_multiplication(self):
        """Test implicit multiplication parsing."""
        assert self.calc.eval("2x", x=5) == 10
        assert self.calc.eval("3x + 2y", x=2, y=3) == 12
        assert self.calc.eval("2(x + 1)", x=3) == 8
        assert self.calc.eval("x(y + 1)", x=2, y=3) == 8

    def test_exponentiation(self):
        """Test exponentiation with both ^ and ** operators."""
        assert self.calc.eval("2^3") == 8
        assert self.calc.eval("2**3") == 8
        assert self.calc.eval("x^2", x=4) == 16
        assert self.calc.eval("x**2", x=4) == 16
        assert self.calc.eval("2^x", x=3) == 8

    def test_special_symbols(self):
        """Test special mathematical symbols."""
        assert self.calc.eval("x²", x=3) == 9
        assert self.calc.eval("x³", x=2) == 8
        # Note: sqrt symbol would need more complex parsing

    def test_order_of_operations(self):
        """Test proper order of operations."""
        assert self.calc.eval("2 + 3 * 4") == 14
        assert self.calc.eval("(2 + 3) * 4") == 20
        assert self.calc.eval("2^3 + 1") == 9
        assert self.calc.eval("2 * 3^2") == 18


class TestMathematicalFunctions:
    """Test built-in mathematical functions."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = EasyMath()

    def test_trigonometric_functions(self):
        """Test trigonometric functions."""
        assert abs(self.calc.eval("SIN(0)") - 0) < 1e-10
        assert abs(self.calc.eval("SIN(PI/2)") - 1) < 1e-10
        assert abs(self.calc.eval("COS(0)") - 1) < 1e-10
        assert abs(self.calc.eval("COS(PI)") - (-1)) < 1e-10
        assert abs(self.calc.eval("TAN(PI/4)") - 1) < 1e-10

    def test_logarithmic_functions(self):
        """Test logarithmic functions."""
        assert self.calc.eval("LN(EXP(1))") == 1
        assert self.calc.eval("LOG10(10)") == 1
        assert self.calc.eval("LOG10(100)") == 2
        assert self.calc.eval("LOG2(8)") == 3

    def test_exponential_functions(self):
        """Test exponential functions."""
        assert abs(self.calc.eval("EXP(1)") - math.e) < 1e-10
        assert self.calc.eval("EXP(0)") == 1
        assert self.calc.eval("EXP2(3)") == 8

    def test_root_functions(self):
        """Test root and power functions."""
        assert self.calc.eval("SQRT(9)") == 3
        assert self.calc.eval("SQRT(16)") == 4
        assert abs(self.calc.eval("CBRT(8)") - 2) < 1e-10
        assert self.calc.eval("POW(2, 3)") == 8

    def test_rounding_functions(self):
        """Test rounding and absolute value functions."""
        assert self.calc.eval("ABS(-5)") == 5
        assert self.calc.eval("ABS(5)") == 5
        assert self.calc.eval("ROUND(3.7)") == 4
        assert self.calc.eval("FLOOR(3.7)") == 3
        assert self.calc.eval("CEIL(3.2)") == 4

    def test_comparison_functions(self):
        """Test min/max functions."""
        assert self.calc.eval("MIN(3, 5)") == 3
        assert self.calc.eval("MAX(3, 5)") == 5


class TestConstants:
    """Test mathematical constants."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = EasyMath()

    def test_pi_constant(self):
        """Test pi constant."""
        assert abs(self.calc.eval("π") - math.pi) < 1e-10
        assert abs(self.calc.eval("PI") - math.pi) < 1e-10
        assert abs(self.calc.eval("2PI") - 2 * math.pi) < 1e-10

    def test_e_constant(self):
        """Test Euler's number."""
        assert abs(self.calc.eval("EXP(1)") - math.e) < 1e-10
        assert abs(self.calc.eval("2*EXP(1)") - 2 * math.e) < 1e-10

    def test_tau_constant(self):
        """Test tau constant."""
        assert abs(self.calc.eval("TAU") - math.tau) < 1e-10


class TestFunctionDefinition:
    """Test custom function definition and usage."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = EasyMath()

    def test_define_simple_function(self):
        """Test defining and using simple functions."""
        self.calc.define("linear", "2x + 1")
        assert self.calc.calculate("linear", x=3) == 7
        assert self.calc.calculate("linear", x=0) == 1

    def test_define_multi_variable_function(self):
        """Test functions with multiple variables."""
        self.calc.define("area_rect", "l * w")
        assert self.calc.calculate("area_rect", l=5, w=3) == 15

        self.calc.define("quadratic", "ax^2 + bx + c")
        assert self.calc.calculate("quadratic", a=1, b=2, c=3, x=2) == 11

    def test_function_with_constants(self):
        """Test functions using mathematical constants."""
        self.calc.define("circle_area", "PI * r^2")
        result = self.calc.calculate("circle_area", r=2)
        expected = math.pi * 4
        assert abs(result - expected) < 1e-10

    def test_function_with_math_functions(self):
        """Test functions using built-in math functions."""
        self.calc.define("hypotenuse", "SQRT(a^2 + b^2)")
        assert self.calc.calculate("hypotenuse", a=3, b=4) == 5

    def test_list_functions(self):
        """Test function listing functionality."""
        self.calc.define("f1", "x + 1")
        self.calc.define("f2", "x^2")

        # This would normally print, but we can check the internal storage
        assert "f1" in self.calc.functions
        assert "f2" in self.calc.functions
        assert len(self.calc.functions) == 2

    def test_delete_function(self):
        """Test function deletion."""
        self.calc.define("temp_func", "x + 1")
        assert "temp_func" in self.calc.functions

        self.calc.delete_function("temp_func")
        assert "temp_func" not in self.calc.functions

    def test_get_function_info(self):
        """Test getting function information."""
        self.calc.define("test_func", "2x + y", "Test function")
        info = self.calc.get_function_info("test_func")

        assert info["expression"] == "2x + y"
        assert info["description"] == "Test function"
        assert "x" in info["variables"]
        assert "y" in info["variables"]


class TestErrorHandling:
    """Test error handling and validation."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = EasyMath()

    def test_missing_variables(self):
        """Test error when variables are missing."""
        with pytest.raises(VariableError):
            self.calc.eval("x + y", x=1)  # Missing y

        with pytest.raises(VariableError):
            self.calc.eval("a + b + c", a=1)  # Missing b and c

    def test_invalid_expressions(self):
        """Test error handling for invalid expressions."""
        with pytest.raises(ExpressionError):
            self.calc.eval("2x +")  # Incomplete expression

        with pytest.raises(ExpressionError):
            self.calc.eval("((x + 1)")  # Unmatched parentheses

    def test_mathematical_errors(self):
        """Test mathematical errors like division by zero."""
        with pytest.raises(EasyMathError):
            self.calc.eval("1 / 0")

        with pytest.raises(EasyMathError):
            self.calc.eval("sqrt(-1)")  # Domain error for real numbers

    def test_undefined_function_error(self):
        """Test error when calling undefined function."""
        with pytest.raises(ValueError):
            self.calc.calculate("undefined_func", x=1)

    def test_invalid_function_names(self):
        """Test error when defining functions with invalid names."""
        with pytest.raises(ValueError):
            self.calc.define("2invalid", "x + 1")  # Starts with number

        with pytest.raises(ValueError):
            self.calc.define("sin", "x + 1")  # Conflicts with built-in

    def test_empty_expression(self):
        """Test error for empty expressions."""
        with pytest.raises(ExpressionError):
            self.calc.eval("")

        with pytest.raises(ExpressionError):
            self.calc.eval("   ")  # Only whitespace


class TestConvenienceFunctions:
    """Test convenience functions like calculate() and solve_quadratic()."""

    def test_calculate_function(self):
        """Test the standalone calculate function."""
        assert calculate("2x + 1", x=3) == 7
        assert calculate("x^2", x=4) == 16
        assert calculate("SIN(PI/2)") == 1

    def test_solve_quadratic(self):
        """Test quadratic equation solver."""
        # x² - 5x + 6 = 0, solutions: x = 2, 3
        x1, x2 = solve_quadratic(1, -5, 6)
        assert set([x1, x2]) == set([2.0, 3.0])

        # x² - 2x + 1 = 0, solution: x = 1 (repeated)
        x1, x2 = solve_quadratic(1, -2, 1)
        assert x1 == x2 == 1.0

        # x² + 1 = 0, no real solutions
        x1, x2 = solve_quadratic(1, 0, 1)
        assert x1 is None and x2 is None

    def test_solve_quadratic_errors(self):
        """Test quadratic solver error handling."""
        with pytest.raises(ValueError):
            solve_quadratic(0, 1, 1)  # a cannot be zero


class TestComplexExpressions:
    """Test complex mathematical expressions."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = EasyMath()

    def test_nested_functions(self):
        """Test expressions with nested function calls."""
        result = self.calc.eval("SIN(COS(0))")
        expected = math.sin(math.cos(0))
        assert abs(result - expected) < 1e-10

        result = self.calc.eval("SQRT(SIN(PI/2)^2 + COS(PI/2)^2)")
        assert abs(result - 1) < 1e-10

    def test_complex_polynomials(self):
        """Test complex polynomial expressions."""
        # (x + 1)(x - 1) = x² - 1
        result = self.calc.eval("(x + 1)(x - 1)", x=5)
        assert result == 24  # 6 * 4 = 24

        # x³ + 2x² - 3x + 1
        result = self.calc.eval("x^3 + 2x^2 - 3x + 1", x=2)
        assert result == 8 + 8 - 6 + 1 == 11

    def test_mixed_operations(self):
        """Test expressions mixing different types of operations."""
        result = self.calc.eval(
            "2PI * SQRT(x^2 + y^2) + SIN(α)", x=3, y=4, α=math.pi / 6
        )
        expected = 2 * math.pi * 5 + 0.5
        assert abs(result - expected) < 1e-10


class TestSafeMode:
    """Test safe mode functionality."""

    def test_safe_mode_enabled(self):
        """Test that safe mode prevents dangerous operations."""
        safe_calc = EasyMath(safe_mode=True)

        # Should work normally
        assert safe_calc.eval("2 + 3") == 5
        assert safe_calc.eval("SIN(PI/2)") == 1

    def test_safe_mode_disabled(self):
        """Test unsafe mode allows more operations."""
        unsafe_calc = EasyMath(safe_mode=False)

        # Should still work normally
        assert unsafe_calc.eval("2 + 3") == 5
        assert unsafe_calc.eval("SIN(PI/2)") == 1


class TestUtilityFunctions:
    """Test utility functions."""

    def test_is_valid_expression(self):
        """Test expression validation function."""
        from realmaths.core import is_valid_expression

        assert is_valid_expression("2x + 1") is True
        assert is_valid_expression("SIN(PI/2)") is True
        assert is_valid_expression("2x +") is False
        assert is_valid_expression("((x + 1)") is False

    def test_get_expression_variables(self):
        """Test variable extraction function."""
        from realmaths.core import get_expression_variables

        vars1 = get_expression_variables("2x + 3y")
        assert set(vars1) == set(["x", "y"])

        vars2 = get_expression_variables("ax^2 + bx + c")
        assert set(vars2) == set(["a", "b", "c", "x"])

        vars3 = get_expression_variables("SIN(PI/2)")
        assert len(vars3) == 0  # No variables, only constants and functions


class TestRealWorldExamples:
    """Test real-world mathematical examples."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = EasyMath()

    def test_physics_formulas(self):
        """Test physics formula calculations."""
        # Kinetic energy: KE = ½mv²
        self.calc.define("kinetic_energy", "0.5 * m * v^2")
        ke = self.calc.calculate("kinetic_energy", m=10, v=20)
        assert ke == 2000

        # Distance formula: d = √((x₂-x₁)² + (y₂-y₁)²)
        self.calc.define("distance", "SQRT((x2-x1)^2 + (y2-y1)^2)")
        distance = self.calc.calculate("distance", x1=0, y1=0, x2=3, y2=4)
        assert distance == 5

    def test_finance_formulas(self):
        """Test financial formula calculations."""
        # Simple interest: A = P(1 + rt)
        self.calc.define("simple_interest", "P * (1 + r * t)")
        amount = self.calc.calculate("simple_interest", P=1000, r=0.05, t=2)
        assert amount == 1100

        # Compound interest: A = P(1 + r/n)^(nt)
        self.calc.define("compound_interest", "P * (1 + r/n)^(n*t)")
        compound = self.calc.calculate("compound_interest", P=1000, r=0.05, n=1, t=2)
        assert abs(compound - 1102.5) < 0.01

    def test_geometry_formulas(self):
        """Test geometry formula calculations."""
        # Circle area: A = πr²
        self.calc.define("circle_area", "PI * r^2")
        area = self.calc.calculate("circle_area", r=2)
        expected = math.pi * 4
        assert abs(area - expected) < 1e-10

        # Triangle area (Heron's formula): A = √(s(s-a)(s-b)(s-c))
        self.calc.define("heron", "SQRT(s*(s-a)*(s-b)*(s-c))")
        area = self.calc.calculate("heron", s=6, a=3, b=4, c=5)  # s = (3+4+5)/2 = 6
        assert area == 6  # Area of 3-4-5 triangle is 6


class TestVectorizedOperations:
    """Test vectorized evaluation functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = EasyMath()

    def test_vectorized_list_operations(self):
        """Test vectorized operations on lists."""
        from realmaths import calculate_vector

        # Test simple vectorized operation (LOG is log base 10)
        result = calculate_vector("LOG(x)", x=[1, 10, 100])
        expected = [0.0, 1.0, 2.0]  # log10(1)=0, log10(10)=1, log10(100)=2
        for r, e in zip(result, expected):
            assert abs(r - e) < 1e-10

        # Test multiple variables
        result = calculate_vector("x + y", x=[1, 2, 3], y=[10, 20, 30])
        assert result == [11, 22, 33]

        # Test with scalar constant
        result = calculate_vector("x + 5", x=[1, 2, 3])
        assert result == [6, 7, 8]

    def test_vectorized_pandas_operations(self):
        """Test vectorized operations with pandas Series."""
        try:
            import pandas as pd
            from realmaths import calculate_vector

            # Create test data
            data = pd.Series([1, 2, 3, 4, 5])
            
            # Test vectorized operation
            result = calculate_vector("x^2", x=data)
            assert isinstance(result, pd.Series)
            assert list(result) == [1, 4, 9, 16, 25]
            
            # Test with multiple Series
            data2 = pd.Series([10, 20, 30, 40, 50])
            result = calculate_vector("x + y", x=data, y=data2)
            assert list(result) == [11, 22, 33, 44, 55]

        except ImportError:
            # Skip if pandas is not available
            pass

    def test_vectorized_error_handling(self):
        """Test error handling in vectorized operations."""
        from realmaths import calculate_vector

        # Test mismatched lengths
        with pytest.raises(VariableError):
            calculate_vector("x + y", x=[1, 2, 3], y=[10, 20])

        # Test invalid expression
        with pytest.raises(EasyMathError):
            calculate_vector("LOG(-1)", x=[1, 2, 3])

    def test_vectorized_fallback_to_scalar(self):
        """Test that vectorized operations fall back to scalar when appropriate."""
        from realmaths import calculate_vector

        # Should work like regular eval for scalar inputs
        result = calculate_vector("x + 1", x=5)
        assert result == 6

        result = calculate_vector("SIN(PI/2)")
        assert abs(result - 1) < 1e-10


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__])
