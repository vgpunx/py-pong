import pygame
from constants import *
from pygame.math import Vector2 as vec


# This is the paddle class.
class Paddle(pygame.sprite.Sprite):
    # paddle sprite
    def __init__(self, x, y):
        """
        :param x: int
        :param y: int
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))  # What the sprite looks like
        self.image.fill(pygame.Color('WHITE'))  # fill the Surface with the color Green
        self.rect = self.image.get_rect()   # The rectangle that encloses the sprite
        self.rect.center = (x, y)
        self.speed = 7

    def get_location(self):
        current_position = vec(self.rect.center[0], self.rect.center[1])
        return current_position

    def get_rect(self):
        return self.rect

    def move_up(self):
        self.rect.move_ip(0, -self.speed)

    def move_down(self):
        self.rect.move_ip(0, self.speed)

    def update(self):

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > PLAYFIELD_SIZE[1]:
            self.rect.bottom = PLAYFIELD_SIZE[1]
