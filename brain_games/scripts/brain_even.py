import random

def is_even(number):
    return number % 2 == 0

def play_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3): 
        number = random.randint(1, 100)
        correct_answer = 'yes' if is_even(number) else 'no'

        print(f"Question: {number}")
        user_answer = input('Your answer: ').strip().lower()

        if user_answer != correct_answer:
            return False, correct_answer

print(f"Congratulations, {name}!")

return True, None

if __name__ == '__main__':
    main()
