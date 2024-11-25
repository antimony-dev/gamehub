import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font_large = pygame.font.Font(None, 74)
font_medium = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 32)

# Game variables
number_to_guess = random.randint(1, 100)
guess = None
feedback = ""
attempts = 0
input_text = ""

def draw_text(text, font, color, x, y, center=True):
    """Utility function to draw text."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def game_loop():
    global input_text, feedback, guess, attempts, number_to_guess
    running = True

    while running:
        screen.fill(WHITE)

        # Title
        draw_text("Guess the Number!", font_large, BLUE, WIDTH // 2, 50)

        # Instructions
        draw_text("I'm thinking of a number between 1 and 100.", font_medium, BLACK, WIDTH // 2, 150)
        draw_text("Enter your guess below:", font_small, GRAY, WIDTH // 2, 200)

        # Input box
        input_box = pygame.Rect(WIDTH // 2 - 100, 250, 200, 50)
        pygame.draw.rect(screen, GRAY, input_box, border_radius=5)
        draw_text(input_text, font_medium, BLACK, input_box.centerx, input_box.centery)

        # Feedback
        if feedback:
            color = GREEN if "correct" in feedback.lower() else RED
            draw_text(feedback, font_medium, color, WIDTH // 2, 350)

        # Attempts count
        draw_text(f"Attempts: {attempts}", font_small, BLACK, 10, 10, center=False)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Submit guess
                    if input_text.isdigit():
                        guess = int(input_text)
                        attempts += 1
                        if guess < number_to_guess:
                            feedback = "Too low! Try again."
                        elif guess > number_to_guess:
                            feedback = "Too high! Try again."
                        else:
                            feedback = f"Correct! The number was {number_to_guess}."
                            running = False
                    else:
                        feedback = "Please enter a valid number!"
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:  # Handle backspace
                    input_text = input_text[:-1]
                elif event.unicode.isdigit():  # Add typed character to input
                    input_text += event.unicode

        # Update the display
        pygame.display.flip()

    # End screen
    end_game_screen()

def end_game_screen():
    global number_to_guess, attempts
    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Game Over!", font_large, BLUE, WIDTH // 2, 100)
        draw_text(f"The number was {number_to_guess}.", font_medium, BLACK, WIDTH // 2, 200)
        draw_text(f"You guessed it in {attempts} attempts.", font_medium, BLACK, WIDTH // 2, 300)
        draw_text("Press R to play again or Q to quit.", font_small, GRAY, WIDTH // 2, 400)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart game
                    reset_game()
                    return
                elif event.key == pygame.K_q:  # Quit game
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

def reset_game():
    """Reset game variables for a new round."""
    global number_to_guess, guess, feedback, attempts, input_text
    number_to_guess = random.randint(1, 100)
    guess = None
    feedback = ""
    attempts = 0
    input_text = ""
    game_loop()

if __name__ == "__main__":
    game_loop()
