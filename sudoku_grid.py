# Please write a function named 
# sudoku_grid_correct(sudoku: list), which 
# takes a two-dimensional array representing a 
# sudoku grid as its argument. The function 
# should use the functions from the three 
# previous exercises to determine whether the 
# complete sudoku grid is filled in correctly. 
# Copy the functions from the exercises above 
# into your Python code file for this exercise.

# The function should check each of the nine 
# rows, columns and 3 by 3 blocks in the grid. 
# If all contain each of the numbers 1 to 9 at 
# most once, the function returns True. If a 
# single one is filled in incorrectly, the 
# function returns False.

# The image of a sudoku grid above these 
# exercises has the nine blocks within the 
# grid indicated with thicker borders. These 
# are the blocks the function should check, 
# and they begin at the indexes (0, 0), (0, 3), 
# (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3)
#  and (6, 6).

def row_correct(sudoku: list, row_no:int):

    numbers = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]

    i = 0

    row = sudoku[row_no]

    for item in row:
        for entity in numbers:
            if entity[0] == item:
                entity[1] += 1

    for entity in numbers:
        if entity[1] > 1:
            value = False
            break
        else:
            value = True

    return value


def column_correct(sudoku:list, column_no: int):
    column = [sublist[column_no] for sublist in sudoku]

    column = (list(filter(lambda x: x != 0,column)))

    correct = (len(column) == len(set(column)))

    if correct == True:
        return(True)
    else:
        return(False)

    print(column)

def block_correct(sudoku:list, row_no:int,column_no:int):
    block = []

    i = 0
    j = 0

    #iterates over rows
    while i < 3:

        j = 0

        while j < 3:

            block.append(sudoku[row_no + i][column_no + j])

            j += 1

            if j == 3:
                i += 1

    block = (list(filter(lambda x: x != 0,block)))

    correct = (len(block) == len(set(block)))

    if correct == True:
        return(True)
    else:
        return(False)


def sudoku_grid_correct(sudoku:list):

    row = 0
    column = 0

    for i in range (9):
        row_status = row_correct(sudoku,i)

        if row_status == True:
            i += 1
        else:
            break

    for i in range(9):
        column_status = column_correct(sudoku,i)

        if column_status == False:
            break
    
    block_status =  True

    for j in range(3):

        if block_status == False:
            break

        for k in range(3):

            row = j*3

            column = k*3

            block_status = block_correct(sudoku,row,column)

            #print(row,column)

            if block_status == False:
                break


    if row_status == False or column_status == False or block_status == False:
        return False
    else:
        return True

        

    


# sudoku1 = [
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],
#   [2, 0, 0, 2, 5, 0, 7, 0, 0],
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],
#   [2, 9, 4, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]

# print(sudoku_grid_correct(sudoku1))


# sudoku2 = [
#   [2, 6, 7, 8, 3, 9, 5, 0, 4],
#   [9, 0, 3, 5, 1, 0, 6, 0, 0],
#   [0, 5, 1, 6, 0, 0, 8, 3, 9],
#   [5, 1, 9, 0, 4, 6, 3, 2, 8],
#   [8, 0, 2, 1, 0, 5, 7, 0, 6],
#   [6, 7, 4, 3, 2, 0, 0, 0, 5],
#   [0, 0, 0, 4, 5, 7, 2, 6, 3],
#   [3, 2, 0, 0, 8, 0, 0, 5, 7],
#   [7, 4, 5, 0, 0, 3, 9, 0, 1]
# ]

# print(sudoku_grid_correct(sudoku2))

# sudoku = [
#   [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
#   [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
#   [ 0, 5, 6, 0, 0, 0, 8, 3, 9 ],
#   [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
#   [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
#   [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
#   [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
#   [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
#   [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
# ]
# print(sudoku_grid_correct(sudoku))