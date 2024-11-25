import sys
from games import hangman, tictactoe, guess_the_number, rock_paper_scissors, number_guessing, calculator, quiz_game, coin_toss, word_search, memory_game

def display_home_screen():
    print("Welcome to the Python Game Collection!")
    print("Please select a game to play:")
    print("1. Hangman")
    print("2. Tic-Tac-Toe")
    print("3. Guess the Number")
    print("4. Rock, Paper, Scissors")
    print("5. Number Guessing")
    print("6. Calculator")
    print("7. Quiz Game")
    print("8. Coin Toss")
    print("9. Word Search")
    print("10. Memory Game")
    print("0. Exit")

def run_game(choice):
    if choice == '1':
        hangman.play()
    elif choice == '2':
        tictactoe.play()
    elif choice == '3':
        guess_the_number.play()
    elif choice == '4':
        rock_paper_scissors.play()
    elif choice == '5':
        number_guessing.play()
    elif choice == '6':
        calculator.play()
    elif choice == '7':
        quiz_game.play()
    elif choice == '8':
        coin_toss.play()
    elif choice == '9':
        word_search.play()
    elif choice == '10':
        memory_game.play()
    elif choice == '0':
        print("Thanks for playing! Goodbye.")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")

def main():
    while True:
        display_home_screen()
        user_choice = input("Enter the number of the game you'd like to play: ")
        run_game(user_choice)

if __name__ == "__main__":
    main()
