import pygame

# This is the paddle class.
class Paddle(pygame.sprite.Sprite):
    # paddle sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 50)) # What the sprite looks like
        self.image.fill(pygame.Color("green")) # fill the Surface with the color Green
        self.rect = self.image.get_rect()   # The rectangle that encloses the sprite
        self.rect.center = (20, 50)


# def draw_paddle(screen, x, y):
#     pygame.draw.rect(screen, pygame.Color("green"), [1 + x, y, 10, 50], 0)