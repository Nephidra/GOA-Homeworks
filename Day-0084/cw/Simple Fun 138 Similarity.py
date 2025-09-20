def similarity(a, b):
    i = 0
    j = len(a) + len(b)
    
    for num in a:
        if num in b:
            i += 1
            j -= 1
    
    return i / j