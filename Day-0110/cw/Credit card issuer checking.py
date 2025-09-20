def get_issuer(number):
    number = str(number)
    length = len(number)

    if length == 15 and (number.startswith("34") or number.startswith("37")):
        return "AMEX"
    elif length == 16 and number.startswith("6011"):
        return "Discover"
    elif length == 16 and number[:2] in ["51", "52", "53", "54", "55"]:
        return "Mastercard"
    elif length in [13, 16] and number.startswith("4"):
        return "VISA"
    else:
        return "Unknown"
