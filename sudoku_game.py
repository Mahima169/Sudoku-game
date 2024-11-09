import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 540
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
FONT = pygame.font.Font(None, 40)
LINE_COLOR = (0, 0, 0)
CELL_COLOR = (255, 255, 255)
HIGHLIGHT_COLOR = (180, 200, 255)

# Create a basic 9x9 Sudoku grid (0 represents empty cells)
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# Copy of the grid to track changes by the player
original_grid = [row[:] for row in grid]

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")


# Function to draw the grid and numbers
def draw_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, CELL_COLOR, rect)
            pygame.draw.rect(screen, LINE_COLOR, rect, 1)

            if grid[row][col] != 0:
                text = FONT.render(str(grid[row][col]), True, LINE_COLOR)
                screen.blit(text, (col * CELL_SIZE + 20, row * CELL_SIZE + 10))

    # Draw thicker lines for 3x3 grid separation
    for i in range(0, GRID_SIZE + 1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 3)
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 3)


# Function to highlight a selected cell
def highlight_cell(row, col):
    rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, HIGHLIGHT_COLOR, rect)


# Main loop
running = True
selected_cell = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            x, y = event.pos
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            if original_grid[row][col] == 0:  # Only allow selection of empty cells
                selected_cell = (row, col)
        elif event.type == pygame.KEYDOWN and selected_cell:
            row, col = selected_cell
            if pygame.K_1 <= event.key <= pygame.K_9:  # Numbers 1-9
                number = event.key - pygame.K_0
                grid[row][col] = number  # Set the number entered by the user

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the grid and highlight the selected cell
    draw_grid()
    if selected_cell:
        highlight_cell(*selected_cell)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
