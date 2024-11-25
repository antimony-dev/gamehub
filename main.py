import pygame
import sys
from games import hangman, snake_game, tictactoe, guess_the_number, rock_paper_scissors, number_guessing, quiz_game, coin_toss, word_search, memory_game

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Game Collection")

# Colors
BACKGROUND_COLOR = (30, 30, 30)
BUTTON_COLOR = (0, 128, 255)
BUTTON_HOVER_COLOR = (0, 102, 204)
TEXT_COLOR = (255, 255, 255)

# Font
FONT = pygame.font.Font(None, 40)

# Button Class
class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.is_hovered = False

    def draw(self, screen):
        # Draw button with different colors based on hover state
        if self.is_hovered:
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, self.rect)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, self.rect)
        
        # Draw button text
        text_surface = FONT.render(self.text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        # Check if the mouse is over the button
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def check_click(self, mouse_pos):
        # Check if the mouse click is within the button area
        return self.rect.collidepoint(mouse_pos)

# Game Selection Menu
def display_home_screen():
    screen.fill(BACKGROUND_COLOR)

    # Define buttons for each game (Tic-Tac-Toe is added back)
    buttons = [
        Button("Hangman", 300, 50, 200, 50),
        Button("Tic-Tac-Toe", 300, 120, 200, 50),
        Button("Guess the Number", 300, 190, 200, 50),
        Button("Rock, Paper, Scissors", 300, 260, 200, 50),
        Button("Number Guessing", 300, 330, 200, 50),
        Button("Snake Game", 300, 400, 200, 50),
        Button("Quiz Game", 300, 470, 200, 50),
        Button("Coin Toss", 300, 540, 200, 50),
        Button("Word Search", 300, 610, 200, 50),
        Button("Memory Game", 300, 680, 200, 50),
        Button("Exit", 300, 750, 200, 50),
    ]

    # Draw all buttons
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
    return buttons

# Game Runner Function
def run_game(choice):
    if choice == "Hangman":
        hangman.play()
    elif choice == "Tic-Tac-Toe":
        tictactoe.play()  # This will call the Tic-Tac-Toe game
    elif choice == "Guess the Number":
        guess_the_number.play()
    elif choice == "Rock, Paper, Scissors":
        rock_paper_scissors.play()
    elif choice == "Number Guessing":
        number_guessing.play()
    elif choice == "Snake Game":
        snake_game.play()
    elif choice == "Quiz Game":
        quiz_game.play()
    elif choice == "Coin Toss":
        coin_toss.play()
    elif choice == "Word Search":
        word_search.play()
    elif choice == "Memory Game":
        memory_game.play()
    elif choice == "Exit":
        print("Thanks for playing! Goodbye.")
        pygame.quit()
        sys.exit()

# Main Game Loop
def main():
    running = True
    buttons = display_home_screen()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEMOTION:
                # Update hover state for each button
                for button in buttons:
                    button.check_hover(event.pos)

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if any button was clicked
                for button in buttons:
                    if button.check_click(event.pos):
                        # If the Exit button is clicked, quit the game
                        if button.text == "Exit":
                            running = False
                            pygame.quit()
                            sys.exit()

                        # Run the corresponding game
                        run_game(button.text)
                        
                        # After the game is finished, return to the menu
                        buttons = display_home_screen()

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Run the program
if __name__ == "__main__":
    main()
