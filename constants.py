import pygame

FPS = 24
WIDTH= 400
HEIGHT = 400

WHITE = (255,255,255)
GREY = (190, 196, 197)
BLACK = (0,0,0)


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
fontMenu = pygame.font.Font("SYNNova-Bold.otf", 40)
fontButtons = pygame.font.Font("SYNNova-Bold.otf", 20)
menuTitleText = fontMenu.render("Sudoku!", True, BLACK)