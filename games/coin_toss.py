import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen Dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Toss Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GOLD = (255, 215, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Fonts
font = pygame.font.Font(None, 50)

# Clock
clock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    """Helper function to draw text on the screen."""
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def coin_toss():
    """Simulates a coin toss."""
    return random.choice(["Heads", "Tails"])

def draw_coin(surface, text, x, y, size, color):
    """Draw a simple coin with text."""
    pygame.draw.circle(surface, color, (x, y), size)
    draw_text(text, font, WHITE, surface, x, y)

def game_loop():
    """Main Game Loop."""
    running = True
    result = None
    flipping = False
    flip_frames = 30
    current_frame = 0
    selected_side = None

    while running:
        screen.fill(WHITE)

        # Display Title
        draw_text("Coin Toss Game", font, BLACK, screen, WIDTH // 2, 50)

        # Draw buttons
        pygame.draw.rect(screen, BLUE, (150, 500, 200, 60))
        pygame.draw.rect(screen, GOLD, (450, 500, 200, 60))
        draw_text("Heads", font, WHITE, screen, 250, 530)
        draw_text("Tails", font, WHITE, screen, 550, 530)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not flipping:
                x, y = event.pos
                if 150 <= x <= 350 and 500 <= y <= 560:
                    selected_side = "Heads"
                    flipping = True
                elif 450 <= x <= 650 and 500 <= y <= 560:
                    selected_side = "Tails"
                    flipping = True

        # Coin flipping animation
        if flipping:
            current_frame += 1
            if current_frame % 2 == 0:
                coin_text = "Heads" if current_frame % 4 == 0 else "Tails"
            else:
                coin_text = "Flipping..."
            draw_coin(screen, coin_text, WIDTH // 2, HEIGHT // 2, 100, GOLD)

            if current_frame >= flip_frames:
                result = coin_toss()
                flipping = False
                current_frame = 0
        elif result:
            draw_coin(screen, result, WIDTH // 2, HEIGHT // 2, 100, GOLD)
            draw_text(f"Result: {result}", font, BLACK, screen, WIDTH // 2, 400)
            if selected_side:
                if selected_side == result:
                    draw_text("You Win!", font, GREEN, screen, WIDTH // 2, 450)
                else:
                    draw_text("You Lose!", font, RED, screen, WIDTH // 2, 450)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    game_loop()
