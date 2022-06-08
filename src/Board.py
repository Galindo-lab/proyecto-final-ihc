import pygame

from src.Questions import Questions
from src.Color import Color
from src.Bitmaptext import Bitmaptext


class Board:
    """"""

    def __init__(self):
        self.question = ""
        self.options = []

    def set(self, question: str, options: list) -> None :
        self.question = question
        self.options = options
    
    def display_border(self, surface: pygame.Surface) -> None:
        rect = pygame.Rect(15, 15, 770, 570)
        pygame.draw.rect(surface, Color.WHITE, rect, 2)

    def display_question(self, surface: pygame.Surface) -> None:
        Bitmaptext.display(surface, self.question, 30, 50, font=Bitmaptext.TITLE)
        
    def display_answers(self, surface: pygame.Surface) -> None:
        for cont, option in enumerate(self.options):
            Bitmaptext.display(surface, f"{cont}) {option}", 50,
                               cont * 25 + 100)

    def draw(self, surface: pygame.Surface) -> None:
        self.display_border(surface)
        self.display_question(surface)
        self.display_answers(surface)

    def update(self):
        pass
