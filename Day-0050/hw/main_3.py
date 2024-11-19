def diagonal_sums(matrix):
    n = len(matrix)
    
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    for i in range(n):
        main_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][n-1-i]
    
    return main_diagonal_sum, secondary_diagonal_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = diagonal_sums(matrix)
print("მთავარი დიაგონალი:", result[0])
print("მეორე დიაგონალი:", result[1])
