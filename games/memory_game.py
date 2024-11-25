import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions and grid configuration
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 4  # 4x4 grid
CARD_SIZE = SCREEN_WIDTH // GRID_SIZE
PADDING = 10
FPS = 30

# Colors
BACKGROUND_COLOR = (30, 30, 60)
CARD_COLOR = (50, 150, 250)
REVEALED_COLOR = (250, 100, 100)
TEXT_COLOR = (255, 255, 255)

# Create the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Game")

# Font
font = pygame.font.Font(None, 60)


def create_grid():
    """Creates a shuffled grid of pairs."""
    total_cards = GRID_SIZE * GRID_SIZE
    values = list(range(1, total_cards // 2 + 1)) * 2
    random.shuffle(values)
    return [values[i * GRID_SIZE:(i + 1) * GRID_SIZE] for i in range(GRID_SIZE)]


def draw_grid(grid, revealed):
    """Draws the grid of cards."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * CARD_SIZE + PADDING
            y = row * CARD_SIZE + PADDING
            rect = pygame.Rect(x, y, CARD_SIZE - PADDING, CARD_SIZE - PADDING)
            if revealed[row][col]:
                pygame.draw.rect(screen, REVEALED_COLOR, rect)
                text = font.render(str(grid[row][col]), True, TEXT_COLOR)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
            else:
                pygame.draw.rect(screen, CARD_COLOR, rect)


def get_card_at_pos(pos):
    """Returns the grid position (row, col) based on mouse click position."""
    x, y = pos
    col = x // CARD_SIZE
    row = y // CARD_SIZE
    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
        return row, col
    return None


def play():
    # Grid and game state
    grid = create_grid()
    revealed = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
    first_card = None
    matches = 0

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BACKGROUND_COLOR)
        draw_grid(grid, revealed)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                card_pos = get_card_at_pos(event.pos)
                if card_pos and not revealed[card_pos[0]][card_pos[1]]:
                    if first_card is None:
                        first_card = card_pos
                        revealed[first_card[0]][first_card[1]] = True
                    else:
                        revealed[card_pos[0]][card_pos[1]] = True
                        pygame.time.wait(500)  # Delay for match feedback
                        if grid[first_card[0]][first_card[1]] == grid[card_pos[0]][card_pos[1]]:
                            matches += 1
                        else:
                            revealed[first_card[0]][first_card[1]] = False
                            revealed[card_pos[0]][card_pos[1]] = False
                        first_card = None

        if matches == (GRID_SIZE * GRID_SIZE) // 2:
            screen.fill(BACKGROUND_COLOR)
            win_text = font.render("You Win!", True, TEXT_COLOR)
            screen.blit(win_text, win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

        clock.tick(FPS)

    pygame.quit()
