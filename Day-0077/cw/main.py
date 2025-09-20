def get_grade(s1, s2, s3):
    grade = (s1+s2+s3) / 3
    if grade >= 90 :
        return "A"
    elif grade >= 80 and grade < 90 :
        return "B"
    elif grade >= 70 and grade < 80 :
        return "C"
    elif grade >= 60 and grade < 70 :
        return "D"
    elif grade >= 0 and grade < 60 :
        return "F"