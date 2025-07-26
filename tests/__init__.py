"""
Test package for EasyMath.

This package contains all unit tests, integration tests, and test utilities
for the EasyMath mathematical expression package.

Test Structure:
- test_realmaths.py: Main test suite for core functionality
- test_examples.py: Tests for example calculations (future)
- test_cli.py: Tests for command-line interface (future)
- test_performance.py: Performance benchmarks (future)

Running Tests:
    pytest tests/                    # Run all tests
    pytest tests/test_realmaths.py    # Run specific test file
    pytest -v                       # Verbose output
    pytest --cov=realmaths           # With coverage report

Test Categories:
- Unit tests: Test individual functions in isolation
- Integration tests: Test component interactions
- Error handling tests: Verify proper error behavior
- Real-world tests: Test actual usage scenarios
"""

# Test configuration and utilities can be added here
import sys
import os

# Add the parent directory to Python path to allow importing realmaths
# This is useful when running tests without installing the package
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Test fixtures and utilities
def assert_close(actual, expected, tolerance=1e-10):
    """
    Helper function to assert that two floating point numbers are close.

    Args:
        actual: The calculated value
        expected: The expected value
        tolerance: Maximum difference allowed

    Raises:
        AssertionError: If values are not within tolerance
    """
    assert abs(actual - expected) < tolerance, f"Expected {expected}, got {actual}"


# Common test data
SAMPLE_EXPRESSIONS = [
    ("2 + 3", {}, 5),
    ("x + 1", {"x": 4}, 5),
    ("2x + 3", {"x": 2}, 7),
    ("x^2", {"x": 3}, 9),
    ("sqrt(16)", {}, 4),
    ("sin(π/2)", {}, 1),
    ("2π", {}, 2 * 3.141592653589793),
]

PHYSICS_FORMULAS = [
    ("kinetic_energy", "0.5 * m * v^2", ["m", "v"]),
    ("potential_energy", "m * g * h", ["m", "g", "h"]),
    ("wave_speed", "f * λ", ["f", "λ"]),
    ("force", "m * a", ["m", "a"]),
]

GEOMETRY_FORMULAS = [
    ("circle_area", "π * r^2", ["r"]),
    ("sphere_volume", "(4/3) * π * r^3", ["r"]),
    ("distance_2d", "sqrt((x2-x1)^2 + (y2-y1)^2)", ["x1", "y1", "x2", "y2"]),
]
