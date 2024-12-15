def calc(a, b) :
    score1 = (a[0] * (a[2] / 10)) + (a[1] * (a[2] / 10))
    score2 = (b[0] * (b[2] / 10)) + (b[1] * (b[2] / 10))

    if score1 > score2 :
        return "Player 1 won"
    elif score1 < score2 :
        return "Player 2 won"
    else :
        return "Tie"

print(calc([1, 2, 3], [4, 5 , 6]))