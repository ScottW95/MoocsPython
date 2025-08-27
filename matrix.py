# The file matrix.txt contains a matrix in the format 
# specified in the example below:

# 1,0,2,8,2,1,3,2,5,2,2,2
# 9,2,4,5,2,4,2,4,1,10,4,2
# ...etc...

# Please write two functions, named matrix_sum and 
# matrix_max. Both go through the matrix in the file, 
# and then return the sum of the elements or the 
# element with the greatest value, as the names of the 
# functions imply.

# Please also write the function row_sums, which 
# returns a list containing the sum of each row in 
# the matrix. For example, calling row_sums when the 
# matrix in the file is defined as

# 1,2,3
# 2,3,4

# the function should return the list [6, 9].

# Hint: you can also include other helper functions in 
# your program. It is very worthwhile to spend a moment 
# considering which functionalities are shared by the 
# three functions you are asked to write. Notice that 
# the three functions named above do not take any 
# arguments, but any helper functions you write may 
# take arguments. The file you are working with is 
# always named matrix.txt.



def matrix_sum():
    matrix = get_matrix()

    total_sum = 0

    for index,item in enumerate(matrix):

        total_sum += sum(item)

    return(total_sum)


def matrix_max():
    matrix = get_matrix()

    max_item = 0

    for index, row in enumerate(matrix):
        for index, item in enumerate(row):
            if item > max_item:
                max_item = item

    return(max_item)
    


def row_sums():
    matrix = get_matrix()

    row_sums = []

    for index,row in enumerate(matrix):

        row_sums.append(sum(row))

    return row_sums



def get_matrix():
    with open('matrix.txt') as new_file:
        matrix_list = []

        line_list = []


        for line in new_file:

            line = line.replace('\n','')

            parts = line.split(',')

            for part in parts:
                line_list.append(int(part))

            matrix_list.append(line_list)

            line_list = []

    return(matrix_list)





# print(matrix_sum())
# print(matrix_max())
# print(row_sums())