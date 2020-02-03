import time
"""
The program takes an incomplete sudoku board and returns the board solved.
The input is inserted row by row using the number 0 for the empty cells.
To solve the board is been used the backtracking algorithm.
"""


def solving(board):
    find = finding_empty(board)
    if not find:
        return True  # board is complete
    else:
        row, col = find

    for i in range(1, 10):
        if validating(board, i, (row, col)):
            board[row][col] = i

            if solving(board):
                return True

            board[row][col] = 0

    return False


def finding_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # row, column
    return None


def validating(board, num, pos):
    """board: the board itself
       num: the number inserted inside the board as a possible solution
       pos: a tuple with the coordinates of the empty slots in the board"""

    # checking row: moving horizontally inside each row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # checking column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != 1:
            return False

    # check each of the 3x3 sector in the board
    sector_x = pos[1] // 3
    sector_y = pos[0] // 3

    for i in range(sector_y*3, sector_y*3 + 3):
        for j in range(sector_x*3, sector_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def creating_board():
    """INPUT: string
       OUTPUT: none, append to a list
       The function validate the input and append to a list."""
    while True:
        try:
            string = input()
            rows = [int(x) for x in string]
        except ValueError:
            print("Make sure you only insert integer numbers")
        else:
            if len(rows) != 9:
                print("Make sure you insert 9 numbers per row")
            else:
                sudoku_board.append(rows)
                break


def printing_board(board):
    """INPUT: nested list.
       OUTPUT: none, print on screen.
       The function print the board as a 9X9 grid"""

    for i in range(len(board)):  # moving vertically in the grid
        if i % 3 == 0 and i != 0:  # not equal to 0 to don't have a line at the beginning
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):  # moving horizontally
            if j % 3 == 0 and j != 0:  # same as before
                print(" | ", end='')

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end='')


if __name__ == "__main__":

    sudoku_board = []
    for row_num in range(1, 10):
        print(f"insert the row n' {row_num} and press ENTER (use 0 for the empty cells): ")
        creating_board()
    print('\n')
    print("Here's the board entered:\n")
    printing_board(sudoku_board)
    print('\n')
    print("Solving...")
    print('\n')

    start_time = time.time()
    solving(sudoku_board)
    end_time = time.time()

    running_time = round(end_time - start_time, 2)
    printing_board(sudoku_board)

    print(f"Running time: {running_time} seconds")

# rows for testing from sudoku.com

# medium     # easy       # hard       # expert
# 159000070  # 780400120  # 007002000  # 530072008
# 007000154  # 600075009  # 090000018  # 609000000
# 000000009  # 000601078  # 084100000  # 000000001
# 910000000  # 007040260  # 600904501  # 050000160
# 003007805  # 001050930  # 001000040  # 200390000
# 000010020  # 904060005  # 009003020  # 400100800
# 000903407  # 070300012  # 400000062  # 000060490
# 000000002  # 120007400  # 000029000  # 000005000
# 098006000  # 049206007  # 008500000  # 074000000
