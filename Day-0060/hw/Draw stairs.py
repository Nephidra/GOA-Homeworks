def draw_stairs(n):
    result = ""
    for i in range(n):
        result += " " * i + "I" + ("\n" if i < n - 1 else "")
    return result