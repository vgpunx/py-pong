import pygame
from constants import *
vec = pygame.math.Vector2


class Ball(pygame.sprite.Sprite):
    # ball sprite
    def __init__(self, bounds):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(pygame.Color("white"))
        self.rect = self.image.get_rect()
        self.rect.center = (PLAYFIELD_SIZE[0]/2, PLAYFIELD_SIZE[1]/2)

        # Position (start in the middle of the screen)
        self.pos = vec(PLAYFIELD_SIZE[0]/2, PLAYFIELD_SIZE[1]/2)
        # Velocity
        self.vel = vec(0, 0)

        self.bounds = bounds

    # def bounce(self):
    #    bounce = False

        # top and bottom boundary bouncing
    #    if self.rect.top <= self.bounds.top or self.rect.bottom >= self.bounds.bottom:
    #        norm = vec(0, 1)
    #        bounce = True

        # left and right boundary bouncing for test purposes
    #   elif self.rect.left <= self.bounds.left or self.rect.right >= self.bounds.right:
    #       norm = vec(1, 0)
    #       bounce = True

    #  if bounce:
    #      self.vel = self.vel.reflect(norm)
    #      self.move(self.vel)

    def update(self):

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            self.vel.x = -2
            self.vel.y = 2

        # check for collision with a wall
        if self.pos.y < 0:
           self.pos.y = 0 + 1
           self.vel.y -= (self.vel.y * 2)
        if self.pos.y > PLAYFIELD_SIZE[1]:
           self.pos.y = PLAYFIELD_SIZE[1] - 1
           self.vel.y -= (self.vel.y * 2)

        self.pos += self.vel

        self.rect.center = self.pos
