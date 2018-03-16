import pygame
from paddle import draw_paddle

# Defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height)
size = (1280, 720)
screen = pygame.display.set_mode(size)

# Title bar text
pygame.display.set_caption("PyPong")

# Main game loop conditional
done = False

# Screen update
clock = pygame.time.Clock()

# Main game loop
while not done:
    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game logic

    # Clear the screen

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    screen.fill(BLACK)

    # Drawing code
    draw_paddle(screen, 15, 15)

    # Update the screen with the draw
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick(60)

# Quit
pygame.quit()