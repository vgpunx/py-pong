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

        # variable to increase the overall speed of the ball by adding the offset to speedx and speedy
        self.speed_offset = 0

    def update(self):

        if self.speedy < 0:
            self.rect.y += (self.speedy - self.speed_offset)
        if self.speedy > 0:
            self.rect.y += (self.speedy + self.speed_offset)

        if self.speedx < 0:
            self.rect.x += (self.speedx - self.speed_offset)
        if self.speedx > 0:
            self.rect.x += (self.speedx + self.speed_offset)

        # self.rect.y += (self.speedy + self.speed_offset)
        # self.rect.x += (self.speedx + self.speed_offset)

        # border collision detection
        if self.rect.top < 0:
            self.rect.top = 0
            # reverse y direction
            self.speedy -= self.speedy * 2
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT-1
            # reverse y direction
            self.speedy -= self.speedy * 2
