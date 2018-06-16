from scoreboardnumeral import *
from playfield import *


class Scoreboard:
    def __init__(self, plfld_size):
        self.size = ((plfld_size[0] * 0.2), (plfld_size[1] * 0.13))
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()

        self.p1_score = 0
        self.p2_score = 0

        self.position = (((DISPLAY_SIZE[0] / 2) - (self.size[0] / 2)), DISPLAY_SIZE[1] * 0.01)

        # instantiate numerals
        self.numerals = pygame.sprite.Group()
        self.p1_score_ones = ScoreboardNumeral(self.size[1], 'WHITE', 'BLACK', self.numerals)
        self.p2_score_ones = ScoreboardNumeral(self.size[1], 'WHITE', 'BLACK', self.numerals)

        self.p1_score_ones.rect.topleft = self.rect.topleft
        self.p2_score_ones.rect.topright = self.rect.topright

        self.p1_score_ones.set_value(self.p1_score)
        self.p2_score_ones.set_value(self.p2_score)

    def draw(self, surface):
        self.image.fill(pygame.Color('BLACK'))
        self.numerals.draw(self.image)

        surface.blit(self.image, self.position)

    def p1_point(self):
        self.p1_score += 1

    def p2_point(self):
        self.p2_score += 1

    def update(self):
        super().update()
        self.numerals.update()
