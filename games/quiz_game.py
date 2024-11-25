import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
GREEN = (34, 139, 34)
RED = (220, 20, 60)

# Fonts
FONT = pygame.font.Font(None, 36)
LARGE_FONT = pygame.font.Font(None, 48)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Quiz Game")

# Questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": 2,
    },
    {
        "question": "Which programming language is named after a snake?",
        "options": ["Java", "Python", "Ruby", "C++"],
        "answer": 1,
    },
    {
        "question": "What is 5 + 3?",
        "options": ["5", "8", "10", "15"],
        "answer": 1,
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 1,
    },
    {
        "question": "Which gas do plants primarily use during photosynthesis?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"],
        "answer": 1,
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"],
        "answer": 1,
    },
    {
        "question": "In which year did the Titanic sink?",
        "options": ["1905", "1912", "1920", "1935"],
        "answer": 1,
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "options": ["Avocado", "Tomato", "Lime", "Cucumber"],
        "answer": 0,
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Pablo Picasso", "Van Gogh", "Michelangelo"],
        "answer": 0,
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Osmium", "Oxygen", "Oxide", "Oganesson"],
        "answer": 1,
    },
]

# Helper function to render text
def render_text(text, font, color, x, y, center=True):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# Main game loop
def play():
    running = True
    question_index = 0
    score = 0
    selected_option = -1  # Store the index of the selected option

    while running:
        screen.fill(WHITE)

        # Display the current question
        current_question = questions[question_index]
        render_text(f"Question {question_index + 1} of {len(questions)}", LARGE_FONT, BLACK, SCREEN_WIDTH // 2, 50)
        render_text(current_question["question"], FONT, BLACK, SCREEN_WIDTH // 2, 120)

        # Display the options
        option_y_start = 200
        option_spacing = 80
        mouse_x, mouse_y = pygame.mouse.get_pos()
        option_rects = []

        for i, option in enumerate(current_question["options"]):
            option_rect = pygame.Rect(100, option_y_start + i * option_spacing, 600, 50)
            option_rects.append(option_rect)
            color = BLUE if i == selected_option else BLACK
            pygame.draw.rect(screen, color, option_rect, border_radius=10)
            render_text(option, FONT, WHITE, option_rect.centerx, option_rect.centery)

        # Submit button
        submit_button = pygame.Rect(300, 500, 200, 50)
        pygame.draw.rect(screen, GREEN, submit_button, border_radius=10)
        render_text("Submit", FONT, WHITE, submit_button.centerx, submit_button.centery)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(event.pos):
                        selected_option = i
                if submit_button.collidepoint(event.pos):
                    if selected_option == current_question["answer"]:
                        score += 1
                    question_index += 1
                    selected_option = -1

                    # End the game if all questions are answered
                    if question_index >= len(questions):
                        running = False

        pygame.display.flip()

    # Display the final score
    screen.fill(WHITE)
    render_text("Quiz Complete!", LARGE_FONT, BLACK, SCREEN_WIDTH // 2, 200)
    render_text(f"Your Score: {score} / {len(questions)}", FONT, BLACK, SCREEN_WIDTH // 2, 300)
    pygame.display.flip()

    pygame.time.wait(3000)

# Run the game
if __name__ == "__main__":
    play()
