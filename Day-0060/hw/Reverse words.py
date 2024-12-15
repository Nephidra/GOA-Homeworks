def reverse_words(text):
    words = text.split(' ')
    reversed_words = ' '.join(word[::-1] for word in words)
    return reversed_words