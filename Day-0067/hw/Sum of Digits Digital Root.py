def digital_root(n):
    while n >= 10:
        total = 0
        temp = n
        while temp > 0:
            total += temp % 10
            temp //= 10
        n = total
    return n