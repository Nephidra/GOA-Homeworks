def pluralize(word):
    last = word[-1]
    last_two = word[-2:] if len(word) >= 2 else ''
    if last_two == 'ch' or last_two == 'sh' or last in ('s', 'x', 'z'):
        return word + 'es'
    elif last == 'y' and len(word) > 1 and word[-2] not in 'aeiou':
        return word[:-1] + 'ies'
    else:
        return word + 's'