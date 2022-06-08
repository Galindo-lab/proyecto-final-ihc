import pygame

from src.Board import Board
from src.Questions import Questions
from src.Subscribe import SubscribeMQTT
from src.Bitmaptext import Bitmaptext

class Game:
    """Gestor de eventos"""

    CHRONOMETER = pygame.USEREVENT + 1

    def __init__(self):
        self.question = Questions()
        self.board = Board()
        self.counter = 0
        self.correctas = 0
        self.incorrectas = -1
        pygame.time.set_timer(Game.CHRONOMETER, 1000)

        self.listen_tel = SubscribeMQTT()
        self.listen_tel.connect_mqtt()
        self.listen_tel.subscribe()
        self.listen_tel.start()

        self.next_question()

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
                self.listen_tel.stop()
                pygame.quit()

            # if e.type == Game.CHRONOMETER:
            #     print(self.listen_tel.get_data())
            #     self.next_question()

        if self.listen_tel.get_data() != "" and self.listen_tel.get_data() != self.question.answer():
            self.incorrectas += 1
            self.listen_tel.clear_data()
            self.next_question()
        
        if self.listen_tel.get_data() == self.question.answer():
            self.correctas += 1
            self.listen_tel.clear_data()
            self.next_question()
            
        # self.listen_tel.client.loop_stop()
                
        
        
    def draw(self, surface):
        pc = self.correctas
        pi = self.incorrectas
        Bitmaptext.display(surface,
                           f" Correctas: {pc} Incorrectas: {pi}",
                           100,
                           300
        )
        self.board.draw(surface)

