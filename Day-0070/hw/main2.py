def print_matrix_details(matrix):
    n = len(matrix)
    
    print("Columns:")
    for j in range(n):
        print([matrix[i][j] for i in range(n)])
    
    print("Rows:")
    for row in matrix:
        print(row)
    
    print("Main Diagonal:")
    print([matrix[i][i] for i in range(n)])
    
    print("Secondary Diagonal:")
    print([matrix[i][n-i-1] for i in range(n)])
