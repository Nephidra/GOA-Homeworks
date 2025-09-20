def valid_card(card):
    card = card.replace(" ", "")
    total = 0
    reverse_digits = card[::-1]

    for i in range(len(reverse_digits)):
        digit = int(reverse_digits[i])
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0
