def is_solved(board):
    n = len(board)
    correct = list(range(n * n))
    
    flat = []
    for i in range(n):
        for j in range(n):
            flat.append(board[i][j])
    
    return flat == correct
