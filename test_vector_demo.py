#!/usr/bin/env python3
"""
Vectorized RealMaths Demo

This script demonstrates the new vectorized evaluation capabilities
of the realmaths package, showing how to apply mathematical expressions
to lists and pandas Series.
"""

from realmaths import EasyMath, calculate_vector

def demo_list_operations():
    """Demonstrate vectorized operations on lists."""
    print("📊 Vectorized Operations on Lists")
    print("=" * 50)
    
    # Example 1: Logarithm of a list
    days = [1, 2, 3, 4, 5, 10, 20, 50, 100]
    log_days = calculate_vector("LOG(x)", x=days)
    print(f"Days: {days}")
    print(f"Log of days: {[round(x, 4) for x in log_days]}")
    print()
    
    # Example 2: Square and add constant
    numbers = [1, 2, 3, 4, 5]
    squared_plus_one = calculate_vector("x^2 + 1", x=numbers)
    print(f"Numbers: {numbers}")
    print(f"x² + 1: {squared_plus_one}")
    print()
    
    # Example 3: Multiple variables
    x_values = [1, 2, 3, 4]
    y_values = [10, 20, 30, 40]
    result = calculate_vector("x * y + 5", x=x_values, y=y_values)
    print(f"x: {x_values}")
    print(f"y: {y_values}")
    print(f"x * y + 5: {result}")
    print()

def demo_pandas_operations():
    """Demonstrate vectorized operations with pandas (if available)."""
    print("🐼 Vectorized Operations with Pandas")
    print("=" * 50)
    
    try:
        import pandas as pd
        
        # Create sample data
        data = {
            'sum_paid_days': [1, 2, 3, 4, 5, 10, 20, 50, 100],
            'amount': [100, 200, 300, 400, 500, 1000, 2000, 5000, 10000]
        }
        df = pd.DataFrame(data)
        
        print("Original DataFrame:")
        print(df)
        print()
        
        # Example 1: Log of days (your original use case)
        df['log_of_days'] = calculate_vector("LOG(x)", x=df['sum_paid_days'])
        print("After adding log_of_days:")
        print(df[['sum_paid_days', 'log_of_days']])
        print()
        
        # Example 2: Square root of amount
        df['sqrt_amount'] = calculate_vector("SQRT(x)", x=df['amount'])
        print("After adding sqrt_amount:")
        print(df[['amount', 'sqrt_amount']])
        print()
        
        # Example 3: Complex calculation
        df['ratio'] = calculate_vector("LOG(x) / SQRT(y)", x=df['sum_paid_days'], y=df['amount'])
        print("After adding ratio (log(days) / sqrt(amount)):")
        print(df[['sum_paid_days', 'amount', 'ratio']])
        print()
        
    except ImportError:
        print("Pandas not available. Install with: pip install pandas")
        print()

def demo_mixed_operations():
    """Demonstrate mixing scalar and vector variables."""
    print("🔀 Mixed Scalar and Vector Operations")
    print("=" * 50)
    
    # Vector with scalar constant
    values = [1, 2, 3, 4, 5]
    result = calculate_vector("x + 10", x=values)  # 10 is broadcast to all elements
    print(f"Values: {values}")
    print(f"x + 10: {result}")
    print()
    
    # Multiple vectors with different operations
    x_vals = [1, 2, 3]
    y_vals = [10, 20, 30]
    result = calculate_vector("x^2 + y + 5", x=x_vals, y=y_vals)
    print(f"x: {x_vals}")
    print(f"y: {y_vals}")
    print(f"x² + y + 5: {result}")
    print()

def demo_error_handling():
    """Demonstrate error handling in vectorized operations."""
    print("⚠️  Error Handling")
    print("=" * 50)
    
    try:
        # Mismatched lengths
        result = calculate_vector("x + y", x=[1, 2, 3], y=[10, 20])
        print("This should not print")
    except Exception as e:
        print(f"Expected error: {e}")
    
    try:
        # Invalid expression
        result = calculate_vector("LOG(-1)", x=[1, 2, 3])
        print("This should not print")
    except Exception as e:
        print(f"Expected error: {e}")
    
    print()

def main():
    """Run all demonstrations."""
    print("🧮 RealMaths Vectorized Operations Demo")
    print("=" * 60)
    print()
    
    demo_list_operations()
    demo_pandas_operations()
    demo_mixed_operations()
    demo_error_handling()
    
    print("✅ Demo completed!")
    print("\nUsage examples:")
    print("  from realmaths import calculate_vector")
    print("  result = calculate_vector('LOG(x)', x=[1, 10, 100])")
    print("  df['new_col'] = calculate_vector('x^2 + 1', x=df['old_col'])")

if __name__ == "__main__":
    main() 