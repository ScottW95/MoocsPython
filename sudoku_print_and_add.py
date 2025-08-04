# In this exercise we will complete two more functions for the sudoku project from the previous section: print_sudoku and add_number.

# The function print_sudoku(sudoku: list) takes a two-dimensional array representing a sudoku grid as its argument. The function should print out the grid in the format specified in the examples below.

# The function add_number(sudoku: list, row_no: int, column_no: int, number:int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should add the digit to the specified location in the grid.# Write your solution here

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


def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

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

# print_sudoku(sudoku)
# add_number(sudoku, 0, 0, 2)
# add_number(sudoku, 1, 2, 7)
# add_number(sudoku, 5, 7, 3)
# print()
# print("Three numbers added:")
# print()
# print_sudoku(sudoku)
