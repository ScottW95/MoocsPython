#Please write a function named column_correct(sudoku: list, column_no: int), 
# which takes a two-dimensional array representing a sudoku grid, and an 
# integer referring to a single column, as its arguments. Columns are indexed from 0.

#The function should return True or False, depending on whether the 
# column is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

def column_correct(sudoku:list, column_no: int):
    column = [sublist[column_no] for sublist in sudoku]

    column = (list(filter(lambda x: x != 0,column)))

    correct = (len(column) == len(set(column)))

    if correct == True:
        return(True)
    else:
        return(False)

    print(column)

# sudoku = [
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

# print(column_correct(sudoku,1))