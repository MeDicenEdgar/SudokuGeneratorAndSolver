from random import shuffle, randint
from turtle import width
import pygame
from constants import *

window = pygame.display.set_mode((WIDTH, HEIGHT))

class Space:
    def __init__(self, value, canUserInput=False):
        self.value = value
        if value == 0:
            self.canUserInput = True
        else:
            self.canUserInput = canUserInput
    
    def __repr__(self) -> str:
        return self.value

def main():
    pygame.display.set_caption("Sudoku!")
    clock = pygame.time.Clock()
    run = True
    state = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        state = drawWindow(state)
    pygame.quit()

def drawWindow(state):
    window.fill(WHITE)
    if state == 0:
        drawMenu()
    pygame.display.update()
    return state

def drawMenu():
    width = 110
    height = 50
    pygame.draw.rect(window, GREY, (WIDTH/2-width/2, WIDTH/3-width/3, width, height))
    pygame.draw.rect(window, GREY, (WIDTH/2-width/2, (WIDTH/3-width/3)*1.8, width, height))
    pygame.draw.rect(window, GREY, (WIDTH/2-width/2, (WIDTH/3-width/3)*2.6, width, height))
    pygame.draw.line(window, BLACK, (0, HEIGHT/6), (WIDTH, HEIGHT/6))


def isValidMove(board, row, col, num):
    for i in range(9):
        if board[row][i].value == num:
            return False

    for x in range(9):
        if board[x][col].value == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol].value == num:
                return False
    return True
 

def hasGameEnded(board):
    for i in range(9):
        for j in board[i]:
            if j.value == 0:
                return False
    return True

def changeBoard(board, x, y, value):
    if board[x][y].canUserInput == False:
        return False
    else:
        board[x][y].value = value
        return True

def printBoard(board):
    printable = ""
    for i in range(9):
        printable+="|"
        for j, n in enumerate(board[i]):
            if n.value == 0: 
                printable  += " |"
            else:
                printable+="{}|".format(n.value)
            if j==2 or j == 5:
                printable+="  |"
        printable+="\n"
        if i ==5 or i == 2:
            printable+="-------------------------\n"
    print(printable)

def deleteValue(board, x, y):
    if board[x][y].canUserInput == True:
        board[x][y].value = 0
        return True
    return False

def solveSudoku(board, x, y):
    if (x == 8 and y >= 9):
        return True
    if y == 9:
        x += 1
        y = 0
    if board[x][y].value > 0:
        return solveSudoku(board, x, y+1)
    for num in range(1, 10, 1):
        if isValidMove(board, x, y, num) == True:
            board[x][y].value = num
            printBoard(board)
            if solveSudoku(board, x, y + 1) == True:
                return True
        board[x][y].value = 0
    return False

def generateSudokuSolved(board, x, y):
    numbers = [1,2,3,4,5,6,7,8,9]
    shuffle(numbers)
    if (x == 8 and y >= 9):
        return True
    if y == 9:
        x += 1
        y = 0
    if board[x][y].value > 0:
        return solveSudoku(board, x, y+1)
    for num in numbers:
        if isValidMove(board, x, y, num) == True:
            board[x][y].value = num
            printBoard(board)
            if solveSudoku(board, x, y + 1) == True:
                if x==0 and y == 0:
                    unsolve(board)
                return True
                
        board[x][y].value = 0
    return False

def unsolve(board):
    clues = randint(17,30)
    usedCoords=[]
    while len(usedCoords)<(81-clues):
        x = randint(0,8)
        y = randint(0,8)
        if [x,y] not in usedCoords:
            usedCoords.append([x,y])
            board[x][y].value = 0
            printBoard(board)
