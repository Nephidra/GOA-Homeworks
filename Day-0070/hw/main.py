def generate_2d_array(rows, cols):
    result = []
    num = 1
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(num)
            num += 1
        result.append(row)
    return result