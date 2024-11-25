import random

def display_hangman(tries):
    stages = ["""
                   -----
                  |     |
                        |
                        |
                        |
                        |
                ------
                """, """
                   -----
                  |     |
                  O     |
                        |
                        |
                        |
                ------
                """, """
                   -----
                  |     |
                  O     |
                  |     |
                        |
                        |
                ------
                """, """
                   -----
                  |     |
                  O     |
                 /|     |
                        |
                        |
                ------
                """, """
                   -----
                  |     |
                  O     |
                 /|\\    |
                        |
                        |
                ------
                """, """
                   -----
                  |     |
                  O     |
                 /|\\    |
                 /      |
                        |
                ------
                """, """
                   -----
                  |     |
                  O     |
                 /|\\    |
                 / \\    |
                        |
                ------
                """]
    return stages[tries]

def play():
    word_list = ["python", "java", "kotlin", "javascript", "html", "css"]
    word = random.choice(word_list)
    word_display = ["_"] * len(word)
    guessed_letters = set()
    tries = 0
    max_tries = 6

    print("Welcome to Hangman!")
    
    while tries < max_tries:
        print(display_hangman(tries))
        print("Word: " + " ".join(word_display))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try again.")
            continue
        
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess
            if "".join(word_display) == word:
                print("Congratulations! You've guessed the word correctly.")
                break
        else:
            tries += 1
            print(f"Sorry! '{guess}' is not in the word.")
    else:
        print(display_hangman(tries))
        print(f"Sorry, you lost. The word was '{word}'.")
