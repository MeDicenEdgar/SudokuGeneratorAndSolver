from ast import While
import pygame

FPS = 24
WIDTH= 400
HEIGHT = 400

WHITE = (255,255,255)
GREY = (190, 196, 197)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255, 0, 0)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
fontMenu = pygame.font.Font("Resources/SYNNova-Bold.otf", 50)
fontButtons = pygame.font.Font("Resources/SYNNova-Bold.otf", 40)
fontNumbers = pygame.font.Font("Resources/SYNNova-Bold.otf", 12)
menuTitleText = fontMenu.render("Sudoku!", True, BLACK)
button1Text = fontButtons.render("Play!", True, WHITE)
button2Text = fontButtons.render("Solve!", True, WHITE)
