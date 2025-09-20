def is_vow(inp):
    result = []
    for i in inp:
        if i == 97:
            result.append('a')
        elif i == 101:
            result.append('e')
        elif i == 105:
            result.append('i')
        elif i == 111:
            result.append('o')
        elif i == 117:
            result.append('u')
        else:
            result.append(i)
    return result