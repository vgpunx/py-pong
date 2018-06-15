import pygame
from constants import *


class Scoreboard:
    def __init__(self, plfld_size):
        self.size = ((plfld_size[0] * 0.2), (plfld_size[1] * 0.13))
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()

        self.p1_score = 0
        self.p2_score = 0

        self.position = (((DISPLAY_SIZE[0] / 2) - (self.size[0] / 2)), DISPLAY_SIZE[1] * 0.01)

    def draw(self, surface):
        self.image.fill(pygame.Color('WHITE'))

        surface.blit(self.image, self.position)

    def p1_point(self):
        self.p1_score += 1

    def p2_point(self):
        self.p2_score += 1
