import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1200, 660  # Adjusted screen height
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (220, 220, 220)

# Fonts
FONT_LARGE = pygame.font.Font(None, 80)
FONT_MEDIUM = pygame.font.Font(None, 60)
FONT_SMALL = pygame.font.Font(None, 40)

# Game constants
MAX_WRONG_GUESSES = 6

# Word categories
WORDS = {
    "Fruits": ["apple", "banana", "orange", "grape", "kiwi"],
    "Animals": ["tiger", "lion", "elephant", "zebra", "giraffe"],
    "Countries": ["india", "china", "brazil", "france", "japan"],
}

# Functions for drawing the hangman
def draw_hangman(stage):
    """Draw the hangman step-by-step depending on the stage."""
    # Adjusted base_x for 0.5 cm left, and base_y for 1 cm up
    base_x, base_y = 50 - 19, HEIGHT - 60 - 38
    
    # Base
    pygame.draw.line(screen, BLACK, (base_x - 100, base_y), (base_x + 100, base_y), 5)
    
    # Pole
    pygame.draw.line(screen, BLACK, (base_x, base_y), (base_x, base_y - 400), 5)
    
    # Shortened top bar (by 2 cm or 76 pixels)
    pygame.draw.line(screen, BLACK, (base_x, base_y - 400), (base_x + 124, base_y - 400), 5)  # Adjusted length
    
    # Rope
    pygame.draw.line(screen, BLACK, (base_x + 124, base_y - 400), (base_x + 124, base_y - 350), 5)

    if stage >= 1:  # Head
        pygame.draw.circle(screen, BLACK, (base_x + 124, base_y - 300), 50, 5)
    if stage >= 2:  # Body
        pygame.draw.line(screen, BLACK, (base_x + 124, base_y - 250), (base_x + 124, base_y - 100), 5)
    if stage >= 3:  # Left arm
        pygame.draw.line(screen, BLACK, (base_x + 124, base_y - 200), (base_x + 74, base_y - 150), 5)
    if stage >= 4:  # Right arm
        pygame.draw.line(screen, BLACK, (base_x + 124, base_y - 200), (base_x + 174, base_y - 150), 5)
    if stage >= 5:  # Left leg
        pygame.draw.line(screen, BLACK, (base_x + 124, base_y - 100), (base_x + 74, base_y), 5)
    if stage >= 6:  # Right leg
        pygame.draw.line(screen, BLACK, (base_x + 124, base_y - 100), (base_x + 174, base_y), 5)


# Game logic
class HangmanGame:
    def __init__(self):
        self.category = random.choice(list(WORDS.keys()))
        self.word = random.choice(WORDS[self.category]).upper()
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.keyboard_colors = {chr(i): GRAY for i in range(65, 91)}  # A-Z
        self.key_positions = {}  # To store the positions of keys for mouse clicks

    def get_display_word(self):
        """Get the word with unguessed letters replaced by underscores."""
        return " ".join([char if char in self.guessed_letters else "_" for char in self.word])

    def guess_letter(self, letter):
        """Check the guessed letter and update the game state."""
        letter = letter.upper()
        if letter in self.guessed_letters:
            return False, "Already guessed!"
        self.guessed_letters.add(letter)
        if letter not in self.word:
            self.wrong_guesses += 1
            self.keyboard_colors[letter] = RED
            return False, "Incorrect guess!"
        self.keyboard_colors[letter] = GREEN
        return True, "Correct guess!"

    def is_game_over(self):
        """Check if the game is over."""
        return self.wrong_guesses >= MAX_WRONG_GUESSES or "_" not in self.get_display_word()

    def is_winner(self):
        """Check if the player has won."""
        return "_" not in self.get_display_word()


# Draw game state
def draw_game_state(game):
    """Render the game state on the screen."""
    # Display category with background box
    pygame.draw.rect(screen, LIGHT_GRAY, (50, 20, 300, 50))
    category_text = FONT_SMALL.render(f"Category: {game.category}", True, BLUE)
    screen.blit(category_text, (60, 30))

    # Display word with new position
    word_text = FONT_LARGE.render(game.get_display_word(), True, BLACK)
    # Shift word 1 cm to the right (38 pixels) and 2 cm downwards (76 pixels)
    screen.blit(word_text, (WIDTH // 2 - word_text.get_width() // 2 + 38, 150 + 76))

    # Draw the hangman
    draw_hangman(game.wrong_guesses)


def draw_keyboard(game):
    """Draw an on-screen keyboard with rounded keys."""
    keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x_start, y_start = 207, HEIGHT - 138  # Further shifted by 0.5 cm right and 1 cm up
    key_width, key_height = 60, 60
    gap = 15

    for i, key in enumerate(keys):
        x = x_start + (key_width + gap) * (i % 13)
        y = y_start + (key_height + gap) * (i // 13)
        color = game.keyboard_colors[key]
        pygame.draw.rect(screen, color, (x, y, key_width, key_height), border_radius=10)
        pygame.draw.rect(screen, BLACK, (x, y, key_width, key_height), 2, border_radius=10)  # Border
        text = FONT_SMALL.render(key, True, BLACK)
        screen.blit(text, (x + key_width // 4, y + key_height // 4))

        # Store key positions for click detection
        game.key_positions[key] = pygame.Rect(x, y, key_width, key_height)


def main():
    """Main game loop."""
    game = HangmanGame()
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)  # Clear the screen

        # Draw the game state and keyboard
        draw_game_state(game)
        draw_keyboard(game)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha() and len(event.unicode) == 1:
                    game.guess_letter(event.unicode)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for key, rect in game.key_positions.items():
                    if rect.collidepoint(mouse_pos):
                        game.guess_letter(key)

            if game.is_game_over():
                # Game over logic
                if game.is_winner():
                    result_text = FONT_LARGE.render("You Win!", True, GREEN)
                else:
                    result_text = FONT_LARGE.render(f"You Lose! Word: {game.word}", True, RED)
                screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, 400))
                pygame.display.flip()
                pygame.time.wait(3000)  # Pause for 3 seconds
                main()  # Restart the game

        # Update the display
        pygame.display.flip()
        clock.tick(30)  # 30 FPS

if __name__ == "__main__":
    main()
