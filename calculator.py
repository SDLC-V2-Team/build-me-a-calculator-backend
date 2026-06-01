#!/usr/bin/env python3
"""
Simple command-line calculator using Python's built-in expression evaluation.
Supports: +, -, *, /, and parentheses.
Usage: python calculator.py "2 + 3 * 4"
"""
import sys

def evaluate(expression):
    """Evaluate a mathematical expression safely."""
    safe_dict = {"__builtins__": {}}
    return eval(expression, safe_dict)

def main():
    if len(sys.argv) < 2:
        print("Usage: calculator.py <expression>", file=sys.stderr)
        print("Example: calculator.py \"2 + 3 * 4\"", file=sys.stderr)
        sys.exit(1)
    expression = ' '.join(sys.argv[1:])
    try:
        result = evaluate(expression)
        print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
