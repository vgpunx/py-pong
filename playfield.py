import pygame
from constants import *
from ball import *
from paddle import *


class Playfield:
    def __init__(self, size):
        self.size = size
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.ball = Ball(self.rect)
        self.paddle1 = Paddle(20, PLAYFIELD_SIZE[1]/2)
        self.paddle2 = Paddle(PLAYFIELD_SIZE[0]-20, PLAYFIELD_SIZE[1]/2)

        # Position of the playfield based on DISPLAY_SIZE.
        self.position = ((DISPLAY_SIZE[0] - PLAYFIELD_SIZE[0]) / 2, DISPLAY_SIZE[1] - ((DISPLAY_SIZE[0] - PLAYFIELD_SIZE[0]) / 2) - PLAYFIELD_SIZE[1])

        self.all_sprites = pygame.sprite.Group(self.ball, self.paddle1, self.paddle2)

    def draw(self, surface):
        # TODO: Draw a green line around the playfield to visually show the playfield boundaries
        self.image.fill(pygame.Color('BLACK'))
        self.update()
        self.all_sprites.draw(self.image)

        # blit from self.image to self.position
        surface.blit(self.image, self.position)

    def update(self):
        self.all_sprites.update()
