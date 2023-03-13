import logging
from typing import List, Optional


logging.basicConfig(level=logging.DEBUG,filename="data.log", filemode="a", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt="%d/%m/%Y %H:%M:%S")


class Question:
    def __init__(self, ask: str, answer: str):
        self.ask = ask
        self.answer = answer

class Game:
    def __init__(self, questions: Optional[List[Question]]):
        self.questions = questions
        self.score = 0
    
    def start_game(self) -> str:
        player_name = input("Please enter Your name: ")
        print(f"Hello {player_name}, welcome to the game!")
        input("Press ANY KEY to start the game!")
        for question in self.questions:
            answer = input(question.ask)
 
            try:
                if answer.lower() == question.answer.lower():
                    print("Correct! You got 1 point")
                    logging.info(f"Correct answer: {answer}")
                    self.score += 1
                else:
                    print(f"Incorrect! The correct answer was: { question.answer }")
                    logging.warning(f"Incorrect answer: {answer}")
                    
            except Exception as e:
                logging.error(e)
        print("Game is finished!")
        print(f"Your result is: {self.score}/{len(self.questions)}")      
        logging.info(f"Final score is: {self.score}/{len(self.questions)}")

q1 = Question("What is the capital of Lithuania?", "Vilnius")
q2 = Question("What is the capital of Latvia?", "Riga")
q3 = Question("What is the capital of Estonia?", "Tallinn")
q4 = Question("What is the capital of Italy?", "Rome")
q5 = Question("What is the capital of France?", "Paris")

questions = [q1, q2, q3, q4, q5]

test = Game(questions)
test.start_game()