from random import shuffle, randint
import pygame
from constants import *

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
    pygame.mixer.music.load("Resources/Music.mp3")
    pygame.mixer.music.play(-1)
    pygame.display.set_caption("Sudoku!")
    clock = pygame.time.Clock()
    run = True
    val = None
    state = 0
    x, y = 0, 0
    generated = False
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print("{}, {}".format(x, y))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    val = 1
                if event.key == pygame.K_2:
                    val = 2   
                if event.key == pygame.K_3:
                    val = 3
                if event.key == pygame.K_4:
                    val = 4
                if event.key == pygame.K_5:
                    val = 5
                if event.key == pygame.K_6:
                    val = 6
                if event.key == pygame.K_7:
                    val = 7
                if event.key == pygame.K_8:
                    val = 8
                if event.key == pygame.K_9:
                    val = 9 
                if event.key == pygame.K_RETURN:
                    if state == 1:
                        if hasGameEnded(board):
                            state = 3
                    elif state == 2:
                        solveSudoku(board, 0, 0)
                        state = 4
                    elif state == 4:
                        x, y = 0, 0
                        board = resetBoard(board)
                        state = 0
                        generated = False
                if event.key == pygame.K_ESCAPE:
                    state = 0
                    x, y = 0,0
                        

        state, generated, val, board = drawWindow(state, board, x, y, generated, val)
    pygame.quit()

def drawWindow(state, board, x, y, generated, val):
    window.fill(WHITE)
    if state == 0:
        drawMenu()
    elif state == 1:
        state = drawBoard(board)
        generated, val= boardGameLogic(board, x, y, generated, val)
    elif state == 2 or state == 4:
        drawCreator(board)
        val = creatorLogic(board,x ,y, val)
    elif state == 3:
        board = drawCongratulations(board)
        generated = False
    
    if state == 4:
        window.blit(solved, (20, 350))

    pygame.display.update()
    if ((x >= 105) and (y >= 135) and x <= 295 and y <= 205) and state == 0:
        state = 1
        x,y = 0,0

    if ((x >= 105) and (y >= 245) and x <= 295 and y <= 315) and state == 0:
        state = 2
        x,y = 0,0
    
    if ((x >= 50) and (y >= 50) and x <= 350 and y <= 140) and state == 3:
        state = 0
        x,y = 0,0

    return state, generated, val, board

def drawBoard(board):
    gap = (WIDTH-100) / 9
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(window, BLACK, (50, 50 + gap*i), (WIDTH-50, 50 + gap*i), 2)
            pygame.draw.line(window, BLACK, (50 + gap*i, 50), (50 + gap*i, HEIGHT - 50), 2)
        else:
            pygame.draw.line(window, BLACK, (50, 50 + gap*i), (WIDTH-50, 50 + gap*i))
            pygame.draw.line(window, BLACK, (50 + gap*i, 50), (50 + gap*i, HEIGHT - 50))

    for i in range(9):
        for j in range(9):
            drawValue(board[j][i].value, 62+ gap*i, 60+ gap*j)

    return 1
    
def boardGameLogic(board, x, y, generated, val):
    selected = []
    row,col = 0,0
    if generated == False:
        generateSudokuSolved(board, 0, 0)
        return True, val
    if x>=50 and x<=350 and y<=350 and y>=50:
        col, row = convertMouse(x,y)
        col, row = int(row), int(col)
        print("{}, {}, {}".format(row, col, board[row][col].canUserInput))
        selected = [row, col]
        drawSelected(board, row, col)
    if val is not None:
        if selected is not None and isValidMove(board, col, row, val) :
            changeBoard(board, col, row, val)
            val = None
    return generated, val

def convertMouse(x,y):
    gap = 300/9
    x -= 50
    y -= 50
    x = x/gap
    y = y/gap
    return x, y

def drawCreator(board):
    gap = (WIDTH-100) / 9
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(window, BLACK, (50, 50 + gap*i), (WIDTH-50, 50 + gap*i), 2)
            pygame.draw.line(window, BLACK, (50 + gap*i, 50), (50 + gap*i, HEIGHT - 50), 2)
        else:
            pygame.draw.line(window, BLACK, (50, 50 + gap*i), (WIDTH-50, 50 + gap*i))
            pygame.draw.line(window, BLACK, (50 + gap*i, 50), (50 + gap*i, HEIGHT - 50))

    for i in range(9):
        for j in range(9):
            drawValue(board[j][i].value, 62+ gap*i, 60+ gap*j)

    return 2

def creatorLogic(board, x, y, val):
    if x>=50 and x<=350 and y<=350 and y>=50:
        col, row = convertMouse(x,y)
        col, row = int(row), int(col)
        print("{}, {}, {}".format(row, col, board[row][col].canUserInput))
        selected = [row, col]
        drawSelected(board, row, col)
    if val is not None:
        if selected is not None and isValidMove(board, col, row, val) :
            changeBoard(board, col, row, val)
            val = None
    return val

def drawMenu():
    width = 190
    height = 70
    pygame.draw.rect(window, GREY, (WIDTH/2-width/2, WIDTH/2-width/3, width, height))
    pygame.draw.rect(window, GREY, (WIDTH/2-width/2, (WIDTH/2-width/3)*1.8, width, height))
    pygame.draw.rect(window, BLACK, (WIDTH/2-width/2, WIDTH/2-width/3, width, height), 1)
    pygame.draw.rect(window, BLACK, (WIDTH/2-width/2, (WIDTH/2-width/3)*1.8, width, height), 1)
    pygame.draw.line(window, BLACK, (0, HEIGHT/5), (WIDTH, HEIGHT/5))
    window.blit(menuTitleText, (WIDTH/2-90,17))
    window.blit(button1Text, (WIDTH/2-43, HEIGHT/2-55))
    window.blit(button2Text, (WIDTH/2-55, (HEIGHT/2)+55))

def drawValue(value, x, y):
    if value == 0:
        return
    text = fontNumbers.render(str(value), 1, BLACK)
    window.blit(text, (x, y))

def drawSelected(board, row, col):
    gap = (WIDTH-100)/9
    if board[col][row].canUserInput == False:
        pygame.draw.rect(window, RED, (50+row*gap, 50+col*gap, gap+2, gap), 3)
    elif board[col][row].canUserInput == True:
        pygame.draw.rect(window, GREEN, (50+row*gap, 50+col*gap, gap+2, gap), 3)

def drawCongratulations(board):
    pygame.draw.rect(window, GREY, (50,50,300,90))
    pygame.draw.rect(window, BLACK, (50,50,300,90), 2)
    congText = fontButtons.render("Congratulations!", True, BLACK)
    clickText = fontNumbers.render("Click Here to return to the main menu", True, BLACK)
    window.blit(congText, (53,60))
    window.blit(clickText, (100,110))
    board = resetBoard(board)
    return board
    
def resetBoard(board):
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
    return board
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
    clues = randint(17, 40)
    usedCoords=[]
    while len(usedCoords)<(81-clues):
        x = randint(0,8)
        y = randint(0,8)
        if [x,y] not in usedCoords:
            usedCoords.append([x,y])
            board[x][y].value = 0
            printBoard(board)
    
    for i in range(9):
        for j in range(9):
            if board[i][j].value != 0:
                board[i][j].canUserInput = False
