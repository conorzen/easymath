"""
Command-line interface for EasyMath.

This module provides a simple command-line calculator interface
for users who want to use EasyMath from the terminal.
"""

import sys
import argparse
from .core import EasyMath
from .examples import run_all_examples


def interactive_mode():
    """Run EasyMath in interactive mode."""
    print("🧮 EasyMath Interactive Calculator")
    print("=" * 40)
    print("Type mathematical expressions or commands.")
    print("Commands: help, functions, define <name> <expr>, quit")
    print("Examples: 2x + 3 (then enter x=5), sin(π/2), sqrt(16)")
    print()
    
    calc = EasyMath()
    
    while True:
        try:
            # Get user input
            user_input = input("math> ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye! 👋")
                break
            
            elif user_input.lower() == 'help':
                calc.help()
                continue
            
            elif user_input.lower() == 'functions':
                calc.list_functions()
                continue
            
            elif user_input.lower().startswith('define '):
                # Parse define command: define <name> <expression>
                parts = user_input.split(' ', 2)
                if len(parts) < 3:
                    print("Usage: define <name> <expression>")
                    continue
                
                name = parts[1]
                expression = parts[2]
                
                try:
                    calc.define(name, expression)
                except Exception as e:
                    print(f"Error defining function: {e}")
                continue
            
            # Try to evaluate as expression
            try:
                # Check if expression contains variables
                from .core import get_expression_variables
                variables = get_expression_variables(user_input)
                
                if variables:
                    # Ask for variable values
                    var_values = {}
                    print(f"Variables needed: {', '.join(variables)}")
                    
                    for var in variables:
                        while True:
                            try:
                                value = input(f"  {var} = ")
                                var_values[var] = float(value)
                                break
                            except ValueError:
                                print("  Please enter a number.")
                    
                    result = calc.eval(user_input, **var_values)
                else:
                    # No variables needed
                    result = calc.eval(user_input)
                
                print(f"= {result}")
                
            except Exception as e:
                print(f"Error: {e}")
                print("Type 'help' for usage information.")
        
        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break
        except EOFError:
            print("\nGoodbye! 👋")
            break


def evaluate_expression(expression, variables=None):
    """Evaluate a single expression with optional variables."""
    calc = EasyMath()
    
    try:
        if variables:
            # Parse variables from command line format
            var_dict = {}
            for var_assignment in variables:
                if '=' not in var_assignment:
                    print(f"Invalid variable assignment: {var_assignment}")
                    print("Use format: variable=value")
                    return 1
                
                name, value = var_assignment.split('=', 1)
                try:
                    var_dict[name.strip()] = float(value.strip())
                except ValueError:
                    print(f"Invalid numeric value: {value}")
                    return 1
            
            result = calc.eval(expression, **var_dict)
        else:
            result = calc.eval(expression)
        
        print(result)
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="EasyMath - Natural mathematical expressions for everyone",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  easymath                          # Interactive mode
  easymath "2 + 3"                 # Evaluate expression
  easymath "2x + 1" x=5            # Expression with variables
  easymath --examples              # Show examples
  
Interactive mode commands:
  help                             # Show help
  functions                        # List defined functions
  define circle_area "π * r^2"     # Define new function
  quit                             # Exit
        """
    )
    
    parser.add_argument(
        'expression', 
        nargs='?', 
        help='Mathematical expression to evaluate'
    )
    
    parser.add_argument(
        'variables',
        nargs='*',
        help='Variable assignments in format var=value'
    )
    
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Start in interactive mode'
    )
    
    parser.add_argument(
        '--examples',
        action='store_true',
        help='Show comprehensive examples'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='EasyMath 1.0.0'
    )
    
    args = parser.parse_args()
    
    # Show examples
    if args.examples:
        run_all_examples()
        return 0
    
    # Interactive mode
    if args.interactive or (not args.expression and not args.examples):
        interactive_mode()
        return 0
    
    # Evaluate single expression
    if args.expression:
        return evaluate_expression(args.expression, args.variables)
    
    # If we get here, show help
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())