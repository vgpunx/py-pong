import pygame
from constants import *
from ball import *
from player1 import *
from player2 import *


class Playfield:
    def __init__(self, size, ball, paddle1, paddle2):
        self.size = size
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.ball = ball
        self.paddle1 = paddle1
        self.paddle2 = paddle2

        # Position of the playfield
        self.position = ((DISPLAY_SIZE[0] - PLAYFIELD_SIZE[0]) / 2, DISPLAY_SIZE[1] - ((DISPLAY_SIZE[0] - PLAYFIELD_SIZE[0]) / 2) - PLAYFIELD_SIZE[1])

        # TODO: White for debug. Change to black when finished.
        self.image.fill(pygame.Color("WHITE"))

        self.all_sprites = pygame.sprite.Group(ball, paddle1, paddle2)

    def draw(self, surface):
        self.update()
        self.all_sprites.draw(self.image)

        # blit from self.image to upper left corner
        surface.blit(self.image, self.position)

    def update(self):
        self.all_sprites.update()
