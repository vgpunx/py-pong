import pygame
from constants import *


# This is the paddle class.
class Player2(pygame.sprite.Sprite):
    # paddle sprite
    def __init__(self, x=20, y=50):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))  # What the sprite looks like
        self.image.fill(pygame.Color("green"))  # fill the Surface with the color Green
        self.rect = self.image.get_rect()   # The rectangle that encloses the sprite
        self.rect.center = (PLAYFIELD_SIZE[0]-20, PLAYFIELD_SIZE[1]/2)
        self.speedy = 0

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5

        self.rect.y += self.speedy

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > PLAYFIELD_SIZE[1]:
            self.rect.bottom = PLAYFIELD_SIZE[1]
