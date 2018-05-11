from constants import *
import pygame
from playfield import *


pygame.init()

# Set the width and height of the screen [width, height)
screen = pygame.display.set_mode(DISPLAY_SIZE)

# Title bar text
pygame.display.set_caption("PyPong")

# Main game loop conditional
done = False

# Screen update
clock = pygame.time.Clock()

# Instantiate objects
ball = Ball(pygame.Surface(PLAYFIELD_SIZE).get_rect())
playfield = Playfield(PLAYFIELD_SIZE, ball)

# Main game loop
while not done:
    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Check for player inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playfield.paddle1.move_up()
            if event.key == pygame.K_s:
                playfield.paddle1.move_down()

    # Clear the screen

    # update all_sprites


    # If you want a background image, replace this clear with blit'ing the
    # background image.

    screen.fill(BLACK)

    # Drawing code

    # draw the playfield to the screen
    playfield.draw(screen)

    # draw all_sprites group to the screen
    # all_sprites.draw(screen)

    # Update the screen with the draw
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick(60)

# Quit
pygame.quit()
