from random import randint

from brain_games.scripts.engine import start_game


def generate_expression(start, step, index):
    return [start + i * step for i in range(index)]


def question_and_answer():
    index = randint(5, 10)  # NOSONAR
    start = randint(1, 20)  # NOSONAR
    step = randint(1, 10)  # NOSONAR
    expression = generate_expression(start, step, index)

    hidden_index = randint(0, index - 1)  # NOSONAR
    correct_answer = str(expression[hidden_index])
    expression_with_hidden = expression.copy()
    expression_with_hidden[hidden_index] = '..'
    question = ' '.join(map(str, expression_with_hidden))
    return question, correct_answer


def main():
    game_rule = 'What number is missing in the progression?'
    start_game(question_and_answer, game_rule, "Progression Game")