import pygame
from constants import *


# This is the paddle class.
class Paddle(pygame.sprite.Sprite):
    # paddle sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))  # What the sprite looks like
        self.image.fill(pygame.Color('GREEN'))  # fill the Surface with the color Green
        self.rect = self.image.get_rect()   # The rectangle that encloses the sprite
        self.rect.center = (x, y)
        self.speedy = 0

    def move_up(self):
        self.speedy = -5

    def move_down(self):
        self.speedy = 5

    def update(self):
        self.rect.y += self.speedy

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > PLAYFIELD_SIZE[1]:
            self.rect.bottom = PLAYFIELD_SIZE[1]

        self.speedy = 0
