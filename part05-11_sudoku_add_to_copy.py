# Write your solution here
def print_sudoku(sudoku: list):
    indexes = [0,1,2,3,4,5,6,7,8]
    c = 1
    d = 1
    for a in indexes:
        if a == 3 or a == 6:
            print()
        for b in indexes:
            if sudoku[a][b] == 0:
                sudoku[a][b] = "_"
            if c != 3 and c != 6 and c != 9:
                print(sudoku[a][b],end=" ")
                c += 1
            elif c != 9:
                print(sudoku[a][b],end="  ")
                c += 1
            else:
                print(sudoku[a][b])
                c = 1


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    a = []
    indexes = [0,1,2,3,4,5,6,7,8]
    for b in indexes:
        d = []
        for c in indexes:
            d.append(sudoku[b][c])
        a.append(d)
    print(a)

    if number >= 1 and number <= 9:
        a[row_no][column_no]=number
    else:
        return -1
    return a



if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)