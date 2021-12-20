# Write your solution here
def row_correct(sudoku: list, row_no: int):
    correct = [1,2,3,4,5,6,7,8,9]
    for a in correct:
        if sudoku[row_no].count(a) > 1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    correct = [1,2,3,4,5,6,7,8,9]
    a = []
    for row in sudoku:
        a.append(row[column_no])
    for b in correct:
        if a.count(b) > 1:
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for r in range(row_no, row_no+3):
        for s in range(column_no, column_no+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
 
    return True

def sudoku_grid_correct(sudoku: list):
    indexes = [0,1,2,3,4,5,6,7,8]
    blocks = [0,3,6]
    a = True
    for b in indexes:
        a = row_correct(sudoku,b)
        if a == False:
            return a

    for b in indexes:
        a = column_correct(sudoku,b)
        if a == False:
            return False
        
    for b in blocks:
        for c in blocks:
            a = block_correct(sudoku,b,c)
            if a == False:
                return False
    
    return a

if __name__ == "__main__":
    sudoku = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku))