def comfortable_word(word):
    left = set("qwertasdfgzxcvb")
    right = set("yuiophjklnm")
    if not word:
        return False
    prev_hand = None
    for char in word.lower():
        if char in left:
            current_hand = "left"
        elif char in right:
            current_hand = "right"
        else:
            return False
        if current_hand == prev_hand:
            return False
        prev_hand = current_hand
    return True
