from random import randint

from brain_games.scripts.engine import start_game


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def question_and_answer():
    number = randint(1, 100)  # NOSONAR
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer


def main():
    game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    start_game(question_and_answer, game_rule, "Prime Game")