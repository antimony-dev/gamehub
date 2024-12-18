import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Initialize the board
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(BG_COLOR)


def draw_lines():
    """Draw the grid lines."""
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_figures():
    """Draw the circles and crosses."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(
                    screen,
                    CIRCLE_COLOR,
                    (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                    CIRCLE_RADIUS,
                    CIRCLE_WIDTH,
                )
            elif board[row][col] == 2:
                pygame.draw.line(
                    screen,
                    CROSS_COLOR,
                    (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                    (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                    CROSS_WIDTH,
                )
                pygame.draw.line(
                    screen,
                    CROSS_COLOR,
                    (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                    (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                    CROSS_WIDTH,
                )


def mark_square(row, col, player):
    """Mark the square for the player."""
    board[row][col] = player


def available_square(row, col):
    """Check if the square is available."""
    return board[row][col] == 0


def is_full():
    """Check if the board is full."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


def check_win(player):
    """Check if the player has won."""
    # Vertical win
    for col in range(BOARD_COLS):
        if all(board[row][col] == player for row in range(BOARD_ROWS)):
            draw_vertical_winning_line(col, player)
            return True

    # Horizontal win
    for row in range(BOARD_ROWS):
        if all(board[row][col] == player for col in range(BOARD_COLS)):
            draw_horizontal_winning_line(row, player)
            return True

    # Descending diagonal win
    if all(board[i][i] == player for i in range(BOARD_ROWS)):
        draw_desc_diagonal(player)
        return True

    # Ascending diagonal win
    if all(board[i][BOARD_ROWS - i - 1] == player for i in range(BOARD_ROWS)):
        draw_asc_diagonal(player)
        return True

    return False


def draw_vertical_winning_line(col, player):
    """Draw a vertical winning line."""
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(
        screen,
        color,
        (col * SQUARE_SIZE + SQUARE_SIZE // 2, 15),
        (col * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - 15),
        LINE_WIDTH,
    )


def draw_horizontal_winning_line(row, player):
    """Draw a horizontal winning line."""
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(
        screen,
        color,
        (15, row * SQUARE_SIZE + SQUARE_SIZE // 2),
        (WIDTH - 15, row * SQUARE_SIZE + SQUARE_SIZE // 2),
        LINE_WIDTH,
    )


def draw_desc_diagonal(player):
    """Draw a descending diagonal winning line."""
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), LINE_WIDTH)


def draw_asc_diagonal(player):
    """Draw an ascending diagonal winning line."""
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), LINE_WIDTH)


def restart():
    """Restart the game."""
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


draw_lines()

# Main loop
player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x-coordinate
            mouseY = event.pos[1]  # y-coordinate

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = 3 - player  # Switch player (1 -> 2, 2 -> 1)
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
                player = 1

    pygame.display.update()
