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

    def draw_zero(self):
        # Draw a zero on the scoreboard
        zero_list = [(20, 10), ((self.size[0] / 4), 10), ((self.size[0] / 4), (self.size[1] - 10)),
                     (20, self.size[1] - 10), (20, 10)]
        # lines(Surface, color, closed, pointlist, width=1)
        pygame.draw.lines(self.image, pygame.Color('GREEN'), False, zero_list, 5)

    def draw(self, surface):
        self.image.fill(pygame.Color('WHITE'))
        self.draw_zero()

        surface.blit(self.image, self.position)
