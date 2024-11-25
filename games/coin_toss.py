import random

def play():
    print("Welcome to Coin Toss!")
    while True:
        user_choice = input("Choose 'heads' or 'tails' (or 'quit' to exit): ").lower()
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        if user_choice not in ['heads', 'tails']:
            print("Invalid choice! Please choose 'heads' or 'tails'.")
            continue
        
        toss_result = random.choice(['heads', 'tails'])
        print(f"The coin landed on: {toss_result}")
        
        if user_choice == toss_result:
            print("You win!")
        else:
            print("You lose!")
