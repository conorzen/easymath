"""
Examples and demonstrations for the EasyMath package.

This module contains comprehensive examples showing how to use EasyMath
for various mathematical calculations across different domains like
physics, finance, geometry, and education.
"""

from realmaths.core import EasyMath, calculate, solve_quadratic


def basic_examples():
    """Demonstrate basic EasyMath functionality."""
    print("🔢 Basic EasyMath Examples")
    print("=" * 50)

    calc = EasyMath()

    # Simple expressions
    print("1. Simple Expressions:")
    examples = [
        ("4n + 1", {"n": 5}),
        ("2x + 3y", {"x": 4, "y": 2}),
        ("x^2 + 2x + 1", {"x": 3}),
        ("sqrt(a^2 + b^2)", {"a": 3, "b": 4}),
        ("sin(π/2)", {}),
        ("log10(1000)", {}),
    ]

    for expr, vars_dict in examples:
        result = calc.eval(expr, **vars_dict)
        vars_str = (
            ", ".join(f"{k}={v}" for k, v in vars_dict.items())
            if vars_dict
            else "no variables"
        )
        print(f"   {expr} where {vars_str}: {result}")

    print()

    # Quick calculations using the convenience function
    print("2. Quick Calculations (using calculate function):")
    quick_examples = [
        ("3x^2 + 2x - 1", {"x": 2}),
        ("π * r^2", {"r": 5}),
        ("e^x", {"x": 1}),
    ]

    for expr, vars_dict in quick_examples:
        result = calculate(expr, **vars_dict)
        vars_str = ", ".join(f"{k}={v}" for k, v in vars_dict.items())
        print(f"   calculate('{expr}', {vars_str}) = {result}")

    print("\n")


def physics_examples():
    """Physics calculations made easy."""
    print("⚛️  Physics Examples")
    print("=" * 50)

    calc = EasyMath()

    # Define physics formulas
    physics_formulas = [
        ("kinetic_energy", "0.5 * m * v^2", "Kinetic energy (KE = ½mv²)"),
        ("potential_energy", "m * g * h", "Gravitational potential energy"),
        ("force", "m * a", "Newton's second law (F = ma)"),
        ("wave_speed", "f * λ", "Wave speed (v = fλ)"),
        ("ohms_law_power", "V * I", "Electrical power (P = VI)"),
        ("centripetal_force", "m * v^2 / r", "Centripetal force"),
        ("elastic_potential", "0.5 * k * x^2", "Elastic potential energy"),
        ("momentum", "m * v", "Linear momentum (p = mv)"),
    ]

    print("Defining physics formulas:")
    for name, formula, description in physics_formulas:
        calc.define(name, formula, description)

    print("\nExample calculations:")

    # Kinetic energy
    energy = calc.calculate("kinetic_energy", m=10, v=25)
    print(f"Kinetic energy (m=10kg, v=25m/s): {energy} J")

    # Potential energy
    pe = calc.calculate("potential_energy", m=5, g=9.81, h=20)
    print(f"Potential energy (m=5kg, h=20m): {pe:.1f} J")

    # Wave speed
    speed = calc.calculate("wave_speed", f=440, λ=0.77)
    print(f"Sound wave speed (440 Hz): {speed:.1f} m/s")

    # Force calculation
    force = calc.calculate("force", m=2, a=9.81)
    print(f"Force on 2kg object (gravity): {force:.1f} N")

    print("\n")


def finance_examples():
    """Financial calculations."""
    print("💰 Finance Examples")
    print("=" * 50)

    calc = EasyMath()

    # Financial formulas
    calc.define(
        "compound_interest",
        "P * (1 + r/n)^(n*t)",
        "Compound interest: P=principal, r=annual rate, n=compounds per year, t=years",
    )
    calc.define(
        "simple_interest",
        "P * (1 + r*t)",
        "Simple interest: P=principal, r=annual rate, t=years",
    )
    calc.define(
        "monthly_payment",
        "P * (r*(1+r)^n) / ((1+r)^n - 1)",
        "Monthly loan payment: P=principal, r=monthly rate, n=total payments",
    )
    calc.define(
        "future_value_annuity",
        "PMT * (((1+r)^n - 1) / r)",
        "Future value of ordinary annuity",
    )
    calc.define("present_value", "FV / (1+r)^n", "Present value calculation")

    print("Example calculations:")

    # Compound interest
    amount = calc.calculate("compound_interest", P=1000, r=0.05, n=12, t=5)
    print(f"$1000 at 5% compounded monthly for 5 years: ${amount:.2f}")

    # Simple interest
    simple = calc.calculate("simple_interest", P=1000, r=0.05, t=5)
    print(f"$1000 at 5% simple interest for 5 years: ${simple:.2f}")

    # Monthly payment (approximation for demonstration)
    # For a $200,000 loan at 4% annual rate for 30 years
    principal = 200000
    annual_rate = 0.04
    monthly_rate = annual_rate / 12
    total_payments = 30 * 12
    payment = calc.calculate(
        "monthly_payment", P=principal, r=monthly_rate, n=total_payments
    )
    print(f"Monthly payment on $200k loan (4%, 30 years): ${payment:.2f}")

    # Present value
    pv = calc.calculate("present_value", FV=1000, r=0.05, n=10)
    print(f"Present value of $1000 in 10 years at 5%: ${pv:.2f}")

    print("\n")


def geometry_examples():
    """Geometry calculations."""
    print("📐 Geometry Examples")
    print("=" * 50)

    calc = EasyMath()

    # Geometry formulas
    geometry_formulas = [
        ("circle_area", "π * r^2", "Area of a circle"),
        ("circle_circumference", "2 * π * r", "Circumference of a circle"),
        ("sphere_volume", "(4/3) * π * r^3", "Volume of a sphere"),
        ("sphere_surface", "4 * π * r^2", "Surface area of a sphere"),
        ("triangle_area", "0.5 * base * height", "Area of a triangle"),
        (
            "triangle_area_heron",
            "sqrt(s*(s-a)*(s-b)*(s-c))",
            "Heron's formula (s=semi-perimeter)",
        ),
        ("rectangle_area", "length * width", "Area of a rectangle"),
        ("cylinder_volume", "π * r^2 * h", "Volume of a cylinder"),
        ("cone_volume", "(1/3) * π * r^2 * h", "Volume of a cone"),
        ("distance_2d", "sqrt((x2-x1)^2 + (y2-y1)^2)", "Distance between two points"),
        ("distance_3d", "sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)", "3D distance"),
    ]

    print("Defining geometry formulas:")
    for name, formula, description in geometry_formulas:
        calc.define(name, formula, description)

    print("\nExample calculations:")

    # Circle calculations
    r = 5
    area = calc.calculate("circle_area", r=r)
    circumference = calc.calculate("circle_circumference", r=r)
    print(f"Circle (r={r}): Area = {area:.2f}, Circumference = {circumference:.2f}")

    # Sphere calculations
    volume = calc.calculate("sphere_volume", r=r)
    surface = calc.calculate("sphere_surface", r=r)
    print(f"Sphere (r={r}): Volume = {volume:.2f}, Surface = {surface:.2f}")

    # Triangle using Heron's formula
    a, b, c = 3, 4, 5
    s = (a + b + c) / 2  # semi-perimeter
    triangle_area = calc.calculate("triangle_area_heron", s=s, a=a, b=b, c=c)
    print(f"Triangle (sides {a},{b},{c}): Area = {triangle_area:.2f}")

    # Distance calculations
    dist_2d = calc.calculate("distance_2d", x1=0, y1=0, x2=3, y2=4)
    dist_3d = calc.calculate("distance_3d", x1=0, y1=0, z1=0, x2=1, y2=2, z2=2)
    print(f"2D distance (0,0) to (3,4): {dist_2d}")
    print(f"3D distance (0,0,0) to (1,2,2): {dist_3d:.2f}")

    print("\n")


def statistics_examples():
    """Basic statistics calculations."""
    print("📊 Statistics Examples")
    print("=" * 50)

    calc = EasyMath()

    # Statistics formulas
    calc.define("mean", "sum_values / n", "Arithmetic mean")
    calc.define(
        "variance_population", "sum_squared_deviations / n", "Population variance"
    )
    calc.define("variance_sample", "sum_squared_deviations / (n-1)", "Sample variance")
    calc.define("std_dev", "sqrt(variance)", "Standard deviation")
    calc.define("z_score", "(x - μ) / σ", "Z-score calculation")
    calc.define(
        "coefficient_variation", "(σ / μ) * 100", "Coefficient of variation (%)"
    )

    # Example dataset
    data = [2, 4, 6, 8, 10, 12, 14]
    n = len(data)

    print(f"Dataset: {data}")
    print(f"Sample size: {n}")

    # Calculate mean
    sum_values = sum(data)
    mean = calc.calculate("mean", sum_values=sum_values, n=n)
    print(f"Mean: {mean:.2f}")

    # Calculate variance and standard deviation
    sum_squared_deviations = sum((x - mean) ** 2 for x in data)
    variance_pop = calc.calculate(
        "variance_population", sum_squared_deviations=sum_squared_deviations, n=n
    )
    variance_samp = calc.calculate(
        "variance_sample", sum_squared_deviations=sum_squared_deviations, n=n
    )

    std_dev_pop = calc.calculate("std_dev", variance=variance_pop)
    std_dev_samp = calc.calculate("std_dev", variance=variance_samp)

    print(f"Population variance: {variance_pop:.2f}")
    print(f"Sample variance: {variance_samp:.2f}")
    print(f"Population std dev: {std_dev_pop:.2f}")
    print(f"Sample std dev: {std_dev_samp:.2f}")

    # Z-score for a value
    x = 10
    z = calc.calculate("z_score", x=x, μ=mean, σ=std_dev_pop)
    print(f"Z-score for {x}: {z:.2f}")

    print("\n")


def education_examples():
    """Educational examples for students."""
    print("🎓 Educational Examples")
    print("=" * 50)

    calc = EasyMath()

    print("1. Quadratic Equations:")
    # Quadratic formula examples
    quadratics = [
        (1, -5, 6),  # x² - 5x + 6 = 0
        (1, -2, 1),  # x² - 2x + 1 = 0 (perfect square)
        (1, 0, -4),  # x² - 4 = 0
        (2, 3, -2),  # 2x² + 3x - 2 = 0
    ]

    for a, b, c in quadratics:
        x1, x2 = solve_quadratic(a, b, c)
        equation = f"{a}x² + {b}x + {c} = 0" if b >= 0 else f"{a}x² {b}x + {c} = 0"
        if x1 is None:
            print(f"   {equation}: No real solutions")
        elif x1 == x2:
            print(f"   {equation}: x = {x1}")
        else:
            print(f"   {equation}: x = {x1}, x = {x2}")

    print("\n2. Trigonometry:")
    # Common trig values
    trig_examples = [
        ("sin(0)", {}),
        ("sin(π/6)", {}),  # 30 degrees
        ("sin(π/4)", {}),  # 45 degrees
        ("sin(π/3)", {}),  # 60 degrees
        ("sin(π/2)", {}),  # 90 degrees
        ("cos(0)", {}),
        ("cos(π/4)", {}),
        ("tan(π/4)", {}),
    ]

    for expr, vars_dict in trig_examples:
        result = calc.eval(expr, **vars_dict)
        print(f"   {expr} = {result:.4f}")

    print("\n3. Exponentials and Logarithms:")
    exp_log_examples = [
        ("e^0", {}),
        ("e^1", {}),
        ("e^2", {}),
        ("ln(1)", {}),
        ("ln(e)", {}),
        ("log10(1)", {}),
        ("log10(10)", {}),
        ("log10(100)", {}),
        ("2^3", {}),
        ("2^10", {}),
    ]

    for expr, vars_dict in exp_log_examples:
        result = calc.eval(expr, **vars_dict)
        print(f"   {expr} = {result}")

    print("\n")


def advanced_examples():
    """Advanced mathematical examples."""
    print("🧮 Advanced Examples")
    print("=" * 50)

    calc = EasyMath()

    # Complex formulas
    advanced_formulas = [
        (
            "normal_distribution",
            "(1/sqrt(2*π*σ^2)) * e^(-0.5*((x-μ)/σ)^2)",
            "Normal distribution PDF",
        ),
        (
            "compound_annual_growth",
            "((FV/PV)^(1/n)) - 1",
            "Compound Annual Growth Rate",
        ),
        (
            "black_scholes_call",
            "S*N_d1 - K*e^(-r*T)*N_d2",
            "Black-Scholes call option (simplified)",
        ),
        (
            "loan_remaining",
            "P * ((1+r)^n - (1+r)^p) / ((1+r)^n - 1)",
            "Remaining loan balance",
        ),
        ("effective_interest", "(1 + r/n)^n - 1", "Effective annual interest rate"),
    ]

    print("Advanced formulas:")
    for name, formula, description in advanced_formulas:
        try:
            calc.define(name, formula, description)
        except Exception:
            print(f"Note: {name} - {description} (formula may need additional setup)")

    print("\nExample calculations:")

    # Compound Annual Growth Rate
    cagr = calc.calculate("compound_annual_growth", FV=1500, PV=1000, n=5)
    print(f"CAGR (1000 to 1500 over 5 years): {cagr:.2%}")

    # Effective interest rate
    effective = calc.calculate("effective_interest", r=0.12, n=12)
    print(f"Effective rate (12% compounded monthly): {effective:.2%}")

    # Normal distribution at mean (simplified)
    # Note: This would normally require the error function for full implementation
    try:
        # Simple case where x = μ, so the exponential term becomes e^0 = 1
        σ = 1  # Standard normal
        pdf_at_mean = calc.eval("1/sqrt(2*π*σ^2)", σ=σ)
        print(f"Standard normal PDF at mean: {pdf_at_mean:.4f}")
    except Exception:
        print("Normal distribution example needs additional setup")

    print("\n")


def interactive_demo():
    """Interactive demonstration for users to try."""
    print("🎯 Try It Yourself!")
    print("=" * 50)
    print("Here are some expressions you can try with EasyMath:")

    suggestions = [
        "Basic: calc.eval('2x + 3', x=5)",
        "Powers: calc.eval('x^3 + x^2 + x + 1', x=2)",
        "Trig: calc.eval('sin(π/4) + cos(π/4)')",
        "Roots: calc.eval('sqrt(x^2 + y^2)', x=3, y=4)",
        "Logs: calc.eval('log10(x) + ln(y)', x=100, y=math.e)",
        "Define: calc.define('quadratic', 'ax^2 + bx + c')",
        "Use: calc.calculate('quadratic', a=1, b=-2, c=1)",
    ]

    for suggestion in suggestions:
        print(f"  {suggestion}")

    print("\nTo run any example:")
    print("  from easymath import EasyMath")
    print("  calc = EasyMath()")
    print("  # Then try any of the above!")
    print("\n")


def run_all_examples():
    """Run all example categories."""
    print("🚀 EasyMath Complete Examples Demo")
    print("=" * 60)
    print("This demonstration shows EasyMath capabilities across different domains.\n")

    try:
        basic_examples()
        physics_examples()
        finance_examples()
        geometry_examples()
        statistics_examples()
        education_examples()
        advanced_examples()
        interactive_demo()

        print("✅ All examples completed successfully!")
        print("EasyMath is ready to make mathematics accessible to everyone!")

    except Exception as e:
        print(f"❌ Error in examples: {e}")
        print("Please check the EasyMath installation and try again.")


if __name__ == "__main__":
    # Run examples when script is executed directly
    run_all_examples()
