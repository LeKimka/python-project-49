from random import randint

from brain_games.scripts.engine import start_game


def generate_expression(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def question_and_answer():
    num1 = randint(1, 100)  # NOSONAR
    num2 = randint(1, 100)  # NOSONAR
    expression = f"{num1} {num2}"
    correct_answer = str(generate_expression(num1, num2))
    return expression, correct_answer


def main():
    game_rule = 'Find the greatest common divisor of given numbers.'
    start_game(question_and_answer, game_rule, "GCD Game")