def capitalize(s, ind):
    chars = list(s)
    for i in ind:
        if i < len(chars):
            chars[i] = chars[i].upper()
    return ''.join(chars)