import random

def generate_expression():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    expression = f"{num1} {operation} {num2}"
    return expression

def calculate_answer(expression):
    return eval(expression) 

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('What is the result of the expression?')

    score = 0
    rounds = 3

    for _ in range(rounds):
        expression = generate_expression() 
        print(f"Question: {expression}")
        user_answer = input('Your answer: ') 
        correct_answer = calculate_answer(expression)

        if str(user_answer) != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  
        
        print("Correct!")
        score += 1

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()