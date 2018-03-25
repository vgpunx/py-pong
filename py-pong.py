from constants import *
from player1 import *
from player2 import *
from ball import *

pygame.init()

# Set the width and height of the screen [width, height)
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

# Title bar text
pygame.display.set_caption("PyPong")

# Main game loop conditional
done = False

# Screen update
clock = pygame.time.Clock()

# Group of all sprites
all_sprites = pygame.sprite.Group()

player1 = Player1()
player2 = Player2()
ball = Ball()

all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(ball)

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

    # check if ball hit the paddle
    collision1 = pygame.sprite.collide_rect(player1, ball)
    if collision1:
        ball.speedx = 3

    collision2 = pygame.sprite.collide_rect(ball, player2)
    if collision2:
        ball.speedx = -3




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
