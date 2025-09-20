def camel_case(s):
    words = s.split(" ")
    result = ""
    
    for word in words:
        if len(word) > 0:
            first_char = word[0].upper()
            rest = word[1:]
            capitalized_word = first_char + rest
            result += capitalized_word
    
    return result