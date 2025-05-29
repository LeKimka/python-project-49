from random import randint
from brain_games.scripts.engine import start_game

def is_even(number):
    return number % 2 == 0

def question_and_answer():
        number = randint(1, 1000)
        question = str(number)
        correct_answer = "yes" if is_even(number) else "no"
        return question, correct_answer

def main():
    game_rule = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'
    start_game(question_and_answer, game_rule, "Even Game")