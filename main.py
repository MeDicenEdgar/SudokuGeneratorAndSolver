from functions import *

if __name__ == "__main__":
    board = [
        [Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0)],
        [Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0)],
        [Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0)],
        [Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0)],
        [Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0)],
        [Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0)],
        [Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0)],
        [Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0)],
        [Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0),Space(0)]]

    while not hasGameEnded(board):
        printBoard(board)
        playerAction = eval(input("Action: "))
        if playerAction == 1:
            x = eval(input("x: "))
            y = eval(input("y: "))
            value = eval(input("value: "))
            if isValidMove(board, x, y, value):
                status = changeBoard(board, x, y, value)
        elif playerAction == 2:
            generateSudokuSolved(board,0,0)
        elif playerAction == 3:
            solveSudoku(board, 0, 0)
    printBoard(board)
        
    
