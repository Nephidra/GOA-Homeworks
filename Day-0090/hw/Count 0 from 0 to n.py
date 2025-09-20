def count_zeros(n):
    counter = 0
    for i in range(1, n + 1):
        counter += str(i).count('0')
    return counter