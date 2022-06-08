import pygame

from src.Board import Board
from src.Questions import Questions


class Game:
    """Gestor de eventos"""

    CHRONOMETER = pygame.USEREVENT + 1

    def __init__(self):
        self.question = Questions()
        self.board = Board()
        self.counter = 0
        pygame.time.set_timer(Game.CHRONOMETER, 1000)

    def next_question(self):
        self.question.next_question()
        self.board.set(self.question.question(), self.question.options())

    def update(self, dt):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()

            if e.type == Game.CHRONOMETER:
                self.next_question()

    def draw(self, surface):
        self.board.draw(surface)

