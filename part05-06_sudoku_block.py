# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    a = [sudoku[row_no][column_no],sudoku[row_no][column_no+1],sudoku[row_no][column_no+2],sudoku[row_no+1][column_no],sudoku[row_no+1][column_no+1],sudoku[row_no+1][column_no+2],sudoku[row_no+2][column_no],sudoku[row_no+2][column_no+1],sudoku[row_no+2][column_no+2]]
    print(a)
    d = []
    for e in a:
        if e in d and e > 0:
            return False
        else:
            d.append(e)
    return True

if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 0, 6))
    print(block_correct(sudoku, 1, 2))