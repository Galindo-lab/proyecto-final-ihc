import pygame

from src.Board import Board
from src.Questions import Questions
from src.Subscribe import SubscribeMQTT


class Game:
    """Gestor de eventos"""

    CHRONOMETER = pygame.USEREVENT + 1

    def __init__(self):
        self.question = Questions()
        self.board = Board()
        self.counter = 0
        pygame.time.set_timer(Game.CHRONOMETER, 1000)

        self.listen_tel = SubscribeMQTT()
        self.listen_tel.connect_mqtt()
        self.listen_tel.subscribe()

    def next_question(self):
        self.question.next_question()
        self.board.set(
            self.question.question(),
            self.question.options()
        )

    def update(self, dt):
        # self.listen_tel.client.loop_start()
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()

            if e.type == Game.CHRONOMETER:
                print(self.listen_tel.get_data())
                self.next_question()

        # self.listen_tel.client.loop_stop()
                
        
        
    def draw(self, surface):
        self.board.draw(surface)

