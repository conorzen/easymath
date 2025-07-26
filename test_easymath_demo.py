#!/usr/bin/env python3
"""
EasyMath Demo Script
Testing the new capitalization convention and fixed functionality
"""

from realmaths import EasyMath, calculate, solve_quadratic

def main():
    print("🧮 EasyMath Demo - New Capitalization Convention")
    print("=" * 50)
    
    # Create calculator instance
    calc = EasyMath()
    
    print("\n📊 1. BASIC ARITHMETIC")
    print("-" * 30)
    result = calc.eval("2x + 3", x=5)
    print(f"2x + 3 (x=5) = {result}")
    
    result = calc.eval("x^2 + 2x + 1", x=3)
    print(f"x² + 2x + 1 (x=3) = {result}")
    
    print("\n🔢 2. CONSTANTS (UPPERCASE)")
    print("-" * 30)
    result = calc.eval("2PI")
    print(f"2PI = {result}")
    
    result = calc.eval("PI * r^2", r=3)
    print(f"πr² (r=3) = {result}")
    
    print("\n📐 3. TRIGONOMETRIC FUNCTIONS (UPPERCASE)")
    print("-" * 30)
    result = calc.eval("SIN(PI/2)")
    print(f"SIN(π/2) = {result}")
    
    result = calc.eval("COS(PI)")
    print(f"COS(π) = {result}")
    
    result = calc.eval("TAN(PI/4)")
    print(f"TAN(π/4) = {result}")
    
    print("\n🔍 4. LOGARITHMIC & EXPONENTIAL (UPPERCASE)")
    print("-" * 30)
    result = calc.eval("LOG10(100)")
    print(f"LOG10(100) = {result}")
    
    result = calc.eval("EXP(1)")
    print(f"EXP(1) = {result}")
    
    print("\n📏 5. ROOT & POWER FUNCTIONS (UPPERCASE)")
    print("-" * 30)
    result = calc.eval("SQRT(16)")
    print(f"SQRT(16) = {result}")
    
    result = calc.eval("POW(2, 3)")
    print(f"POW(2, 3) = {result}")
    
    print("\n🔢 6. ROUNDING FUNCTIONS (UPPERCASE)")
    print("-" * 30)
    result = calc.eval("CEIL(3.2)")
    print(f"CEIL(3.2) = {result}")
    
    result = calc.eval("FLOOR(3.7)")
    print(f"FLOOR(3.7) = {result}")
    
    result = calc.eval("ROUND(3.5)")
    print(f"ROUND(3.5) = {result}")
    
    print("\n📊 7. VARIABLE MULTIPLICATION (lowercase)")
    print("-" * 30)
    result = calc.eval("ax^2 + bx + c", a=1, b=2, c=3, x=2)
    print(f"ax² + bx + c (a=1, b=2, c=3, x=2) = {result}")
    
    print("\n🏗️ 8. CUSTOM FUNCTION DEFINITION")
    print("-" * 30)
    calc.define("circle_area", "PI * r^2", "Area of a circle")
    result = calc.calculate("circle_area", r=5)
    print(f"Circle area (r=5) = {result}")
    
    calc.define("distance", "SQRT((x2-x1)^2 + (y2-y1)^2)", "Distance between two points")
    result = calc.calculate("distance", x1=0, y1=0, x2=3, y2=4)
    print(f"Distance (0,0) to (3,4) = {result}")
    
    print("\n🎯 9. QUADRATIC EQUATION SOLVER")
    print("-" * 30)
    x1, x2 = solve_quadratic(1, -5, 6)  # x² - 5x + 6 = 0
    print(f"x² - 5x + 6 = 0 → x₁ = {x1}, x₂ = {x2}")
    
    x1, x2 = solve_quadratic(1, -2, 1)  # x² - 2x + 1 = 0
    print(f"x² - 2x + 1 = 0 → x₁ = x₂ = {x1}")
    
    print("\n🔧 10. CONVENIENCE FUNCTION")
    print("-" * 30)
    result = calculate("SIN(PI/2)")
    print(f"calculate('SIN(PI/2)') = {result}")
    
    result = calculate("2x + 1", x=3)
    print(f"calculate('2x + 1', x=3) = {result}")
    
    print("\n📋 11. FUNCTION LISTING")
    print("-" * 30)
    calc.list_functions()
    
    print("\n✅ Demo completed successfully!")
    print("\n📝 Key Points:")
    print("• Functions and constants use UPPERCASE: SIN, COS, PI, SQRT")
    print("• Variables use lowercase: x, y, a, b, c")
    print("• No more function name splitting issues!")
    print("• Implicit multiplication works: ax → a*x")

if __name__ == "__main__":
    main() 