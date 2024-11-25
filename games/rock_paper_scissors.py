import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Fonts
font_large = pygame.font.SysFont("arial", 50)
font_small = pygame.font.SysFont("arial", 30)

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Utility Functions
def draw_text(text, font, color, center_x, center_y):
    """Draws centered text on the screen."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(center_x, center_y))
    screen.blit(text_surface, text_rect)

def determine_winner(player, computer):
    """Determines the winner based on player and computer choices."""
    if player == computer:
        return "Tie"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "Player"
    else:
        return "Computer"

# Game Function
def play():
    running = True
    player_choice = None
    computer_choice = None
    winner = None

    while running:
        screen.fill(WHITE)

        # Draw Title
        draw_text("Rock, Paper, Scissors", font_large, BLUE, WIDTH // 2, 80)

        # Draw Buttons
        pygame.draw.rect(screen, GRAY, (150, 300, 150, 60))  # Rock
        pygame.draw.rect(screen, GRAY, (325, 300, 150, 60))  # Paper
        pygame.draw.rect(screen, GRAY, (500, 300, 150, 60))  # Scissors
        draw_text("Rock", font_small, BLACK, 225, 330)
        draw_text("Paper", font_small, BLACK, 400, 330)
        draw_text("Scissors", font_small, BLACK, 575, 330)

        # Display Choices
        if player_choice:
            draw_text(f"Player: {player_choice}", font_small, GREEN, WIDTH // 4, 450)
        if computer_choice:
            draw_text(f"Computer: {computer_choice}", font_small, RED, WIDTH * 3 // 4, 450)

        # Display Winner
        if winner:
            draw_text(f"Winner: {winner}", font_large, DARK_GRAY, WIDTH // 2, 520)

        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Detect button clicks
                if 150 <= x <= 300 and 300 <= y <= 360:
                    player_choice = "Rock"
                elif 325 <= x <= 475 and 300 <= y <= 360:
                    player_choice = "Paper"
                elif 500 <= x <= 650 and 300 <= y <= 360:
                    player_choice = "Scissors"

                if player_choice:
                    computer_choice = random.choice(choices)
                    winner = determine_winner(player_choice, computer_choice)

        pygame.display.flip()

# Run the game
if __name__ == "__main__":
    play()
