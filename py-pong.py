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
playfield = Playfield(PLAYFIELD_SIZE)

# Main game loop
while not done:
    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.event.pump()

    # I see a white screen and I want it painted black
    screen.fill(BLACK)

    # draw the playfield to the screen
    playfield.update()
    playfield.draw(screen)

    # Input checks
    # Check for player 1 inputs
    key_state = pygame.key.get_pressed()
    if key_state[pygame.K_w]:
        playfield.paddle1.move_up()
    if key_state[pygame.K_s]:
        playfield.paddle1.move_down()

    # Check for player 2 inputs
    if key_state[pygame.K_UP]:
        playfield.paddle2.move_up()
    if key_state[pygame.K_DOWN]:
        playfield.paddle2.move_down()

    # Check for space bar to start the round if needed
    if key_state[pygame.K_SPACE] and not playfield.ball.in_play:
        playfield.ball.start_round()

    # Update the screen with the draw
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick(60)

# Quit
pygame.quit()
