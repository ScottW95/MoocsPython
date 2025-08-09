# Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument. The function should transpose the matrix. Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.

# You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.


def transpose(matrix:list):
    number = len(matrix)
    
    length = len(matrix[0])
    

    new_matrix = []

    i = 0

    j = 0

    while i < length:

        new_matrix_row = []

        while j < number:

            item_to_append = matrix[j][i]

            new_matrix_row.append(item_to_append)

            j += 1

        new_matrix.append(new_matrix_row)

        i += 1
        j = 0

    print(new_matrix)

    matrix[:] = new_matrix



# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# print(matrix)

# print(transpose(matrix))
