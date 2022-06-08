import json
from random import randint


class Questions:

    QUESTION = "question"
    OPTIONS = "options"
    ANSWER = "answer"

    def __init__(self):
        self.n_pregunta = 0
        self.questions_file = open('data/data.json')
        self.questionnaire = json.load(self.questions_file)

    def next_question(self) -> None:
        """Pasar a la siguiente pregunta"""
        n_preguntas = len(self.questionnaire)
        siguiente = (self.n_pregunta +
                     randint(1, n_preguntas - 1)) % n_preguntas
        self.n_pregunta = siguiente

    def current_question(self) -> dict:
        """obtener la respuesta"""
        return self.questionnaire[self.n_pregunta]

    def question_attrib(self, attrib: str) -> str:
        """Atributo de uns pregunta"""
        question = self.current_question()
        return question[attrib]

    def options(self) -> list:
        return self.question_attrib(Questions.OPTIONS)

    def answer(self) -> str:
        return self.question_attrib(Questions.ANSWER)

    def question(self) -> str:
        return self.question_attrib(Questions.QUESTION)
