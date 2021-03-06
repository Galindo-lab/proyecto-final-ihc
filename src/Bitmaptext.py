import pygame
from src.Color import Color

pygame.font.init()


class Bitmaptext:
    """"""

    # estilos del texto
    TITLE = pygame.font.SysFont('Consolas', 25)
    NORMAL = pygame.font.SysFont('Consolas', 20)

    def __init__(self):
        pass

    @classmethod
    def display(cls, surface, text, x, y, color=Color.WHITE, font=None):
        if (font is None): font = Bitmaptext.NORMAL
        text_surface = font.render(text, False, color)
        surface.blit(text_surface, pygame.math.Vector2(x, y))
