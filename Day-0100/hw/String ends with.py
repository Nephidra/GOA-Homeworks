def solution(text, ending):
    ending_length = len(ending)
    if text[-ending_length:] == ending:
        return True
    else:
        return False
