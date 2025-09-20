def cube_odd(arr):
    for x in arr:
        if type(x) != int and type(x) != float:
            return None
    total = 0
    for x in arr:
        if x ** 3 % 2 != 0:
            total += x ** 3
    return total