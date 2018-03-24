import pygame
from paddle import Paddle

# Defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Constants
SCREEN_X = 1024
SCREEN_Y = 576

pygame.init()

# Set the width and height of the screen [width, height)
size = (SCREEN_X, SCREEN_Y)
screen = pygame.display.set_mode(size)

# Title bar text
pygame.display.set_caption("PyPong")

# Main game loop conditional
done = False

# Screen update
clock = pygame.time.Clock()

# Group of all sprites
all_sprites = pygame.sprite.Group()

player = Paddle()
comp = Paddle(SCREEN_X-20, SCREEN_Y-50)

all_sprites.add(player)
all_sprites.add(comp)

# Main game loop
while not done:
    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game logic

    # Clear the screen

    # update all_sprites
    all_sprites.update()

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    screen.fill(BLACK)

    # Drawing code

    # draw all_sprites group to the screen
    all_sprites.draw(screen)

    # Update the screen with the draw
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick(60)

# Quit
pygame.quit()
