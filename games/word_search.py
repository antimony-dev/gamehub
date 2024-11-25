import random

def generate_word_search(word_list, size=10):
    grid = [[" " for _ in range(size)] for _ in range(size)]
    for word in word_list:
        placed = False
        while not placed:
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal':
                row = random.randint(0, size - 1)
                col = random.randint(0, size - len(word))
                if all(grid[row][col + i] == " " for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row][col + i] = word[i]
                    placed = True
            else:
                row = random.randint(0, size - len(word))
                col = random.randint(0, size - 1)
                if all(grid[row + i][col] == " " for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row + i][col] = word[i]
                    placed = True
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

def play():
    word_list = ["python", "java", "ruby", "javascript", "html", "css"]
    grid = generate_word_search(word_list)
    print("Welcome to Word Search!")
    print("Find the words in the grid.")
    print_grid(grid)

    found_words = set()
    while len(found_words) < len(word_list):
        print(f"Words found: {', '.join(found_words)}")
        word = input("Enter a word you found: ").lower()
        if word in word_list and word not in found_words:
            found_words.add(word)
            print(f"Good job! You found '{word}'.")
        else:
            print("Word not found or already discovered.")
    
    print("Congratulations! You found all the words!")
