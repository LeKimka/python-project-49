from random import choice, randint

from brain_games.scripts.engine import start_game


def generate_expression(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    else:
        raise ValueError(f'Unsupported operation: {operation}')


def question_and_answer():
    num1 = randint(1, 100)  # NOSONAR
    num2 = randint(1, 100)  # NOSONAR
    operation = choice(['+', '-', '*'])  # NOSONAR
    expression = f"{num1} {operation} {num2}"
    correct_answer = str(generate_expression(num1, num2, operation))
    return expression, correct_answer


def main():
    game_rule = 'What is the result of the expression?'
    start_game(question_and_answer, game_rule, "Calculate Game")