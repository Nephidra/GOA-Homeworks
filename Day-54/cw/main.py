import math

def count_area(a, b=None, c=None):
    if b is not None and c is None:
        return a * b
    elif b is None and c is None:
        return math.pi * a ** 2
    elif b is not None and c is not None:
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        return "Invalid arguments"