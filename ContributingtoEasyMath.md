# Contributing to EasyMath

Thank you for your interest in contributing to EasyMath! This project aims to make mathematics accessible to everyone, regardless of their programming background.

## 🎯 Project Goals

- **Accessibility**: Make mathematical calculations easy for non-programmers
- **Natural syntax**: Support intuitive mathematical notation
- **Educational value**: Useful for students, teachers, and researchers
- **Reliability**: Robust error handling and clear error messages
- **Extensibility**: Easy to add new mathematical functions and features

## 🚀 Getting Started

### Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/conorzen/easymath.git
   cd easymath
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install in development mode**
   ```bash
   pip install -e .
   pip install -r requirements-dev.txt
   ```

4. **Run tests to verify setup**
   ```bash
   pytest tests/
   ```

### Project Structure

```
easymath/
├── easymath/           # Main package
│   ├── __init__.py    # Package initialization
│   ├── core.py        # Core EasyMath functionality
│   ├── exceptions.py  # Custom exception classes
│   ├── examples.py    # Example calculations
│   └── cli.py         # Command-line interface
├── tests/             # Test suite
│   ├── __init__.py
│   └── test_easymath.py
├── docs/              # Documentation
├── setup.py           # Package configuration
├── README.md          # Project documentation
└── requirements*.txt  # Dependencies
```

## 🔧 Development Guidelines

### Code Style

- **Follow PEP 8**: Use standard Python style guidelines
- **Type hints**: Add type hints for function parameters and return values
- **Docstrings**: Use Google-style docstrings for all public functions
- **Comments**: Write clear, helpful comments for complex logic

Example function:
```python
def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle.
    
    Args:
        radius: The radius of the circle
        
    Returns:
        The area of the circle
        
    Raises:
        ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2
```

### Testing

- **Write tests**: All new features must include comprehensive tests
- **Test coverage**: Aim for >90% test coverage
- **Test naming**: Use descriptive test names that explain what's being tested
- **Edge cases**: Include tests for edge cases and error conditions

Example test:
```python
def test_area_calculation_positive_radius():
    """Test area calculation with positive radius."""
    calc = EasyMath()
    calc.define("circle_area", "π * r^2")
    result = calc.calculate("circle_area", r=3)
    expected = math.pi * 9
    assert abs(result - expected) < 1e-10

def test_area_calculation_zero_radius():
    """Test area calculation with zero radius."""
    calc = EasyMath()
    calc.define("circle_area", "π * r^2")
    result = calc.calculate("circle_area", r=0)
    assert result == 0
```

### Error Handling

- **Custom exceptions**: Use EasyMath's custom exception classes
- **Helpful messages**: Provide clear, actionable error messages
- **User-friendly**: Remember that users may not be programmers

Example error handling:
```python
try:
    result = self.eval(expression, **variables)
except SyntaxError:
    raise ExpressionError(
        f"Invalid syntax in expression: {expression}",
        suggestion="Check for missing operators or unmatched parentheses"
    )
```

## 📝 Types of Contributions

### 🐛 Bug Reports

When reporting bugs, please include:

- **Clear description**: What you expected vs. what happened
- **Steps to reproduce**: Minimal code example that demonstrates the bug
- **Environment**: Python version, EasyMath version, operating system
- **Error messages**: Full error traceback if applicable

Use this template:
```markdown
**Bug Description**
A clear description of what the bug is.

**To Reproduce**
```python
from easymath import EasyMath
calc = EasyMath()
# Your code here
```

**Expected Behavior**
What you expected to happen.

**Actual Behavior**
What actually happened, including any error messages.

**Environment**
- Python version: 
- EasyMath version:
- Operating System:
```

### ✨ Feature Requests

For new features, please include:

- **Use case**: Why is this feature needed?
- **Description**: What should the feature do?
- **Examples**: How would users interact with this feature?
- **Implementation ideas**: Any thoughts on how it could be implemented

### 📚 Documentation Improvements

- Fix typos or unclear explanations
- Add more examples
- Improve API documentation
- Translate documentation (if interested)

### 🔧 Code Contributions

#### New Mathematical Functions

When adding new mathematical functions:

1. **Add to `math_functions` dictionary** in `core.py`
2. **Write comprehensive tests** in `test_easymath.py`
3. **Update documentation** in docstrings and README
4. **Add examples** in `examples.py`

Example:
```python
# In core.py
self.math_functions = {
    # ... existing functions ...
    'factorial': math.factorial,
    'gcd': math.gcd,
}

# In test_easymath.py
def test_factorial_function(self):
    """Test factorial function."""
    assert self.calc.eval("factorial(5)") == 120
    assert self.calc.eval("factorial(0)") == 1
```

#### Expression Parsing Improvements

When improving expression parsing:

1. **Understand the parsing pipeline** in `_parse_expression()`
2. **Add regex patterns carefully** - test edge cases
3. **Maintain backward compatibility**
4. **Test extensively** with various expression types

#### New Features

For larger features:

1. **Discuss first**: Open an issue to discuss the feature
2. **Plan the API**: How will users interact with it?
3. **Write tests first**: Test-driven development
4. **Implement incrementally**: Break into smaller commits
5. **Update documentation**: README, docstrings, examples

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=easymath

# Run specific test file
pytest tests/test_easymath.py

# Run specific test
pytest tests/test_easymath.py::TestBasicEvaluation::test_simple_arithmetic
```

### Test Categories

- **Unit tests**: Test individual functions in isolation
- **Integration tests**: Test how components work together
- **Error handling tests**: Test that errors are handled properly
- **Real-world tests**: Test actual use cases and examples

### Test Data

Create test data that covers:
- **Common cases**: Typical user inputs
- **Edge cases**: Empty inputs, very large numbers, etc.
- **Error cases**: Invalid syntax, missing variables, etc.
- **Mathematical accuracy**: Verify calculations are correct

## 📖 Documentation

### Docstring Style

Use Google-style docstrings:

```python
def example_function(param1: int, param2: str = "default") -> bool:
    """
    One-line summary of what the function does.
    
    Longer description if needed. Explain the purpose, behavior,
    and any important details.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter with default value
        
    Returns:
        Description of what the function returns
        
    Raises:
        ValueError: When param1 is negative
        TypeError: When param2 is not a string
        
    Examples:
        Basic usage:
        >>> result = example_function(5, "test")
        >>> print(result)
        True
        
        With default parameter:
        >>> result = example_function(10)
        >>> print(result)
        True
    """
```

### README Updates

When updating the README:
- Keep examples simple and clear
- Focus on user benefits, not technical details
- Test all code examples to ensure they work
- Maintain consistent formatting

## 🔄 Pull Request Process

### Before Submitting

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the coding guidelines
   - Add tests for new functionality
   - Update documentation as needed

3. **Test thoroughly**
   ```bash
   pytest tests/
   python -m easymath.examples  # Test examples still work
   ```

4. **Update CHANGELOG.md** with your changes

5. **Commit with clear messages**
   ```bash
   git commit -m "Add support for hyperbolic functions
   
   - Add sinh, cosh, tanh to math_functions
   - Include comprehensive tests
   - Update examples and documentation"
   ```

### Pull Request Template

```markdown
## Description
Brief description of the changes and why they're needed.

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## How Has This Been Tested?
Describe the tests you ran and how to reproduce them.

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
```

### Review Process

1. **Automated checks**: Tests and linting must pass
2. **Code review**: Maintainers will review your code
3. **Feedback incorporation**: Address any requested changes
4. **Approval and merge**: Once approved, changes will be merged

## 🏷️ Versioning

EasyMath follows [Semantic Versioning](https://semver.org/):

- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality in a backwards compatible manner
- **PATCH**: Backwards compatible bug fixes

## 🤝 Community Guidelines

### Be Respectful

- **Inclusive language**: Use welcoming and inclusive language
- **Constructive feedback**: Focus on the code, not the person
- **Patient teaching**: Remember that contributors have different experience levels

### Communication

- **Clear and concise**: Explain your ideas clearly
- **Ask questions**: Don't hesitate to ask for clarification
- **Share knowledge**: Help others learn and grow

### Recognition

All contributors will be acknowledged in:
- **CONTRIBUTORS.md**: List of all contributors
- **Release notes**: Major contributions highlighted
- **README**: Special thanks section

## 📞 Getting Help

If you need help:

- **Open an issue**: For bugs, feature requests, or questions
- **Discussions**: For general questions about usage or contribution
- **Email**: For private inquiries (your.email@example.com)

## 🎉 First Time Contributors

New to open source? Here are some good first issues:

- **Documentation**: Fix typos, improve examples
- **Tests**: Add tests for existing functionality
- **Examples**: Add new real-world examples
- **Error messages**: Improve error message clarity

Look for issues labeled `good-first-issue` or `help-wanted`.

## 📋 Development Workflow Summary

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Document** your changes
6. **Submit** a pull request
7. **Respond** to feedback
8. **Celebrate** when merged! 🎉

Thank you for contributing to EasyMath and helping make mathematics more accessible to everyone! 🧮✨