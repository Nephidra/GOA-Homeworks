def reverse_letter(s):
    result = ""
    for char in s:
        if char.isalpha():
            result = char + result
    return result