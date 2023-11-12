from ast import operator
import random


def generate_function_integer(min, max):
    """
    Generate a Random integer between min and max.
    """
    return random.randint(min, max)


def generate_random_operator():
    """
    Generate a random operator : '+', '-', '*'
    """
    return random.choice(['+', '-', '*'])


def result(num1, num2, operator):
    """
    calculate the result of the operation
    """
    
    if operator == '-': 
        result = num1 - num2
    elif operator == '+': 
        result = num1 + num2
    else:
        result = num1 * num2
    return result

def math_quiz():
    """
    Main function for math quiz
    """
    point = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    try:
        for _ in range(t_q):
            num1 = generate_function_integer(1, 10)
            num2 = generate_function_integer(1, 5.5)
            operator = generate_random_operator()

            problem, answer = result(num1,num2,operator)

            print(f"\nQuestion: {problem}")
            user_answer = int(input("Your answer: "))
        

            if user_answer == answer:
                print("Correct! You earned a point.")
                point += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")

        print(f"\nGame over! Your score is: {point}/{t_q}")

    except ValueError:
        print("Error: Invalid input")

if __name__ == "__main__":
    math_quiz()
