import random
import prompt

def is_even(number):
    return number % 2 == 0

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')

    correct_answers = 0

    while correct_answers < 3:
        number = random.randint(1, 1000)
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()

        correct_answer_str = "yes" if is_even(number) else "no"

        if answer == correct_answer_str:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer_str}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
