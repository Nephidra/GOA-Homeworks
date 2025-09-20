def starting_mark(height):
    x1, y1 = 1.52, 9.45
    x2, y2 = 1.83, 10.67
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    starting_mark = m * height + b
    return round(starting_mark, 2)
