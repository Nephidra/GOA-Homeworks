import math

def count_area(*args):
    if len(args) == 2:
        length, width = args
        return length * width
    elif len(args) == 1:
        radius = args[0]
        return math.pi * radius ** 2
    elif len(args) == 3:
        pirveli, meore, mesame = args
        s = (pirveli + meore + mesame) / 2
        return math.sqrt(s * (s - pirveli) * (s - meore) * (s - mesame))
    else:
        return "Wrong Args"
print(count_area(2, 3, 4))