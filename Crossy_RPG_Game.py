# Gain access to the pygame library
import pygame

# Size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Colors according to RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# Create the window of specified size in white to display the game
game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set the game window color to white
game_display.fill(WHITE_COLOR)

