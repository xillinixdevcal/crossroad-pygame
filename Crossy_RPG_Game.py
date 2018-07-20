# Gain access to the pygame library
import pygame

# Display title
DISPLAY_TITLE = "Crossy RPG"

# Size of the display
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800

# Colors according to RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# Clock used to update game events and frames
clock = pygame.time.Clock()

class Game:
    # Typical rate of 60, equivalent to FPS
    TICK_RATE = 60
    

    # Initializer for the game class to set up the title, width, and height
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Create the window of specified size in white to display the game
        self.game_display = pygame.display.set_mode((width, height))
        # Set the game window color to white
        self.game_display.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False
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
            clock.tick(self.TICK_RATE)

# Initialize pygame
pygame.init()

new_game = Game(DISPLAY_TITLE, DISPLAY_WIDTH, DISPLAY_HEIGHT)
new_game.run_game_loop()

# Quit pygame and the program
pygame.quit()
quit()

# Load the player image from the file directory
# player_image = pygame.image.load('player.png')
# Scale the image up
# player_image = pygame.transform.scale(player_image, (50, 50))

# Draw a rectangle on top of the game display (x, y, width, height)
# pygame.draw.rect(game_display, BLACK_COLOR, [350, 350, 100, 100])
# Draw a circle on top of  the game display (x, y, radius)
# pygame.draw.circle(game_display, BLACK_COLOR, (400, 300), 50)

# Draw the player image on top of the screen at (x, y) position 
# game_display.blit(player_image, (375, 375))

