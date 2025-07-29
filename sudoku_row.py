# Write your solution here

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


