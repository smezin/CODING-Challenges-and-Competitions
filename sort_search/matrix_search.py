MATRIX = [
    [15,20,40,85],
    [20,35,80,95],
    [30,55,95,105],
    [40,80,100,120]
]

def search_matrix(matrix, num):
    """
    searches 'num' in doubly sorted matrix (both rows and cols are sorted)
    """
    first_row_i = 0
    first_col_i = 0
    last_row_i = len(matrix) - 1
    last_col_i = len(matrix[0]) - 1
    return reduce_matrix(matrix, num, first_row_i, last_row_i, first_col_i, last_col_i)

def reduce_matrix(matrix, num, first_row_i, last_row_i, first_col_i, last_col_i):
    #print ([[matrix[m][n] for n in range(last_col_i+1)] for m in range(first_row_i, last_row_i + 1)])
    for i in range (first_col_i, last_col_i + 1):
        print ([matrix[i][j] for j in range(last_col_i + 1)])
        
    if matrix[first_row_i][last_col_i] == num:
            print(num, 'found at index \n',[first_row_i, last_col_i])
            return [first_row_i, last_col_i] 

    for i in range(last_col_i, -1, -1):
        while matrix[first_row_i][last_col_i] > num:
            last_col_i -= 1
    
    for i in range(first_row_i, last_row_i):
        while matrix[first_row_i][last_col_i] < num:
            first_row_i += 1
    
    return reduce_matrix(matrix, num, first_row_i, last_row_i, first_col_i, last_col_i)

search_matrix(MATRIX, 120)   

