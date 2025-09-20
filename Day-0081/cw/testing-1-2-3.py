def number(lines):
    order = []
    for i in range(len(lines)) :
        word = str(i + 1) + ": " + lines[i]
        order.append(word)
    return order