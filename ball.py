from constants import *


class Ball(pygame.sprite.Sprite):
    # ball sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(pygame.Color("white"))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

        # initial speed
        self.speedx = -3
        self.speedy = -3

    def update(self):

        self.rect.y += self.speedy
        self.rect.x += self.speedx

        # collision detection
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedy = 3
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT-1
            self.speedy = -3
