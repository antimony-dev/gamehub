import random

def play():
    print("Welcome to Number Guessing!")
    lower_bound = int(input("Enter the lower bound of the number range: "))
    upper_bound = int(input("Enter the upper bound of the number range: "))
    number = random.randint(lower_bound, upper_bound)
    attempts = 0
    while True:
        guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
        attempts += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
