def calculator(a, b, op):
    if type(a) != int or type(b) != int:
        return "unknown value"

    if op not in ['+', '-', '*', '/']:
        return "unknown value"

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b 