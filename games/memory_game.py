import random

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def play():
    print("Welcome to Memory Game!")
    deck = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    deck = shuffle_deck(deck * 2)  # Two sets of each card for matching
    
    revealed_cards = ["*"] * len(deck)
    attempts = 0
    matches = 0
    
    while matches < len(deck) // 2:
        print("Cards:", " ".join(revealed_cards))
        try:
            first_choice = int(input("Select the first card (1-16): ")) - 1
            second_choice = int(input("Select the second card (1-16): ")) - 1
        except ValueError:
            print("Invalid input. Try again.")
            continue
        
        if first_choice == second_choice or revealed_cards[first_choice] != "*" or revealed_cards[second_choice] != "*":
            print("Invalid choice, try again.")
            continue
        
        revealed_cards[first_choice] = deck[first_choice]
        revealed_cards[second_choice] = deck[second_choice]
        print("Cards:", " ".join(revealed_cards))

        if deck[first_choice] == deck[second_choice]:
            matches += 1
            print(f"Match found! {deck[first_choice]} == {deck[second_choice]}")
        else:
            print(f"No match! {deck[first_choice]} != {deck[second_choice]}")
            revealed_cards[first_choice] = "*"
            revealed_cards[second_choice] = "*"
        
        attempts += 1
        if matches == len(deck) // 2:
            print(f"Congratulations! You found all matches in {attempts} attempts.")
