# This is the very last sudoku task. This time we will create a slightly different version of the function for adding new numbers to the grid.

# The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should return a copy of the original grid with the new digit added in the correct location. The function should not change the original grid received as a parameter.

# The print_sudoku function from the previous exercise could be useful for testing, and it is used in the example below:

def print_sudoku(sudoku: list):

    new_sudoku = []


    for i,j in enumerate(sudoku):
        new_sudoku_row=[]
        for index,item in enumerate(j):
            if item == 0:
                new_sudoku_row.append('_')
            elif item != ' ':
                new_sudoku_row.append(item)
            else:
                continue

            if isinstance(item,int) or item == '_' and index != 2 and index != 8:
                new_sudoku_row.append(' ')

        new_sudoku_row.insert(5,' ')
        new_sudoku_row.insert(12,' ')

        new_sudoku.append(new_sudoku_row)

    spaces = [' ']*19

    new_sudoku.insert(3,spaces)
    new_sudoku.insert(7,spaces)


    for index,item in enumerate(new_sudoku):
        for number in item:
            print(number, end="")

        print()



def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new_sudoku = []
    
    for item in sudoku:
        new_sudoku_row = []

        for row in item:
            new_sudoku_row.append(row)

        new_sudoku.append(new_sudoku_row)

    
    new_sudoku[row_no][column_no] = number

    return new_sudoku





# sudoku  = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# grid_copy = copy_and_add(sudoku, 0, 0, 2)
# print("Original:")
# print_sudoku(sudoku)
# print()
# print("Copy:")
# print_sudoku(grid_copy)
