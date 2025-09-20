def rps(first_player, second_player) :
    if first_player == "scissors" and second_player == "paper" :
       return "First player won"
    if first_player == "scissors" and second_player == "rock" :
        return "Second player won"
    if first_player == "scissors" and second_player == "scissors" :
        return "Tie"


    if first_player == "paper" and second_player == "rock" :
        return "First player won"
    if first_player == "paper" and second_player == "scisor" :
        return "Second player won"
    if first_player == "paper" and second_player == "paper" :
        return "Tie"


    if first_player == "rock" and second_player == "scissors" :
        return "First player won"
    if first_player == "rock" and second_player == "paper" :
        return "Second player won" 
    if first_player == "rock" and second_player == "rock" :
        return "Tie"

print(rps(input("First move: "), input("Second move: ")))