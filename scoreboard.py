import pygame

class Scoreboard:
    def __init__(self, size):
        self.size = size
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()

        self.p1_score = 0
        self.p2_score = 0

        self.position = (0, 0)

    def draw(self, surface):
        self.image.fill(pygame.Color('WHITE'))

        surface.blit(self.image, self.position)