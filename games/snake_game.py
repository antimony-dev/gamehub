import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
BLOCK_SIZE = 20

# Colors
BACKGROUND_COLOR = (30, 30, 30)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 255, 255)

# Fonts
FONT = pygame.font.Font(None, 36)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()


def display_message(message, score):
    """Display a message in the center of the screen."""
    screen.fill(BACKGROUND_COLOR)
    game_over_surface = FONT.render(message, True, TEXT_COLOR)
    score_surface = FONT.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(game_over_surface, (SCREEN_WIDTH // 2 - game_over_surface.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(score_surface, (SCREEN_WIDTH // 2 - score_surface.get_width() // 2, SCREEN_HEIGHT // 2 + 10))
    pygame.display.flip()
    pygame.time.wait(3000)


def play():
    """Main game loop."""
    # Initialize game variables
    snake = [[100, 100]]
    direction = "RIGHT"
    food = [random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE), random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE)]
    score = 0
    running = True

    while running:
        screen.fill(BACKGROUND_COLOR)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quitting the game.")  # Debugging print
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # Move snake
        head = snake[0].copy()
        if direction == "UP":
            head[1] -= BLOCK_SIZE
        elif direction == "DOWN":
            head[1] += BLOCK_SIZE
        elif direction == "LEFT":
            head[0] -= BLOCK_SIZE
        elif direction == "RIGHT":
            head[0] += BLOCK_SIZE
        snake.insert(0, head)

        # Check collisions
        if head[0] < 0 or head[1] < 0 or head[0] >= SCREEN_WIDTH or head[1] >= SCREEN_HEIGHT or head in snake[1:]:
            display_message("Game Over", score)
            running = False
            continue

        # Check if food is eaten
        if head == food:
            score += 1
            food = [random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE), random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE)]
        else:
            snake.pop()

        # Draw food
        pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

        # Draw snake
        for block in snake:
            pygame.draw.rect(screen, SNAKE_COLOR, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

        # Display score
        score_surface = FONT.render(f"Score: {score}", True, TEXT_COLOR)
        screen.blit(score_surface, (10, 10))

        # Refresh screen
        pygame.display.flip()

        # Debugging print
        print(f"Snake Head: {head} Direction: {direction}")

        clock.tick(9)  # Slightly slower speed

    pygame.quit()
    sys.exit()

# Run the game
if __name__ == "__main__":
    play()
