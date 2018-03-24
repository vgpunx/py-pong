import pygame


# This is the paddle class.
class Paddle(pygame.sprite.Sprite):
    # paddle sprite
    def __init__(self, x=20, y=50):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 50))  # What the sprite looks like
        self.image.fill(pygame.Color("green"))  # fill the Surface with the color Green
        self.rect = self.image.get_rect()   # The rectangle that encloses the sprite
        self.rect.center = (x, y)
