# Gain access to the pygame library
import pygame

# Initialize pygame
pygame.init()

# Size of the screen
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800

# Display title
DISPLAY_TITLE = "Crossy RPG"

# Colors according to RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# Clock used to update game events and frames
clock = pygame.time.Clock()

# Typical rate of 60, equivalent to FPS
TICK_RATE = 60
is_game_over = False

# Create the window of specified size in white to display the game
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
# Set the game window color to white
game_display.fill(WHITE_COLOR)
pygame.display.set_caption(DISPLAY_TITLE)

# Main game loop, used to update all gameplay such as movement, checks, and graphics
# Runs until is_game_over = True
while not is_game_over:
    # A loop to get all of the events occuring at any given time
    # Events are most often mouse movement, mouse and button clicks, or exit events
    for event in pygame.event.get():
        # If we have a quite type event (exit out) then exit out of the game loop
        if event.type == pygame.QUIT:
            is_game_over = True
        
        print(event)

    # Update all game graphics
    pygame.display.update()
    # Tick the clock to update everything within the game
    clock.tick(TICK_RATE)

# Quit pygame and the program
pygame.quit()
quit()