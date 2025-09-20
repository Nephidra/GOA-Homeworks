def open_or_senior(data):
    cate = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            cate.append("Senior")
        else:
            cate.append("Open")
    return cate