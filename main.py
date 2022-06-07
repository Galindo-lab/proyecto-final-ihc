import pygame, time

from src.Game import Game

pygame.init()
pygame.font.init()

# settings
WINDOW_TITLE = "Proyecto Final"
WINDOW_DIMENSION = (800, 600)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TARGET_FPS = 60

# base configurations
pygame.display.set_caption(WINDOW_TITLE)
window = pygame.display.set_mode(WINDOW_DIMENSION)
canvas = pygame.Surface(WINDOW_DIMENSION)
clock = pygame.time.Clock()
running = True

# Init
game = Game()

while True:
    dt = clock.tick(60) * .001 * TARGET_FPS
    canvas.fill((0, 0, 0))
    
    game.update(dt)
    game.draw(canvas)
    
    window.blit(canvas, (0, 0))
    pygame.display.update()

