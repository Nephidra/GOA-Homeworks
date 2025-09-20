def find_multiples(integer, limit):
    multiples = []
    for i in range(integer, limit + 1, integer):
        multiples.append(i)
    return multiples